import pandas as pd
from article_stats import article_data
import json
import os


def compile_data(data):

    try:
        os.mkdir(f'./filtered_data')
    except FileExistsError:
        pass

    for folder in data:
        
        main_data = {'response': []}

        for file in folder.files:
            file.get_data()
            main_data['response'].extend([article.to_dict() for article in file.fpages])

        
        with open(f'./filtered_data/{folder.year}.json', 'w') as jsonFile:
            json.dump(main_data, jsonFile, indent=4)

if __name__ == '__main__':
    
    compile_data(article_data)

    for year in os.listdir('./filtered_data'):

        data = {}
        with open(f'./filtered_data/{year}', 'r') as jsonFile:
            json_data = json.load(jsonFile)['response']

                
        df = pd.json_normalize(json_data)

        print(df)
