import requests

import article_search
from get_months import get_months

dates = get_months([11, 1961], [8, 1973])


dataset = {}

# for i in dates:


#     month = i[0]
#     year = i[1]
#     archive = article_search.get_data(year, month, month)

#     dataset[f"{month}/{year}"]["headline"] = 
#     dataset[f"{month}/{year}"]["snippet"] = 
#     dataset[f"{month}/{year}"]["keywords"] = 


# print(article_search.get_data(1961, 11, 12))


url = f'https://api.nytimes.com/svc/search/v2/articlesearch.json?begin_date=19611101&end_date=19611130&fq=print_page:1 AND (print_section:("A", "1") OR (!_exists_:print_section))&api-key=AiqnOCCGOOEoohhGGYEGdnXjraJ3mFRj'
response = requests.get(url)
print(response.json())