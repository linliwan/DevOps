import requests
import json
from pprint import pprint
username = "devnet"
password = "devnet"
url = "https://192.168.50.241/restconf/data/Cisco-IOS-XE-native:native/interface/Loopback"

headers = {
    'Content-Type': 'application/yang-data+json',
    'Accept': 'application/yang-data+json',
    "Authorization": "Basic ZGV2bmV0OmRldm5ldA=="
}
payload = {}

# response = requests.request("get", url, headers=headers, data=payload, auth=(username, password),verify=False)
# with open("01_iosxe_get.json", "w") as f:
#     json.dump(response.json(), f, indent=4)

response = requests.request("get", url, headers=headers, verify=False, data=payload)
pprint(response.text)

