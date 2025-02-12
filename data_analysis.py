import pandas as pd
from article_stats import article_data
import json
import os


def compile_data(data):

    try:
        os.mkdir(f'./filtered_data')
    except FileExistsError:
        pass
    
    total_keywords = {}

    for folder in data:
        
        main_data = {'response': []}

        for file in folder.files:
            file.get_data()
            main_data['response'].extend([article.to_dict() for article in file.fpages])
            
            keywords = file.get_keywords()

            for word in keywords:
                if word in total_keywords:
                    if keywords[word]['name'] in total_keywords[word]['name']:
                        total_keywords[word]['name'].extend(keywords[word]['name'])
                        print(f'Gave the {"/".join(total_keywords[word]['name'])} "{word}" {keywords[word]['points']} more points')

                    total_keywords[word]['points'] += keywords[word]['points']
                else:
                    total_keywords[word] = keywords[word]
                    print(f'Added the {"/".join(total_keywords[word]['name'])}, "{word}" to the dictionary with {keywords[word]['points']} points')



        

        with open(f'./filtered_data/{folder.year}.json', 'w') as jsonFile:
            json.dump(main_data, jsonFile, indent=4)
            print('finished compiling data')
        
    with open(f'./filetered_data/KEYWORDS.json', 'w') as jsonFile:
        json.dump(total_keywords)
        print('finished adding keywords')    

if __name__ == '__main__':
    
    compile_data(article_data)

    for year in os.listdir('./filtered_data'):

        data = {}
        with open(f'./filtered_data/{year}', 'r') as jsonFile:
            json_data = json.load(jsonFile)['response']

                
        df = pd.json_normalize(json_data)

        print(df)
