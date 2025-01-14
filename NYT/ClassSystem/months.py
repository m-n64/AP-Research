
import sys
import requests

sys.path.append("C:/Users/retro/Documents/GitHub/AP-Research/NYT")
from ClassSystem import article

from API.article_search import article_search



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
        self.article_list = article.filter_data(self.month, self.year, info)
        

        

    def rundown(self):
        print(f'{self.date}:')
        print(f'Results: {self.results}')
        print("----")
        print(f'Article List:')
        print(self.article_list)

if __name__ == "__main__":
    test_month = Month(11, 1961)
    print(test_month.article_list[0].__dict__)




        
        
    
