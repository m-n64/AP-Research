import requests
import json
import os

from Useful.get_months import get_months
from Useful.loop_buffer import validate
from Useful.check_history import check_history

def archive(month: int, year: int):
    url = f'https://api.nytimes.com/svc/archive/v1/{year}/{month}.json?api-key=AiqnOCCGOOEoohhGGYEGdnXjraJ3mFRj'

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
    
def write(month: int, year: int, jsonFile: dict):
    try:
        os.mkdir(f'data/{year}')
    except FileExistsError:
        pass
    
    with open(f'data/{year}/{month}-{year}.json', 'w') as f:
        json.dump(jsonFile, f) 


if __name__ == '__main__':


    sm, sy = check_history('data')
    
    if sm == None:
        sm = input('start month: ')
    if sy == None:
        sy = input('start year: ')

    timespan = get_months(int(sm) + 1, int(sy), 8, 1973)
    print(f'getting data from {int(sm) + 1}/{sy} to 8/1973...')
    
    for date in timespan:
        status = archive(date[0], date[1])
        if (status == 200) and (date[0] == 12):

            print(f'----------\nGot the Data for {date[1]}...\n----------')
            
            if validate('Continue?\ny/n: ') == True:
                pass
            else:
                break

        elif (status == 429):
            break