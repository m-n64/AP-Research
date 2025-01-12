import sys
import requests
import csv
sys.path.append("../AP-Research")
from Convinience.loop_buffer import validate


from get_months import get_months

from ClassSystem import classes

if __name__ == "__main__":

    start_month = int(input("start date (MM): "))
    start_year = int(input("start year: (YYYY): "))
    end_month = int(input("end month: "))
    end_year = int(input("end year: "))

    timespan = get_months(start_month, start_year, end_month, end_year)


    with open("./test.csv", "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Date", "Headline", "Abstract", "Keywords", "Link", "Published"])

        for date in timespan:
            month = date[0]
            year = date[1]

            data = classes.Month(month, year)

            print(data.response)

            for article in data.article_list:
                
                if data.article_list.index(article) == 0:
                    writer.writerow([data.date, article.headline, article.abstract, article.keywords, article.url, article.published])
                else:
                    writer.writerow(["", article.headline, article.abstract, article.keywords, article.url, article.published])
            
            if validate("Continue?\n(y/n): ") == True:
                pass
            else:
                print("Cancelling...")
                print(f"Start Again at {data.date}")        

