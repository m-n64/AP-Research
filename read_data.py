import json
import os

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
            
            print(f'Within {month}, {count} of {len(data)} were front page articles [{round(100*(count/len(data)))}%]')
        except json.JSONDecodeError as e:
            print(f'---------\n{month}\n{e}\n----------')    
