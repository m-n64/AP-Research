import requests
import sys

sys.path.append("../AP-Research")
from API import archive, article_search
from ClassSystem.article_classes import Article


from get_months import get_months


def filter_data(month, year, info) -> dict:

    try:

        #get the data from the specific month. first input the month, then input the amount of days (based on month and if it is a leap year), then input the year
        month_data = []

        print(f"{month}/{year}:")


        for i in info:
            article_data =  Article(month, year)
            article_data.headline = i["headline"]["main"]
            article_data.published = i["pub_date"]
            article_data.abstract = i["abstract"]

            article_data.keywords = []

            for keyword in i["keywords"]:
                article_data.keywords.append(keyword["value"])
            
            month_data.append(article_data)
            print("------")
            article_data.rundown()
            
        return month_data
    except TypeError:
        return "N/a"
     
    




file = {}


for i in (dates := get_months([11, 1961], [8, 1973])):

    month = i[0]
    year = i[1]
    

    file[f"{month}/{year}"] = filter_data(month, year)


    if (check := input("continue? (y/n) ")) == "y":
        pass
    elif check == "n":
        break
    else:
        check = input("continue? (y/n) ")
