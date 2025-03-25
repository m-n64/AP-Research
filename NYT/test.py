import pandas as pd


df = pd.read_csv('NYT/dataframes/master.csv')

keywords = df['keywords']



for r in range(len(keywords)):

    terms = keywords[r].split("', '")

    for i in range(len(terms)):
        if i == 0: terms[i] = terms[i][2:]
        if i == len(terms) - 1: terms[i] = terms[i][:-2]
        
    # if r == 3: break
    keywords[r] = '||'.join(terms)    
    if keywords[r] == '': keywords[r] == 'N/a'



df.to_csv('NYT/dataframes/master.csv')
