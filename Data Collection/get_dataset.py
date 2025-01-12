

import sys

sys.path.append("./API")

from API import archive
import get_months
import top10


#gets the range of months to pull from
time_period = get_months.get_months([11, 1961], [8, 1973])


#does this for every month

for date in time_period:

    try: 
        month_data = archive.make_url(date[0], date[1])
        list = top10.top_10(top10.word_count(month_data))
        print(list)
    except TypeError:
        pass


