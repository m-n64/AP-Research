import requests


dates = {
    "start ": {"month": 11, "year": 1961},
    "end" : {"month": 8,"year": 1973}

}


def article_search(month, days: int, year: int, url: str) -> list:

    # url = f'https://api.nytimes.com/svc/search/v2/articlesearch.json?begin_date={year}{month}01&end_date={year}{month}{days}&fq=print_page:1 AND (print_section:("A", "1") OR (!_exists_:print_section))&api-key=AiqnOCCGOOEoohhGGYEGdnXjraJ3mFRj'
        
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
            article_search(month, days, year)
        
        else:
            print(f"Undefined Error...\nmonth:{month}\nurl:{url}")

    elif response.status_code == 429:
        print("Too many requests...")



# get_data(dates["end"]["year"], "01", dates["end"]["month"])
