
import os
import json
import sys
import random
import datetime

from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from Useful.percent import percent    
from Useful.dynamic_loading import load
    
class Article:
    def __init__(self, data, file):
        self.file = file
        self.location = file.location
        self.raw = data
        self.index = file.data.index(data)
        self.headline = data['headline']['main']
        self.keywords = data['keywords']
        self.date = data['pub_date']
        self.link = data['web_url']

    def __str__(self):
        return self.headline

    def to_dict(self):
        return {'file': self.location, 'date': self.date, 'headline': self.headline, 'keywords': self.keywords, 'url': self.link}
    
    def rundown(self):
        
        
        print(f'"{self.location}"')
        print('------------')
        print(f'Headline: {self.headline}')
        print(f'Keywords: {' || '.join([term['value'] for term in self.keywords])}')
        print(f'Published: {self.date.split('T')[0]}')
        print(f'URL: {self.link}')
    
        
class File:
    def __init__(self, name, folder, dir):
        # assign preestablished data
        self.name = name
        self.month = int(name.split('-')[0])
        self.year = int(folder)
        self.date = f'{self.month}/{self.year}'
        self.location = f'./{dir}/{folder}/{name}'

    def get_data(self): 
        # assign data according to the file
        with open(str(self.location), 'r') as jsonFile:
            self.raw = json.load(jsonFile)
            self.data = self.raw['response']['docs']

            if len(self.data) != int(self.raw['response']['meta']['hits']):
                print(f"Error!! Totals don't Match! [{self.location}]")
            
            self.copyright = self.raw['copyright']

        #filter articles based on front pages and non front pages
    
        self.fpages = []
        self.extra = []

        for article in self.data:
            #create a new article based on the data
            new_article = Article(article, self)

            #check if it is a front page article
            try:
                if int(article['print_page']) == 1: self.fpages.append(new_article)
                else: self.extra.append(new_article)
            except KeyError:
                self.extra.append(new_article)

            load(article, self.data, True, f'[{self.date}] Loading', f'[{self.date}] Task Completed')
            
            
        
        self.fpage_percent = percent(len(self.fpages), len(self.data), 2)
        

        if len(self.fpages) >= 1: self.usable = True
        else: self.usable = False            

    def __str__(self):
        return self.name
    

        


class Folder:
    def __init__(self, name, dir):
        self.year = int(name)
        self.location = f'./{dir}/{name}'
        
        # create list of files
        self.files = []
        for file in sorted(os.listdir(self.location), key=lambda date: int(date.split('-')[0])):
            self.files.append(File(file, name, dir))
        

    def total_fpages(self):
        # create fpage_stats
        self.abs_fpages = 0
        self.abs_total = 0

        for file in self.files:
            while (True):
                try:
                    self.abs_fpages += len(file.fpages)
                    self.abs_total += len(file.data)
                    break
                except AttributeError:
                    file.get_data()

        self.fpage_percent = percent(self.abs_fpages, self.abs_total, 2)


        

    def __str__(self):
        return self.location
    


def search(data, y = None, m = None, a = None):


    # if no year specified, pick one
    if y == None:
        year = pick_action(data)
    else:
        year = pick_action(data, y-1960)

    # if no month specified, pick one
    if m == None:
        month = pick_action(year.files)
    else:
        if m < year.files[0].month: m = year.files[0].month
        elif m > year.files[-1].month: m = year.files[-1].month

        month = pick_action(year.files, m) 
    
    # generate the data
    month.get_data()

    file_actions = ['Front Page Stats', 'Keyword Stats', 'Article Actions']

    action = (file_actions)

    if action == file_actions[0]:
        pass
        #print fpage stats
    elif action == file_actions[1]:
        pass
    elif action == file_actions[2]:
        if a == None: article = pick_action(month.fpages)
        else: article = pick_action(month.fpages, a)

        return article


        


def pick_action(action_list, response = None):
    
    if response == None:
        for action in action_list:
            print(f'{action_list.index(action) + 1} - {str(action)}')
        print('----------')
        
        while (response := int(input('Pick an Action: '))) not in range(len(action_list) + 1):
            response = int(input('Pick an Action: '))
        
        print('===========')

    for action in action_list:
        if action_list.index(action) + 1 == response:
            return action




folders = os.listdir('./raw_data')
    
article_data = [Folder(year, 'raw_data') for year in folders]
        

if __name__ == '__main__':


    file = search(article_data, 1971, 11)





