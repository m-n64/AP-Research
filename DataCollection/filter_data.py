import requests
import sys

sys.path.append("../AP-Research")
from API import archive, article_search
from ClassSystem import classes
from Convinience.loop_buffer import validate


from get_months import get_months

if __name__ == "__main__":
    is_displaying = True
else:
    is_displaying = False


def filter_data(month, year, info) -> dict:

    try:

        #get the data from the specific month. first input the month, then input the amount of days (based on month and if it is a leap year), then input the year
        month_data = []




        if is_displaying: print(f"{month}/{year}:") 

        for i in info:
            article_data =  classes.Article(month, year)
            article_data.headline = i["headline"]["main"]
            article_data.published = i["pub_date"]
            article_data.abstract = i["abstract"]
            article_data.url = i["web_url"]
            article_data.keywords = []

            for keyword in i["keywords"]:
                article_data.keywords.append(keyword["value"])
            
            month_data.append(article_data)
            if is_displaying:
                print("------")
                article_data.rundown()
            
        return month_data
    except TypeError:
        return "N/a"