import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import json
import os


keywords = [
    
    {'Communism': ['Communism', 'Communist', 'Soviet', 'USSR']},  
    {'Radiation and Atomic Science': ['Radiation', 'Radiate', 'Radioactivity', 'Atom', 'Nuclear', 'Warhead']},
    {'Space': ['Space', 'Moon', 'Aeronaut', 'Astronaut', 'Cosmonaut', 'NASA']}, 
    {'Youth & Counterculture': ['Youth', 'Student', 'Drug', 'Activism', 'Activist', 'Protest', 'Riot']},
    'Vietnam'

]





master = pd.read_csv('./NYT/dataframes/master.csv')


# first check the keywords, then check the headline, then check the abstract

def check_occurences(word):
    
    wordcount = {}
            
    for index, row in master.iterrows():

        headline = row['headline'].lower()
        keywords = row['keywords'].lower()
        try:
            abstract = row['abstract'].lower()
        except AttributeError:
            pass

        date = datetime.strptime(row['date'], f'%Y-%m-%d').strftime(f'%m/%Y')

        if date not in wordcount: wordcount[date] = 0

        if type(word) == str:
            
            w = word.lower()
            if (w in keywords) or (w in headline) or (w in abstract):
                wordcount[date] += 1

            
        elif type(word) == dict:

            for term in word[list(word.keys())[0]]:
                t = term.lower()
                if (t in keywords) or (t in headline) or (t in abstract):
                    wordcount[date] += 1

    
    return wordcount



if __name__ == '__main__':
    
    if os.path.exists('./NYT/filtered_data/graphing.json') == False:
    
        occurences = {}
        
        for i in keywords: 
            if type(i) == dict:
                occurences[list(i.keys())[0]] = check_occurences(i)
            else:
                occurences[i] = check_occurences(i)
            
            print(f'finished {i}')

        with open('./NYT/filtered_data/graphing.json', 'w') as jsonFile:
            json.dump(occurences, jsonFile, indent=4)
    

    if os.path.exists('./NYT/dataframes/graphing.csv') == False:

        with open('./NYT/filtered_data/graphing.json', 'r') as jsonFile:
            occurences = json.load(jsonFile)

        dfs = {i: pd.json_normalize(occurences[i]).transpose() for i in occurences}

        master_df = pd.DataFrame([])

        for i in dfs:


            dfs[i] = dfs[i].reset_index()
            dfs[i].columns = ['Date', i]
            dfs[i]['Date'] = pd.to_datetime(dfs[i]['Date'])

            try:
                master_df = pd.merge(master_df, dfs[i], on='Date', how='outer')
            except KeyError:
                master_df = dfs[i]
            
            
        master_df = master_df.drop(0, axis='index')
        print(master_df.head())

        master_df.to_csv('./NYT/dataframes/graphing.csv')


