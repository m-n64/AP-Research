import requests



def get_data(year: int, start_day: str, end_day: str) -> list:
    try:
        url = f'https://api.nytimes.com/svc/search/v2/articlesearch.json?begin_date={year}{start_day}&end_date={year}{end_day}&fq=print_page:1print_page:1 AND (print_section:("A", "1") OR (!_exists_:print_section))&sort=oldest&api-key=AiqnOCCGOOEoohhGGYEGdnXjraJ3mFRj'
        response = requests.get(url)
        print(response)
        print(f'hits: {response.json()["response"]["meta"]["hits"]}')
        return response.json()["response"]["docs"]
    except KeyError:
        if response.status_code == 429:
            print("Too many requests...")




def make_list(start_day: str, start_year: int, end_day: str, end_year: int):

    year = start_year

    while year <= end_year:
        if year == start_year:

            get_data(year, start_day, "1231")

        elif year == end_year:
            
            get_data(year, "0101", end_day)

        else:
            get_data(year, "0101", "1231")



        check = input("Continue? (Y/N): ")

        if (check == "Y") or (check == "y"):
            year += 1
        elif (check == "N") or (check == "n"):
            break
        else:
            check = input("Y/N? ")


# make_list("1101", 1961, "0831", 1973)

get_data()

# for article in archive:
#     try:
#         print(f'{article["pub_date"]}:\nheadlines: {article["headline"]["main"]}\nkeyword: {article["keywords"][0]["value"]}\n----------')
#     except IndexError:
#         print(f'{article["pub_date"]}:\nheadlines: {article["headline"]["main"]}\nkeyword: N/A\n----------')


