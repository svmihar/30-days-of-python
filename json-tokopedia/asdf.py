import pandas as pd 
import json 
import requests



url = 'https://www.tokopedia.com/reputationapp/review/api/v2/product/269922085?page=1&total=20'

kumpulan_url = []
for i in range(1, 401): 
    kumpulan_url.append(f'https://www.tokopedia.com/reputationapp/review/api/v2/product/269922085?page={i}&total=20')

print(kumpulan_url)


for index, link in enumerate(kumpulan_url): 
    req = requests.get(link)
    data_json = req.json()
    with open(f'file.json', 'a+') as f: 
        json.dump(data_json['data']['list'], f)
    # print()

