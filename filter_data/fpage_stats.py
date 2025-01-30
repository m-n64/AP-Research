import os
import json

def fpage_stats():

    key_files = []
    extra_files = []
    total_results = 0
    valid_results = 0

    for year in os.listdir('.data'):
        for file in os.listdir(f'./data/{year}'):
            
            fpages = 0

            date = file.split('.')[0]
            usable = False

            with open(f'./data/{year}{file}', 'r') as jsonFile:
                
                response = json.load(jsonFile)['response']
                data = response['docs']
                results = int(response['meta']['hits'])

                for article in data:
                    if int(article['print_page']) == 1:
                        fpages += 1
                        usable = True
            
            valid_results += fpages
            total_results += results
            
            if usable: key_files.append(file)
            else: extra_files.append(file)

            print(f'---\n{date} -- {fpages}/{results} [{percent(fpages, results, 2)}%]\n---')

    print('**********')
    print(f'TOTAL -- {valid_results}/{total_results}')
    print('**********')

    total_files = key_files + extra_files

    print(f'Usable Files: {percent(len(key_files), len(total_files), 2)}%')
    print(key_files)
    print(f'Unusable File: {len(extra_files, len(total_files), 2)}%')
    print(extra_files)


if __name__ == '__main__':
    fpage_stats()
