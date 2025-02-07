import os
import sys
import json

from collect_data import archive
from filter_data.fpage_stats import fpage_stats
from Useful.dynamic_loading import load

from pathlib import Path


#iterate through each subfolder


        

    
def delete_articles(file, keys):
            
    data = file['response']['docs']

    data = [data[article] for article in keys]

        
    
        

if __name__ == "__main__":

    key_info = fpage_stats()
    #iterate through files
    for file in key_info:

        year = file.split('/')[0]
        month = file.split('/')[1].split('-')[0]
        date = file.split('/')[1].split('.')[0]

        with open(f'./data/{file}', 'r') as jsonFile:
            raw = json.load(jsonFile)
        # try:
        with open(f'./data/{file}', 'w') as jsonFile:
            
            print(raw)

            delete_articles(raw, key_info[file]) 
            
            json.dump(raw, jsonFile)

            load(file, key_info, True, f'[{date}] Cutting Data...', True)
        # except Exception as e:
        #     print(e)

        #     year = file.split('/')[0]
        #     month = file.split('/')[1].split('-')[0]
        #     archive(month, year)
        #     break



    