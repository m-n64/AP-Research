from fpage_stats import fpage_stats
import json

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from Useful.dynamic_loading import load


def get_values(key: str):

    fpages = fpage_stats()
    values = {
        "results": 0,
        "files": {}
        }


    for file in fpages:

        with open(f'./data/{file}', 'r') as jsonFile:

            # open the file and load the json in "data"

            data = json.load(jsonFile)['response']['docs']

            values['files'][file] = []

            # for every saved article
            for article in fpages[file]:
                
                try: 
                    
                    #get the key fron the dictionary and save the term.
                    term = data[article][key]

                    #keywords is the only known outlier at the moment, so if the key is keywords, go through the list.
                    if key == 'keywords':

                        for item in data[article][key]:

                            term = item['value']
                            
                            if term not in values['files'][file]:
                                values['files'][file].append(term)
                                values['results'] += 1

                    #if the key is LITERALLY ANYTHING ELSE...
                    else:
                        if term not in values['files'][file]:
                            values['files'][file].append(term)
                            values['results'] += 1
                #if the key isn't there, skip
                except KeyError:
                    pass
                
                #progress every article
        load(list(fpages.keys()).index(file), len(fpages), f"Adding {key}")

    return values

def state_values(fpages: dict):

    while (year := int(input(f"State a year from 1961 to 1973\n"))) not in range(1961, 1973):
        year = int(input('Try again...(YYYY)\n'))
    
    if year == 1961:
        months = range(11,13)
    elif year == 1973:
        months = range(1, 9)
    else:
        months = range(1, 13)

    while (month := int(input(f'State a month from {months[0]} to {months[-1]}\n'))) not in months:
        month = int(input('Try again...(MM)\n'))

    file = f'{year}/{month}-{year}.json'

    print(f'{month}/{year}:')
    print('<==========>')
    print(f'{fpages['files'][file]}')

    while ((validate := input('Continue? (y/n): ')) != 'Y') or (validate != 'N'):
        validate = input('y/n: ')
        
    if validate == 'y':
        state_values(fpages)




if __name__ == '__main__':

    my_data = get_values('keywords')
    print(f'\n{my_data['results']}')
    if my_data['results'] > 100:
        print('Yikes... :|')
    else:
        print('light work, no reaction B)')

    state_values(my_data)

    