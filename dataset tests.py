import requests

def make_url(year, month):
    url =  f'https://api.nytimes.com/svc/archive/v1/{year}/{month}.json?api-key=AiqnOCCGOOEoohhGGYEGdnXjraJ3mFRj'
    response = requests.get(url)

    if response.status_code == 200:
        print("we chillin")
    else:
        print(f"No data; {response.status_code}")