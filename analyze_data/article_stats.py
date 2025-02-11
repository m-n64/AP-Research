import json
import sys
import os
from fractions import Fraction
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
        self.abstract = data['abstract']
        self.keywords = data['keywords']

        try: self.print_section = data['print_section']
        except AttributeError: self.print_section = 'Undocumented'
        except KeyError: self.print_section = 'Key Error'
        

        pub_date = data['pub_date'].split('+')[0].split('T')
        date = pub_date[0].split('-')
        date = [int(i) for i in date]

        time = pub_date[1].split(':')
        time = [int(i) for i in time]

        self.date = datetime.datetime(date[0], date[1], date[2], time[0], time[1], time[0])
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
        print(f'Abstract: {self.abstract}') 
        print(f'Print Section: {self.print_section}')
        print(f'Published: {self.date.strftime(f"%c")}')
        print(f'URL: {self.link}')
    
        
class File:
    def __init__(self, name, folder, dir):
        # assign preestablished data
        self.name = name
        self.month = int(name.split('-')[0])
        self.year = int(folder)
        self.date = datetime.datetime(self.year, self.month, 1)
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

            load(article, self.data, True, f'[{self.date.strftime(f'%x')}] Loading', f'[{self.date.strftime(f'%x')}] Task Completed')
            
            
        
        self.fpage_percent = percent(len(self.fpages), len(self.data), 2)
        self.fpage_frac = f'{len(self.fpages)}/{len(self.data)}'
        self.fpage_ratio = Fraction(len(self.fpages), len(self.data))


        if len(self.fpages) >= 1: self.usable = True
        else: self.usable = False            

    def get_keywords(self):
        wordcount = {}
        for article in self.fpages:
            for keyword in article.keywords:
                
                value = keyword['value']

                if value not in list(wordcount.keys()): wordcount[value] = {'type': [], 'points': 0}

                type = keyword['name']
                if type not in wordcount[value]['type']: wordcount[value]['type'].append(type)
                
                points = 514-int(keyword['rank'])

                wordcount[value]['points'] += points
        # wordcount = sorted(wordcount.items(), key=lambda word: word['points'])

        

        print(wordcount)

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
        month_list = [int(file.date.strftime("%m")) for file in year.files]
        
        if m < year.files[0].month: m = year.files[0].month
        elif m > year.files[-1].month: m = year.files[-1].month

        month = pick_action(year.files, month_list.index(m) + 1)
    
    # generate the data
    month.get_data()

    file_actions = ['Front Page Stats', 'Keyword Stats', 'Article Actions']

    action = pick_action(file_actions)

    if action == file_actions[0]:
        print(f'{month.fpage_frac}')
        print('---------')
        print(f'Percent: {month.fpage_percent}')
        print(f'Ratio: {month.fpage_ratio}')
    elif action == file_actions[1]:
        print(month.get_keywords())
        #print keywords
    elif action == file_actions[2]:
        #print article actions
        if a == None: article = pick_action(month.fpages)
        else: article = pick_action(month.fpages, a)

        article.rundown()



def pick_action(action_list, response = None):
    
    if response == None:
        for action in action_list:
            print(f'{action_list.index(action) + 1} - {str(action)}')
        print('----------')
        
        response = int(input('Pick an Action: '))
        while response not in range(len(action_list) + 1):
            response = int(input('Pick an Action: '))
        
        print('===========')

    for action in action_list:
        if action_list.index(action) + 1 == response:
            return action
    

    if action == None:
        print(f'{response} not in {action_list}')




if __name__ == '__main__':
    
    folders = os.listdir('./raw_data')

    article_data = [Folder(year, 'raw_data') for year in folders]
    search(article_data, 1961, 11)  
