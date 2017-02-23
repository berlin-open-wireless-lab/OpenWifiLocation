from setuptools import setup, find_packages

setup(
    name='OpenWifiLocation',
    version="0.1",
    description="Location for OpenWifi",
    author="Johannes Wegener",
    install_requires=["OpenWifi"],
    entry_points="""
    [OpenWifi.plugin]
    """,
    packages=find_packages(),
    include_package_data=True,
)
