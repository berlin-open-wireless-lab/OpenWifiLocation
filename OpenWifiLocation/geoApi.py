from openwifi.jobserver.tasks import get_jsonubus_from_uuid
import requests

from .ApiKey import *
from cornice import Service
import json


location = Service(name='location',
                   path='/node/{UUID}/loc',
                   description='Get location data.')

@location.get()
def getLocationWithGoogleAPI(request):
    uuid=request.matchdict['UUID']
    wifi_device="wlan0"

    js = get_jsonubus_from_uuid(uuid)
    scanResults = js.call("iwinfo", "scan", device=wifi_device)[1]["results"]

    geo_api_request = {}
    geo_api_request["wifiAccessPoints"]=[]

    for scan in scanResults:
        geo_api_request['wifiAccessPoints'].append({
                                "macAddress":scan["bssid"],
                                "channel":scan["channel"],
                                "signalStrength":scan["quality"],
                                "signalToNoiseRatio":scan["signal"]
                               })

    geo_api_answer = requests.post('https://www.googleapis.com/geolocation/v1/geolocate?key='+google_api_key, json=geo_api_request)
    return json.loads(geo_api_answer.text)
