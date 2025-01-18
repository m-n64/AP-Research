import requests

import sys
from pathlib import Path
sys.path.append(Path(__file__).resolve().parent.parent)


from API import archive, article_search
from Convenience.loop_buffer import validate

from DataCollection.get_months import get_months


class Article:

    def __init__(self, month, year):
        
        self.date = f'TBD'
        self.headline = "None"
        self.abstract = "None"
        self.published = "Unknown"
        self.month = month
        self.year = year
        self.keywords = "None"
        self.url = "None"




    def rundown(self):
        print(f'Published: {self.date}')
        print(f'Headline: {self.headline}')
        print(f'Abstract: {self.abstract}')
        print(f'Keywords: {self.keywords}')
        print(f'Link: {self.url}')



def filter_data(month, year, info) -> dict:

    try:

        #get the data from the specific month. first input the month, then input the amount of days (based on month and if it is a leap year), then input the year
        month_data = []




        if __name__ == "__main__": print(f"{month}/{year}:") 

        for i in info:
            article_data =  Article(month, year)
            article_data.headline = i["headline"]["main"]
            article_data.published = i["pub_date"].split("T")[0]
            article_data.time = i["pub_date"].split("T")[1]
            article_data.abstract = i["abstract"]
            article_data.url = i["web_url"]
            article_data.keywords = []

            for keyword in i["keywords"]:
                article_data.keywords.append(keyword["value"])
            
            month_data.append(article_data)
            if __name__ == "__main__":
                print("------")
                article_data.rundown()
            
        return month_data
    except TypeError:
        return "N/a"