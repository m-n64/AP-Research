
import requests
from article_classes import Article


class Month:

    def __init__(self, month, year):
        self.month = month
        self.year = year
        self.days = self.check_days()
        self.url = f'https://api.nytimes.com/svc/search/v2/articlesearch.json?begin_date={year}{month}01&end_date={year}{month}{self.days}&fq=print_page:1 AND (print_section:("A", "1") OR (!_exists_:print_section))&api-key=AiqnOCCGOOEoohhGGYEGdnXjraJ3mFRj'
        self.date = f'{self.month}/{self.year}'
        self.results = 0
        self.article_list = "N/a"


    def check_days(self):
        odd_months = [1, 3, 5, 7, 8, 10, 12]

        if self.month in odd_months:
            return 31
        elif self.month == 2:
            if self.year % 4 == 0:
                return 29
            else:
                return 28
        else:
            return 30

    def rundown(self):
        print(f'{self.date}:')
        print(f'Link: {self.url}')
        print(f'Results: {self.results}')
        print("----")
        print(f'Article List:')
        print(self.article_list)



    def search_articles(self):


        #calls the url from NYT Database
        response = requests.get(self.url)
        
        # prints the confirmation response
        print(response)
        
        # "200" means everything went smoothly and we can progress with data analysis
        if response.status_code == 200:

            #define how many results were found
            self.results = response.json()["response"]["meta"]["hits"]
            print(self.results)

            # celebrate the good news...
            print(f'We did it... We got the data from {self.month}/1/{self.year}, to {self.month}/{self.days}/{self.year}...')
            print("------------------")
            # print(response.json()["response"]["docs"])
            self.data = response.json()["response"]["docs"]
        

        # "400 means it was a bad request, like a typo or smth"
        elif response.status_code == 400:
            # say it was some sort of error
            print("Bad request... Retrying...")
            
            # check if the type was because the month was single digit instead of double
            if (type(self.month) == int) and self.month < 10:
                
                self.month = "0" + str(self.month)
                self.search_articles()
            
            # tell dev they're outta luck if its not that type of typo
            else:
                print(f"Undefined Error...\nmonth:{self.month}\nurl:{self.url}")

        #429 means we hit the request limit, either for the minute or the day (likely the former) and we need to wait.
        elif response.status_code == 429:
            print("Too many requests...")

    def get_data(self):

        self.article_list = []

        for article in self.data:
            info = Article(self.month, self.year)
            info.headline = article["headline"]["main"]
            info.published = article["pub_date"]
            info.abstract = article["abstract"]
            


        self.article_list.append(info)
        
    
