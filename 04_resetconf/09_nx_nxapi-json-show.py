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
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': f'Basic {encoded_credentials.decode("utf-8")}'
}

payload = json.dumps(
    {
        "ins_api": {
            "version": "1.0",
            "type": "cli_show",
            "chunk": "0",
            "sid": "sid",
            "input": "show version",
            "output_format": "json"
        }
    }
)

response = requests.request("POST", url, headers=headers, data=payload, verify=False)
print(response.text)
