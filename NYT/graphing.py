import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import json
import os


keywords = {
    'The Cold War': [
        'cold war',
        'communis',
        'ussr',
        'russia',
        'china',
        'stalin',
        'cuba',
        'castro',
        'espionage'


    ],

    'Radiation and Atomic Science': [
        'Atomic',
        'Radiat',
        'Nuclear',
        'Hydrogen Bomb',
        'Missile'
    ],

    'The Vietnam War': [
        'Draft',
        'Viet',
        'Ho Chi Minh',
        'War Crimes',
    ],

    'The Space Race': [
        'Space',
        'Sputnik',
        'aeronaut',
        'astronaut',
        'satellites',


    ],

    'Youth and Counterculture': [
        'Protest ',
        'Protester',
        'Protesting',
        'Youth',
        'Children',
        'Riot',
        'Drug',
        'Police',
        'Generation Gap',
        'Assassinat',
        'Colllege',
        'University',
        'Student',


    ],

    'Civil Rights': [
        'Malcolm X',
        'King, Martin Luther',
        'Negro',
        'Colored People',
        'Civil Rights',
        'segregation'

    ]
}

    

    









# {'Communism': ['Communism', 'Communist', 'Soviet', 'USSR', 'Russia', 'China']},  
# {'Radiation and Atomic Science': ['Radiation', 'Radiate', 'Radioactivity', 'Atom', 'Nuclear', 'Warhead']},
# {'Space': ['Space', 'Moon', 'Aeronaut', 'Astronaut', 'Cosmonaut', 'NASA']}, 
# {'Youth and Counterculture': ['Youth', 'Student', 'Drug', 'Hippie', 'Hipster']},
# {'Protests': ['Activism', 'Activist', 'Protest', 'Riot', 'boycott', 'march']},
# {'Civil Rights': ['civil right', 'malcolm x', 'black', 'negro', 'martin luther king' 'mlk', 'segregation', 'colored', 'NAACP']},
# {'Vietnam': ['Vietnam', 'Vietcong', 'Draft']}





master = pd.read_csv('./NYT/dataframes/master.csv')


# first check the keywords, then check the headline, then check the abstract

def check_occurences(term_list):
    
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
        
        for word in term_list:
            w = word.lower()
            if w in keywords:
                wordcount[date] += 1
                break


    
    return wordcount



if __name__ == '__main__':
    

        
    occurences = {}
    
    for i in keywords: 
        
        occurences[i] = check_occurences(keywords[i])
        
        print(f'finished {i}')

    with open('./NYT/filtered_data/graphing.json', 'w') as jsonFile:
        json.dump(occurences, jsonFile, indent=4)


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


