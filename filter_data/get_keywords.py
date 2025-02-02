from fpage_stats import fpage_stats
import json

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from Useful.dynamic_loading import load


def get_values(key: str):

    files = fpage_stats()
    values = []

    for date in files:

        with open(f'./data/{date}', 'r') as jsonFile:

            # open the file and load the json in "data"

            data = json.load(jsonFile)['response']['docs']

            # for every saved article
            for article in files[date]:
                try: 
                    
                    #get the key fron the dictionary and save the term.
                    term = data[article][key]

                    #keywords is the only known outlier at the moment, so if the key is keywords, go through the list.
                    if key == 'keywords':

                        for item in data[article][key]:

                            term = item['value']
                            
                            if term not in values:
                                values.append(term)

                    #if the key is LITERALLY ANYTHING ELSE...
                    else:
                        if term not in values:
                                values.append(term)
                #if the key isn't there, skip
                except KeyError:
                    pass
                
                #progress every article
        load(list(files.keys()).index(date), len(files), f"Adding {key}")

    return values

if __name__ == '__main__':

    my_data = get_values('keywords')
    print(my_data)
    print('----------')
    print(len(my_data))
    if len(my_data) > 100:
        print('Yikes... :|')
    else:
        print('light work, no reactin B)')
