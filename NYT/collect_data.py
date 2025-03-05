import requests
import json
import os
from Useful.get_months import get_months
from Useful.loop_buffer import validate
from Useful.check_history import check_history

from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent))
from keys import Archive as key

def archive(month: int, year: int):
    url = f'https://api.nytimes.com/svc/archive/v1/{year}/{month}.json?api-key={key}'

    response = requests.get(url)
    status = response.status_code
    if status == 200:
        write(month, year, response.json())
        print(f'Got the Data for {month}/{year}...')

    elif status == 429:
        print('Too Many Entries... Try Again Later...')
    else:
        print('Unkown Error...')
    return status
    
def write(month: int, year: int, jsonFile: dict, root:str = "./NYT/raw_data"):
    
    try:
        os.mkdir(f'{root}')
    except FileExistsError:
        pass
    
    try:
        os.mkdir(f'{root}/{year}')
    except FileExistsError:
        pass
    
    with open(f'{root}/{year}/{month}-{year}.json', 'w') as f:
        json.dump(jsonFile, f) 




if __name__ == '__main__':


    sm, sy = check_history('data')
    
    if sm == None:
        sm = 11
    if sy == None:
        sy = 1961

    timespan = get_months(int(sm) + 1, int(sy), 8, 1973)

    sm = timespan[0][0]
    sy = timespan[0][1]
    print(f'getting data from {sm}/{sy} to 8/1973...')
    
    while True:
        try:
            wait = int(input('Check every _ guesses: '))
            break
        except ValueError:
            pass
    
    if wait > 12: wait = 12
    elif wait < 1: wait = 1

    if wait > 1:
        print(f'Checking every {wait} guesses')
    else:
        print(f'Checking every 1 guess')
    
    i = 0
    
    for date in timespan:
        
        status = archive(date[0], date[1])
        i += 1

        if status == 200:

            if date[0] == 12:

                print(f'----------\nGot the Data for {date[1]}...\n----------')
                
                if validate('Continue?\ny/n: ') == True:
                    pass
                else:
                    print('Ok.\nEnding search...')
                    break
            
            elif wait == i:
                if validate('Continue?\ny/n: ') == True:
                    i = 0
                else:
                    print('Ok.\nEnding search...')
                    break

        elif status == 429:
            break