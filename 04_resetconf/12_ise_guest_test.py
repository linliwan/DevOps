import base64
import requests
import json
from pprint import pprint

host = "ise.abc.com"
sponsor_user = "sponsorlinliwan"
sponsor_password = "Devnet123"
# credential encoding
creds = bytes(':'.join((sponsor_user, sponsor_password)), encoding='utf-8')
encoded_creds = bytes.decode(base64.b64encode(creds))
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': f"Basic {encoded_creds}"
}
guest_base_url = f"https://{host}:9060/ers/config/guestuser"

response = requests.request("GET", guest_base_url + "?size=3&page=1", verify=False, headers=headers)
user_list = response.json()['SearchResult']['resources']
guest_list = []
for item in user_list:
    user_id = item['id']
    response1 = requests.request("GET", guest_base_url + '/' + user_id, verify=False, headers=headers)
    json_response = response1.json()
    json_response['GuestUser'].pop("link")
    json_response['GuestUser'].pop("customFields")
    json_response['GuestUser']['portalId'] = "b7e7d773-7bb3-442b-a50b-42837c12248a"
    guest_list.append(json_response)

pprint(guest_list)




