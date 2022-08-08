'''
The code to collect the data is obtained by calling the API of the European Data Portal,
which provides direct download of the data,
and by finding the underlying API of the web page to download the data in bulk.
'''
import requests
import random
import csv
import json
import time

headers = {
'authority':'data.europa.eu',
'accept':'application/json, text/plain, */*',
'accept-language':'zh-CN,zh;q=0.9',
'cookie':'ppms_privacy_17a3f28e-e00f-4d28-a2eb-0a82687dbc96={%22consents%22:{%22analytics%22:{%22status%22:-1%2C%22updatedAt%22:%222022-07-09T09:42:28.775Z%22}}%2C%22domain%22:{%22normalized%22:%22data.europa.eu%22%2C%22isWildcard%22:false%2C%22pattern%22:%22data.europa.eu%22}}; _pk_ses.17a3f28e-e00f-4d28-a2eb-0a82687dbc96.7c27=*; _pk_id.17a3f28e-e00f-4d28-a2eb-0a82687dbc96.7c27=9036531db5add22a.1657359751.4.1658847135.1658847033.',
'referer':'https://data.europa.eu/data/datasets?locale=en&categories=TRAN&page=2',
'sec-ch-ua':'".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
'sec-ch-ua-mobile':'?0',
'sec-ch-ua-platform':'"macOS"',
'sec-fetch-dest':'empty',
'sec-fetch-mode':'cors',
'sec-fetch-site':'same-origin',
}


def get_url():
    for i in range(1, 269, 1):
        print('page', i)
        time.sleep(3)
        url = 'https://data.europa.eu/api/hub/search/search?q=&filter=dataset&limit=15&page='\
              +str(i)+'&sort=relevance+desc,+modified+desc,+title.en+asc&facetOperator=AND&facetGroupOperator=AND&dataServices=false&includes=id,' \
                      'title.en,description.en,languages,modified,issued,catalog.id,catalog.title,catalog.country.id,distributions.id,distributions.' \
                      'format.label,distributions.format.id&facets={"country":[],"catalog":[],"categories":["TRAN"],"publisher":[],"keywords":[],' \
                      '"dataServices":[],"scoring":[],"format":[],"license":[]}'


        request = requests.get(url, headers=headers)
        print(request)
        response = json.loads(request.text)
        result = response['result']['results']
        for link in result:
            link_id = link['id'].replace('-', '')
            print(link_id)
            dower_url = 'https://data.europa.eu/api/hub/repo/datasets/{}.rdf?useNormalizedId=true&locale=en'.format(link_id)
            print(dower_url)
            fr(dower_url, link_id)
def fr(dower_url, link_id):
    res = requests.get(dower_url, headers=headers)

    with open('/Users/liyuning/Documents/Data science/Individual Project/latestdata/transport' + link_id+'.rdf', 'wb') as download:
        download.write(res.content)

get_url()