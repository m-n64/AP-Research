import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime


terms = {
    'The Cold War': ['Communism','Communist', 'Soviet', 'USSR', 'Freedom', 'Democracy', 'Cold War', 'Vietnam'],
    'Science and Technology': ['Science', 'Technology', 'Radiation', 'Space', 'Bomb'],
    'Youth and Reform': ['Drug', 'Civil Rights', 'Youth', 'Student', 'Negro', 'Protest', 'Riot', 'Police']
}





master = pd.read_csv('./NYT/dataframes/master.csv')


# first check the keywords, then check the headline, then check the abstract

def check_occurences(item):
    
    occurences = {}
    i = item.lower()

    for index, row in master.iterrows():

        headline = row['headline'].lower()
        keywords = row['keywords'].lower()
        date = datetime.strptime(row['date'], f'%Y-%m-%d').strftime(f'%m/%Y')
        
        if date not in occurences: occurences[date] = 0

        try:
            abstract = row['abstract'].lower()
        except AttributeError:
            pass

        if (i in headline) or (i in keywords) or (i in abstract):
            occurences[date] += 1
    

    return occurences
    
occurences = {}

for genre in terms:
    occurences[genre] = {i : check_occurences(i) for i in terms[genre]}
    print(f'finished {genre}')


print(occurences)