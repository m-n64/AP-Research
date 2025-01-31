import os
import json
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from Useful.percent import percent

def fpage_stats(stats: bool = False):

    key_files = []
    extra_files = []
    total_results = 0
    valid_results = 0
    article_keys = {}

    for year in os.listdir('./data'):
        for file in os.listdir(f'./data/{year}'):
            
            fpages = 0

            date = file.split('.')[0]

            with open(f'./data/{year}/{file}', 'r') as jsonFile:
                
                response = json.load(jsonFile)['response']
                data = response['docs']
                results = int(response['meta']['hits'])
                article_keys[file] = []
                for article in data:
                    try:
                        if int(article['print_page']) == 1:
                            fpages += 1
                            article_keys[file].append(data.index(article))
                            
                    except KeyError:
                        pass
            
            valid_results += fpages
            total_results += results
            
            if fpages > 0: key_files.append(file)
            else: extra_files.append(file)
            if stats:
                print(f'---\n{date} -- {fpages}/{results} [{percent(fpages, results, 2)}%]\n---')
            
    
    print(f'TOTAL -- {valid_results}/{total_results} [{percent(valid_results, total_results, 2)}%]')

    total_files = key_files + extra_files
        
    print(f'Usable Files: {percent(len(key_files), len(total_files), 2)}%')
    print(f'Unusable Files: {percent(len(extra_files), len(total_files), 2)}%')
    return article_keys

if __name__ == '__main__':
    fpage_stats(True)
