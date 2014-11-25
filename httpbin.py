import requests, json
from pprint import pprint

payload = {'key1':'value1', 'key2': 'value2'}
data = requests.get("http://httpbin.org/get", params=payload)
#print(data.url)
#print(data.content)
data = json.loads(data.text)

pprint(data)

#for item in data['public'][id0]:
#    print(item)
url = data["url"]
print(url)

print(data["headers"]["Host"])
print(data["args"]["key2"])
print(data["args"]["key1"])