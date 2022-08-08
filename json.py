import json
import pandas as pd

with open('nodes with links.json','r',encoding='utf-8') as f:
    content = f.read()
if content.startswith(u'\ufeff'):
    content = content.encode('utf8')[3:].decode('utf8')
i = json.loads(content,strict=False)

with open('datasets.json','r',encoding='utf-8') as f1:
    newcontent = f1.read()
if newcontent.startswith(u'\ufeff'):
    newcontent = newcontent.encode('utf8')[3:].decode('utf8')
j = json.loads(newcontent,strict=False)
print(type(i))
print(type(j))
nodes = []
for n in i:
    nodes.append(n.get('m'))
for n in j:
    nodes.append(n.get('n'))

new_nodes = []
for i in nodes:
    if i not in new_nodes:
        new_nodes.append(i)


for i in new_nodes:
    if 'ns0__Dataset' in i.get("labels"):
        i['dataset'] = True
for i in new_nodes:
    if 'ns1__title' in i.get("properties").keys():
        i['name'] = i.get("properties")['ns1__title']


for i in new_nodes:
    if 'education' in i.get("labels"):
        i["labels"] = int(0)
    elif 'energy' in i.get("labels"):
        i["labels"] = int(1)
    elif 'health' in i.get("labels"):
        i["labels"] = int(2)
    elif 'cities' in i.get("labels"):
        i["labels"] = int(3)
    elif 'transport' in i.get("labels"):
        i["labels"] = int(4)
    elif 'international' in i.get("labels"):
        i["labels"] = int(5)

for i in new_nodes:
    i['id'] = i.pop('identity')
    i['category'] = i.pop('labels')
for i in new_nodes:
    i['id'] = str(i['id'])




with open('links.json','r',encoding='utf-8') as f:
    content = f.read()
if content.startswith(u'\ufeff'):
    content = content.encode('utf8')[3:].decode('utf8')
j = json.loads(content,strict=False)

print(type(j))
links = []

for link in j:
    if link.get('p')['segments'][0]['relationship']['type'] == 'ns0__landingPage':
        url = link.get('p')['segments'][0]['end']['properties']['uri']
        dataset_id = str(link.get('p')['segments'][0]['relationship']['start'])
        for node in new_nodes:
            if node['id'] == dataset_id:
                node['properties']['uri'] = url

for link in j:
    '''print(link)
    print(type(link))
    print(link.get('p')['start']['identity'])
    print(link.get('p')['end']['identity'])
    print(link.get('p')['segments'][0]['relationship']['type'])'''
    each_link = {"source":link.get('p')['start']['identity'],"target": link.get('p')['end']['identity'],"name":link.get('p')['segments'][0]['relationship']['type']}
    links.append(each_link)
print('dfghjvcvbjyfjkjhgfcvnjmk')
#print(links)
for i in links:
    i["source"] = str(i["source"])
    i["target"] = str(i["target"])
categories = [
      {
        "name": "education"
      },
      {
        "name": "energy"
      },
      {
        "name": "health"
      },
      {
        "name": "cities"
      },
      {
        "name": "transport"
      },
      {
        "name": "international"
      },
]

all = {"nodes": new_nodes,"links": links,"categories":categories}
#print(all)

with open('data.json','w') as json_file:
    json_file.write(json.dumps(all,indent=4))


