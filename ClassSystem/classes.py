
import sys
import requests

sys.path.append("../AP-Research")

from API.article_search import article_search
from DataCollection.filter_data import filter_data


class Article:

    def __init__(self, month, year):
        self.headline = "None"
        self.abstract = "None"
        self.published = "Unknown"
        self.month = month
        self.year = year
        self.keywords = "Unknown"
        self.url = ""
        self.date = f'{self.month}/{self.year}'




    def rundown(self):
        print(f'Published: {self.published}')
        print(f'Headline: {self.headline}')
        print(f'Abstract: {self.abstract}')
        print(f'Keywords: {self.keywords}')
        print(f'Link: {self.url}')



class Month:

    def __init__(self, month, year):
        self.month = month
        self.year = year

        #gets the number of days within the month
        odd_months = [1, 3, 5, 7, 8, 10, 12]
        if self.month in odd_months:
            self.days = 31
        elif self.month == 2:
            if self.year % 4 == 0:
                self.days = 29
            else:
                self.days = 28
        else:
            self.days = 30

        self.date = f'{self.month}/{self.year}'
        self.results = 0
        
        info =  article_search(self.month, self.days, self.year)
        self.article_list = filter_data(self.month, self.year, info)
        
        if info == 429:
            self.response = 429
        else:
            self.response = 200

        

    def rundown(self):
        print(f'{self.date}:')
        print(f'Link: {self.url}')
        print(f'Results: {self.results}')
        print("----")
        print(f'Article List:')
        print(self.article_list)        




        
        
    
