import requests
import sys

import article_search
from get_months import get_months

dates = get_months([11, 1961], [8, 1973])


data = {}

for i in dates:
    data[f"{i[0]}/{i[1]}"] = ""


for i in data:
    print(i)