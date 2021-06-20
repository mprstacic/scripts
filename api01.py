import requests
import json

url = 'https://www.virustotal.com/vtapi/v2/file/scan'
params = {'apikey': '<YOUR_API_KEY_HERE>'}
files = {'file': ('sample.pdf', open('sample.pdf', 'rb'))}
response = requests.post(url, files=files, params=params)
print(response.json())
print(response.headers)
print(response.status_code)

with open('web.json', 'w', encoding='utf-8') as f:
    json.dump(response.json(), f, ensure_ascii=True, indent=4)