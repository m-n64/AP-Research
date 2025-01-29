import json
import os

for year in os.listdir('./data'):

    for month in os.listdir(f'./data/{year}'):

        count = 0

        with open(f'./data/{year}/{month}') as jsonFile:
            data = json.load(jsonFile)['response']['docs']

            for article in data:
                print(article)
            
        print(f'{month}/{year} has {count} usable articles.')