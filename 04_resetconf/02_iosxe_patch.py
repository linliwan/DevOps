import base64
import requests
import json

username = "devnet"
password = "devnet"
credentials = bytes(":".join([username, password]), encoding="utf-8")
encoded_credentials = base64.b64encode(credentials)
url = "https://192.168.50.241/restconf/data/Cisco-IOS-XE-native:native/hostname"
headers = {
    'Content-Type': 'application/yang-data+json',
    'Accept': 'application/yang-data+json',
    'Authorization': f'Basic {encoded_credentials.decode("utf-8")}',
}

# ############### from string
# payload = '''
# {
#   "hostname": "c8000v_2"
# }
# '''

# ############### from python dict
# hostname_dict = {
#     "hostname": "c8000v_3"
# }
# payload = json.dumps(hostname_dict)

# ############### from json file
with open("02_hostname.json") as f:
    payload = f.read()

response = requests.request("PATCH", url, headers=headers, data=payload, verify=False)
print(response.status_code)












# response.raise_for_status()
# try catch (try except)



