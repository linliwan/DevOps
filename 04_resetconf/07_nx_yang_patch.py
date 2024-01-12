import base64
import requests

host = "192.168.50.245"
username = "admin"
password = "Devnet123"
credentials = bytes(":".join([username, password]), encoding="utf-8")
encoded_credentials = base64.b64encode(credentials)
url = f"https://{host}/restconf/data/Cisco-NX-OS-device:System/bd-items"
headers = {
    'Content-Type': 'application/yang.data+json',
    'Accept': 'application/yang.data+json',
    'Authorization': f'Basic {encoded_credentials.decode("utf-8")}',
}

payload = '''
{
    "bd-items": {
        "BD-list": [
            {
                "fabEncap": "vlan-55",
                "name": "vlan55test"
            }
        ]
    }
}
'''

response = requests.request("PATCH", url, headers=headers, data=payload, verify=False)
print(response.text, response.status_code)
