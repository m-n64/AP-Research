import requests


dates = {
    "start ": {"month": 11, "year": 1961},
    "end" : {"month": 8,"year": 1973}

}


def get_data(year: int, start_month, end_month) -> list:
    url = f'https://api.nytimes.com/svc/search/v2/articlesearch.json?begin_date={year}{start_month}01&end_date={year}{end_month}31&fq=print_page:1 AND (print_section:("A", "1") OR (!_exists_:print_section))&api-key=AiqnOCCGOOEoohhGGYEGdnXjraJ3mFRj'
    response = requests.get(url)
    print(response)
    if response.status_code == 200:

        print(f'hits: {response.json()["response"]["meta"]["hits"]}')
        # print(response.json()["response"]["docs"])
        return response.json()["response"]["docs"]
    
    elif response.status_code == 400:
        print("Bad request... Retrying...")
        
        if (type(start_month) == int) and start_month < 10:
            
            start_month = "0" + str(start_month)
            get_data(year, start_month, end_month)

        elif (type(end_month) == int) and end_month < 10:
            
            end_month = "0" + str(end_month)
            get_data(year, start_month, end_month)
        
        else:
            print(f"Undefined Error...\nstart month:{start_month}\nend month: {end_month}\nurl:{url}")

    elif response.status_code == 429:
        print("Too many requests...")

    


# get_data(dates["end"]["year"], "01", dates["end"]["month"])
