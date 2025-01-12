
import sys
import requests
from article_classes import Article

sys.path.append("../AP-Research")

from API.article_search import article_search
from DataCollection.filter_data import filter_data

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

        self.url = f'https://api.nytimes.com/svc/search/v2/articlesearch.json?begin_date={year}{month}01&end_date={year}{month}{self.days}&fq=print_page:1 AND (print_section:("A", "1") OR (!_exists_:print_section))&api-key=AiqnOCCGOOEoohhGGYEGdnXjraJ3mFRj'
        self.date = f'{self.month}/{self.year}'
        self.results = 0
        self.article_list = "N/a"



        

    def rundown(self):
        print(f'{self.date}:')
        print(f'Link: {self.url}')
        print(f'Results: {self.results}')
        print("----")
        print(f'Article List:')
        print(self.article_list)



    def create_list(self):
        info =  article_search(self.month, self.days, self.year, self.url)
        self.article_list = filter_data(self.month, self.year, info)
        




        
        
    
