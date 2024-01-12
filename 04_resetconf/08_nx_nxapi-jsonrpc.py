import base64
import requests
import json

host = "192.168.50.245"
username = "admin"
password = "Devnet123"
credentials = bytes(":".join([username, password]), encoding="utf-8")
encoded_credentials = base64.b64encode(credentials)
url = f"https://{host}/ins"
headers = {
    'Content-Type': 'application/json-rpc',
    'Accept': 'application/json-rpc',
    'Authorization': f'Basic {encoded_credentials.decode("utf-8")}'
}
payload = json.dumps(
    [
        {
            "jsonrpc": "2.0",
            "method": "cli",
            "params": {
                "cmd": "interface e1/8",
                "version": 1
            },
            "id": 1
        },
        {
            "jsonrpc": "2.0",
            "method": "cli",
            "params": {
                "cmd": "description configured by jsonrpc",
                "version": 1
            },
            "id": 2
        },
        {
            "jsonrpc": "2.0",
            "method": "cli",
            "params": {
                "cmd": "no switchport",
                "version": 1
            },
            "id": 3
        },
        {
            "jsonrpc": "2.0",
            "method": "cli",
            "params": {
                "cmd": "ip address 8.8.8.1 255.255.255.0",
                "version": 1
            },
            "id": 4
        },
        {
            "jsonrpc": "2.0",
            "method": "cli",
            "params": {
                "cmd": "no shutdown",
                "version": 1
            },
            "id": 5
        }
    ]
)

response = requests.request("POST", url, headers=headers, data=payload, verify=False)
print(response.text)
