import requests
import json
from bs4 import BeautifulSoup

url = 'https://untrusted-root.badssl.com/'
r = requests.get(url,verify='/home/mprstacic/scripts/badssl-com-root.pem')

print(r.status_code)
print(r.text)

html_body = BeautifulSoup(r.text, 'html.parser')
print(html_body)