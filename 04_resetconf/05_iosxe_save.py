import base64
import requests
import json

username = "devnet"
password = "devnet"
credentials = bytes(":".join([username, password]), encoding="utf-8")
encoded_credentials = base64.b64encode(credentials)
url = "https://192.168.50.241/restconf/operations/cisco-ia:save-config/"
headers = {
    'Content-Type': 'application/yang-data+json',
    'Accept': 'application/yang-data+json',
    'Authorization': f'Basic {encoded_credentials.decode("utf-8")}',
}
payload = {}

response = requests.request("POST", url, headers=headers, data=payload, verify=False)
print(response.status_code)
print(response.text)
