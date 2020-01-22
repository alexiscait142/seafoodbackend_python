import os 
import requests

def get_fishs():
    url = 'https://www.fishwatch.gov/api/species'
    r = requests.get(url, headers={'Content-Type': 'application/json'})
    fish = r.json()
    fish_list = []
    for i in fish:
        fish_list.append(i['Species Name'])
    return fish

get_fishs()