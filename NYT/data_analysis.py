import pandas as pd
from article_stats import article_data
import json
import os



def compile_data(data):

    try:
        os.mkdir(f'./NYT/filtered_data')
    except FileExistsError:
        pass
    

    for folder in data:
        
        main_data = {'response': []}

        for file in folder.files:
            file.get_data()
            main_data['response'].extend([article.to_dict() for article in file.fpages])
            
        with open(f'./NYT/filtered_data/{folder.year}.json', 'w') as jsonFile:
            json.dump(main_data, jsonFile, indent=4)
            print('finished compiling data')
        


def compile_keywords(data):

    try:
        os.mkdir(f'./NYT/sample_data')
    except FileExistsError:
        pass

    try:
        os.mkdir(f'./NYT/sample_data/keywords')
    except FileExistsError:
        pass

    for folder in data:
        for file in folder.files:
            file.get_data()
            temp_keywords = file.get_keywords()

            for keyword in temp_keywords:
                for topic in temp_keywords[keyword]['name']:
                    try: 
                        with open(f'./NYT/sample_data/keywords/{topic}.json', 'r') as jsonFile:
                            total_keywords = json.load(jsonFile)
                    except json.JSONDecodeError:
                        total_keywords = {}

                    if keyword not in total_keywords: total_keywords[keyword] = temp_keywords[keyword]['points']
                    else: total_keywords[keyword] += temp_keywords[keyword]['points']

                    with open(f'./NYT/sample_data/keywords/{topic}.json', 'w') as jsonFile:
                        json.dump(total_keywords, jsonFile, indent=4)


def create_df():

    main_df = pd.DataFrame([])
    for file in os.listdir(f'./NYT/sample_data/filtered_data'):
        try:
            with open(f'./NYT/sample_data/filtered_data/{file}', 'r') as jsonFile:
                data = json.load(jsonFile)['response']

                if main_df.empty:
                    main_df = format_data(data)
                else:
                    new_df = format_data(data)
                    main_df = pd.concat([main_df, new_df])
        except KeyError:
            pass
    return main_df





def format_data(json_data):

    df = pd.json_normalize(json_data)
    formated_df = df.drop('print_section', axis='columns')
    formated_df['date'] = pd.to_datetime(formated_df['date'])
    formated_df.sort_values('date')

    for row in formated_df.index:
  
        headline = formated_df.loc[row, 'headline']

        if 'No Title' in headline:
            formated_df = formated_df.drop(row, axis='index')

    return formated_df

def create_kw(json_data):
    headers = list(json_data.keys())
    points = {'points': [json_data[word] for word in json_data]}

    df = pd.DataFrame(points, index=headers).sort_values('points', ascending=False)

    for row in df.index:
        if row == 'MISCELLANEOUS SECTION':
            df = df.drop(row, axis='index')

    return df

if __name__ == '__main__':
    compile_data(article_data)
    compile_keywords(article_data)
    try: os.mkdir('./NYT/dataframes')
    except FileExistsError: pass
    try: os.mkdir('./NYT/dataframes/keywords')
    except FileExistsError: pass

    master_df = create_df()
    master_df.to_csv('./NYT/dataframes/master.csv', encoding='utf-8', index=False, header= True)

    for file in os.listdir(f'./NYT/sample_data/keywords'):
        with open(f'./NYT/sample_data/keywords/{file}') as jsonFile:
            keyword_data = json.load(jsonFile)
            kw_df = create_kw(keyword_data)
        
        kw_df.to_csv(f'./NYT/dataframes/keywords/{file.split('.')[0]}.csv', encoding='utf-8', header= True)

            

        






            


