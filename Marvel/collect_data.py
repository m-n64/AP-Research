import requests
from datetime import datetime
import hashlib
import json
import os
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent))
from keys import Marvel_public as public
from keys import Marvel_private as private

ts = datetime.now()
hash = hashlib.md5(f'{ts}{private}{public}'.encode()).hexdigest()


class Hero:
    def __init__(self, name, titles):
        self.name = name
        
        try: os.mkdir(f'./Marvel/raw_data')
        except FileExistsError: pass
        try: os.mkdir(f'./Marvel/raw_data/{name}')
        except FileExistsError: pass
    
        self.id = self.get_data('characters')[0]['id']        
        self.comics = {}
        
        for i in titles:
            for series in self.get_data('series'):
                if i == series['title']:
                    self.comics[i] = {
                        'id': series['id'],
                        'issues': []
                    }
                    break
        

        print(f'making comics for {name}')
        for series in self.comics:
            for comic in self.get_data('comics'):

                if series == comic['series']['name']:
                    self.comics[series]['issues'].append({
                        'issueNumber': comic['issueNumber'],
                        'id': comic['id'],
                        'published': comic['dates'][0]['date']
                    })


    def __str__(self):
        return self.name

    def get_data(self, entity):

        url = f'http://gateway.marvel.com/v1/public/{entity}?&ts={ts}&apikey={public}&hash={hash}'

        if entity == 'characters':
            url += f'&name={self.name}'

        elif entity == 'series':
            url += f'&contains=comic&limit=100&orderBy=startYear&characters={self.id}'
        elif entity == 'comics':
            url += f'&dateRange=1961-11-01,1973-08-31&series={",".join([str(self.comics[i]['id']) for i in self.comics])}&orderBy=onsaleDate&characters={self.id}&format=comic&formatType=comics&noVariants=True&limit=100'
            url2 = url + '&offset=100'

        
        
        if os.path.isfile(f'{Path(__file__).parent}/raw_data/{self.name}/{entity}.json') == False:

            response = requests.get(url).json()
            try: 
                response2 = requests.get(url2).json()
                response['data']['count'] += response2['data']['count']
                response['data']['limit'] += response2['data']['limit']
                response['data']['results'].extend(response2['data']['results'])
            except UnboundLocalError:
                print(f'entity == {entity}')

            


            with open(f'./Marvel/raw_data/{self.name}/{entity}.json', 'w', encoding='utf-8') as jsonFile:
                json.dump(response, jsonFile, indent=4)

        with open(f'./Marvel/raw_data/{self.name}/{entity}.json', 'r', encoding='utf-8') as jsonFile:
            
            return json.load(jsonFile)['data']['results']


    def to_df(self):
        
        df = []

        for series in self.comics:
        
            issue_list = self.comics[series]['issues']
            
            on_sale_dates = [datetime.strptime(issue['published'], f'%Y-%m-%dT%H:%M:%S%z') for issue in issue_list]

            df.append({
                'Series': [series] * len(issue_list),
                'Issues': [issue['issueNumber'] for issue in issue_list],
                'Cover Date': [date.strftime(f'%b. %Y') for date in on_sale_dates],
                'On Sale Date': on_sale_dates
            })
        
        return df




hero_data = {
    'Spider-Man (Peter Parker)' : [
        'Amazing Fantasy (1962)',
        'The Amazing Spider-Man (1963 - 1998)',
        'Amazing Spider-Man Annual (1964 - 2018)',
        'Spectacular Spider-Man (1968)'
    ],
    'Captain America': [
        'Tales of Suspense (1959 - 1968)',
        'Captain America (1968 - 1996)',
        'Captain America Annual (1971 - 1991)'
    ],
    'Fantastic Four': [
        'Fantastic Four (1961 - 1998)',
        'Fantastic Four Annual (1963 - 1994)'
    ]
}


sample = [Hero(char, hero_data[char]) for char in hero_data]
