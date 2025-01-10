import requests

import archive
import article_search
from get_months import get_months



def collect_data(month, year) -> dict:

    try:
        info = article_search.get_data(month, article_search.check_days(month, year), year)
        month_data = []

        print(f"{month}/{year}:")


        for i in info:
            article_data =  {}
            article_data["headline"] = i["headline"]["main"]
            article_data["pub_date"] = i["pub_date"]
            article_data["abstract"] = i["abstract"]

            article_data["keywords"] = []

            for keyword in i["keywords"]:
                article_data["keywords"].append(keyword["value"])
            
            month_data.append(article_data)
            
            print("------")
            print(f'Published: {article_data["pub_date"]}')
            print(f'Headline: {article_data["headline"]}')
            print(f'Abstract: {article_data["abstract"]}')
            print(f'Keywords: {article_data["keywords"]}')
            
        return month_data
    except TypeError:
        return "N/a"
     
    




file = {}


for i in (dates := get_months([11, 1961], [8, 1973])):

    month = i[0]
    year = i[1]
    

    file[f"{month}/{year}"] = collect_data(month, year)


    if (check := input("continue? (y/n) ")) == "y":
        pass
    elif check == "n":
        break
    else:
        check = input("continue? (y/n) ")
