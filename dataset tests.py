
# requests lets us call other modules
import requests

# month = input("say the month (MM): ")

# year = input("say the year (YYYY): ")


# function requires a spicified date and year.

def make_url(month, year):

    # puts the month and year into completed url and grabs it from NYT
    url =  f'https://api.nytimes.com/svc/archive/v1/{year}/{month}.json?api-key=AiqnOCCGOOEoohhGGYEGdnXjraJ3mFRj'
    response = requests.get(url)


    # checks if we got the data
    if response.status_code == 200:
        
        #creates a dicitonary out of the completed data.
        data = response.json()

        #sends a silly confirmation
        print(f"We chillin... We got the data on {month}/{year}...")
        return data
        # return data

    else:

        #prints status code if we don't have the data
        print(f"No data;\n{response.status_code}")


def get_headlines(month, year):

    headlines = []

    news_data = make_url(month, year)

    for i in range(len(news_data["response"]["docs"])):

        headlines.append(news_data["response"]["docs"][i]["headline"]["main"])

        print(f"{i + 1} --- {headlines[-1]}")
        i += 1

    return headlines

