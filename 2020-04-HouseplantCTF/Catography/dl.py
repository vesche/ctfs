import json
import requests

with open('output.har') as f:
    data = json.loads(f.read())

urls = [i['request']['url'] for i in data['log']['entries']]

for url in urls:
     with open('cat_pics/' + url.split('/')[-1], 'wb') as f:
         f.write(requests.get(url).content)
