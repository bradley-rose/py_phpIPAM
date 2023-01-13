#!/usr/bin/env Python
__author__ = "Bradley Rose"
__version__ = "0.1"
"""
Samples on how to read data from phpIPAM and output it to JSON.
"""

import phpipam_API as ipamAPI
import json

ipam = ipamAPI.IPAM(
        "", #API User with read permissions
        "", #API Key for user with read permissions
        "" # No trailing forward slash
    )

def main():
    # Set a section ID to obtain subnets from a particular section with phpIPAM.
    sectionID = 0
    subnets = ipam.getSubnetsBySection(sectionID)['data']
    with open("subnets.json", "w") as outFile:
        json.dump(subnets, outFile)

    locations = ipam.getLocation()['data']
    with open("locations.json","w") as outFile:
        json.dump(locations, outFile)

    deviceTypes = ipam.getDeviceTypes()['data']
    with open("deviceTypes.json","w") as outFile:
        json.dump(deviceTypes, outFile)

    devices = ipam.getDevices()['data']
    with open("devices.json","w") as outFile:
        json.dump(devices, outFile)

    vlans = ipam.getVLANs()['data']
    with open("vlans.json","w") as outFile:
        json.dump(vlans, outFile)

if __name__ == "__main__":
    main()