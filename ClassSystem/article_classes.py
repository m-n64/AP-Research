import requests
import sys

sys.path.append("../AP-Research")
from API.article_search import check_days

class Article:

    def __init__(self, month, year):
        self.headline = "None"
        self.abstract = "None"
        self.published = "Unknown"
        self.month = month
        self.year = year
        self.keywords = "Unknown"



    def rundown(self):
        print(f'Published: {self.published}')
        print(f'Headline: {self.headline}')
        print(f'Abstract: {self.abstract}')
        print(f'Keywords: {self.keywords}')


    
