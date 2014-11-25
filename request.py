import requests

import requests,string
import simplejson as json
from pprint import pprint
data = requests.get('https://api.github.com/events')
data = json.loads(data.text)
pprint(data)
#for item in data['public'][id0]:
#    print(item)
for key, val in data.items():
    print key, val
#print(data.text)
#print(data.json)
