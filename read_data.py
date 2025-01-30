import json
import os
import math



for year in os.listdir('./data'):

    for month in os.listdir(f'./data/{year}'):

        count = 0
        try:
            with open(f'./data/{year}/{month}') as jsonFile:
                response = json.load(jsonFile)
                data = response['response']['docs']
                for article in data:
                    try: 
                        if (int(article['print_page']) == 1) or (article['print_section'] == 'A'):
                            count += 1
                    except KeyError:
                        pass
            
        except json.JSONDecodeError as e:
            print(f'---------\n{month}\n{e}\n----------')


def calculate_stats():
    pass
    # print each year's % of fps
    # print total range's % of fps
    # print all usable years
    # print all UNUSABLE years