import requests


dates = {
    "start ": {"month": 11, "year": 1961},
    "end" : {"month": 8,"year": 1973}

}


def get_data(month, days, year: int) -> list:

    url = f'https://api.nytimes.com/svc/search/v2/articlesearch.json?begin_date={year}{month}01&end_date={year}{month}{days}&fq=print_page:1 AND (print_section:("A", "1") OR (!_exists_:print_section))&api-key=AiqnOCCGOOEoohhGGYEGdnXjraJ3mFRj'
        
    response = requests.get(url)
    print(response)
    if response.status_code == 200:

        print(f'hits: {response.json()["response"]["meta"]["hits"]}')
        print(f'We did it... We got the data from {month}/1/{year}, to {month}/{days}/{year}...')
        print("------------------")
        # print(response.json()["response"]["docs"])
        return response.json()["response"]["docs"]
    
    elif response.status_code == 400:
        print("Bad request... Retrying...")
        
        if (type(month) == int) and month < 10:
            
            month = "0" + str(month)
            get_data(month, days, year)
        
        else:
            print(f"Undefined Error...\nmonth:{month}\nurl:{url}")

    elif response.status_code == 429:
        print("Too many requests...")

    
def check_days(month, year):

    odd_months = [1, 3, 5, 7, 8, 10, 12]

    if month in odd_months:
        return 31
    elif month == 2:
        if year % 4 == 0:
            return 29
        else:
            return 28
    else:
        return 30



# get_data(dates["end"]["year"], "01", dates["end"]["month"])
