import requests
import json
import os

from get_months import get_months
from loop_buffer import validate


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

sm = input('start month: ')
sy = input('start year: ')


if __name__ == '__main__':
    timespan = get_months(int(sm), int(sy), 8, 1973)
    print(f'getting data from {sm}/{sy} to 8/1973...')
    
    for date in timespan:
        status = archive(date[0], date[1])

        if status == 200:
            if validate('Continue?\ny/n: ') == True:
                pass
            else:
                break
        else:
            break
