import requests
import json

url ='https://api.github.com/events'
payload={'some':'data'}
r = requests.post(url, data=json.dumps(payload))
print(r.text)
print(r.json)
