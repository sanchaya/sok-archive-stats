import pandas as pd
import requests
import json

max_url_per_req = 50

csv_file = 'search.csv'

views_list = []

api_url = "https://be-api.us.archive.org/views/v1/short/"

all_column = pd.read_csv(csv_file)

identifier = list(all_column['identifier'])

try:
    all_column.pop('views')
except:
    pass

def append_to_views_list(views, datas):
    for data in datas:
        views.append(datas[data]['all_time'])
    print("completed ===========", len(views), "rows")
        
i = 0
while i < len(identifier):
    joint = ','.join(identifier[i:min(len(identifier), i + max_url_per_req)])
    i += max_url_per_req
    url = api_url + joint
    resp = requests.get(url)
    json_data = json.loads(resp.content)
    append_to_views_list(views_list, json_data)

all_column['views'] = views_list

all_column.to_csv('new_csv.csv', encoding='utf-8')
