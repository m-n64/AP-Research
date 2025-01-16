import requests
import csv
import os

from Convenience.loop_buffer import validate

from get_months import get_months

from ClassSystem.months import Month


def write_csv(timespan):

    for date in timespan:
        month = date[0]
        year = date[1]

        current_month = Month(month, year)
        writer.writerow([current_month.date, "-----", "-----", "-----", "-----", "-----", "-----"])
        
        for article in current_month.article_list:
            try:
                writer.writerow(["-----", article.headline, article.abstract, article.keywords, article.url, article.published, article.time])
            except AttributeError:
                pass
                # print(article)
        

        if date != timespan[-1]:
            if (validate("Continue?\n(y/n): ") == True):
                pass
            else:
                print("Cancelling...")
                print(f"The next entry will be {current_month.date}.")
                break

if __name__ == "__main__":

    start_month = 11 # int(input("start date (MM): "))
    start_year = 1961 # int(input("start year: (YYYY): "))
    end_month = 8 # int(input("end month: "))
    end_year = 1973 # int(input("end year: "))



    try:
 
        with open("article.csv", "x") as csvfile:
            writer = csv.writer(csvfile) 
            writer.writerow(["Date", "Headline", "Abstract", "Keywords", "Link", "Publ.", "Time"])
            write_csv(get_months(start_month, start_year, end_month, end_year))

    except FileExistsError:

        last_date = "N/a"

        with open("article.csv", "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reversed(reader):
                try: 
                    # if (row[0] != "Date") or (row[0]): last_date = row[0]
                    print(f'Starting at {row[0]}')
                    split_date = row[0].split("/")
                    start_month = int(split_date[0]) + 1
                    start_year = int(split_date[1])

                    if start_month == 13:
                        start_month = 1
                        start_year += 1

                                                
                except IndexError:
                    pass
            
        if last_date != "N/a":     
            print(f'Starting at {last_date}')
            split_date = last_date.split("/")

            start_month = int(split_date[0]) + 1
            start_year = int(split_date[1])

            if start_month == 13:
                start_month = 1
                start_year += 1

        if (start_month != end_month) and (start_year != end_year):

            with open("article.csv", "a") as csvfile:
                writer = csv.writer(csvfile) 
                write_csv(get_months(start_month, start_year, end_month, end_year))


    # with open("./test.csv", "r") as csvfile:
    #     reader = csv.reader(csvfile)
    #     for row in reader:
    #         print(row)
