from setuptools import setup, find_packages

setup(
    name='OpenWifiLocation',
    version="0.1",
    description="Location for OpenWifi",
    author="Johannes Wegener",
    install_requires=["OpenWifi", "requests"],
    entry_points="""
    [OpenWifi.plugin]
    addPluginRoutes=OpenWifiLocation:addPluginRoutes
    """,
    packages=find_packages(),
    include_package_data=True,
)
