import os
import json
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from Useful.dynamic_loading import load
from Useful.percent import percent

def fpage_stats(stats: bool = False):
    key_files = []
    extra_files = []
    total_results = 0
    valid_results = 0
    article_keys = {}
    total_files = []

    #get the total amount of files, for loading purposes
    for year in os.listdir('./data'):
        for file in os.listdir(f'./data/{year}'):
            total_files.append(file)

    #for each folder within the data...
    for year in (folders := os.listdir('./data')):

        #for each file within each subfolder
        for file in os.listdir(f'./data/{year}'):
            
            #set the front pages per file to 0
            fpages = 0

            #define the date based on the file name
            date = file.split('.')[0]

            #open the file
            with open(f'./data/{year}/{file}', 'r') as jsonFile:
                
                #get the article data
                response = json.load(jsonFile)['response']
                data = response['docs']
                
                #get the total results
                results = int(response['meta']['hits'])
                total_results += results

                # for each article within the list, add its identifier to the dictionary, according to it's file loction
                article_keys[f'{year}/{file}'] = []
                for article in data:
                    try:
                        if int(article['print_page']) == 1:
                            fpages += 1
                            article_keys[f'{year}/{file}'].append(data.index(article))

                    #if there isn't a print page mentioned, skip
                    except KeyError:
                        pass
            
            #add the number of front pages to the list of "valid results" 
            valid_results += fpages
            
            #if the file has at least 1 front page, state it is an important file
            if fpages > 0: key_files.append(file)
            else: extra_files.append(file)

            #if statistics should be displayed, display them
            if stats:
                print(f'{date} -- {fpages}/{results} [{percent(fpages, results, 2)}%]')
                print('----------')
            #otherwise, just share a generic loading message.
            else:
                load(folders.index(year), len(folders), f'[{year}] Collecting Data')
    
    print(f'TOTAL USABLE ARTICLES -- {valid_results:,}/{total_results:,} [{percent(valid_results, total_results, 2)}%]')

    print(f'Usable Files: {percent(len(key_files), len(total_files), 2)}%')
    print(f'Unusable Files: {percent(len(extra_files), len(total_files), 2)}%')
    return article_keys

if __name__ == '__main__':
    fpage_stats()
