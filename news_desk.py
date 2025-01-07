import get_data
import get_months

news_desks = []

time_period = get_months.get_months([11, 1961], [8, 1973])

for date in time_period:
    month_data = get_data.make_url(date[0], date[1])
    try:
        for article in month_data:
            if article["news_desk"] not in news_desks:
                news_desks.append(article["news_desk"])
    except TypeError:
        pass


for i in news_desks:
    print(i)


                