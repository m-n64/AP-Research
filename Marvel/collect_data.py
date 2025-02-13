import requests
import datetime
import hashlib
import json
import os
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent))
from keys import Marvel_public as public
from keys import Marvel_private as private

ts = datetime.datetime.now()
hash = hashlib.md5(f'{ts}{private}{public}'.encode()).hexdigest()






def collect_data(entity, name):
    
    response = requests.get(f'http://gateway.marvel.com/v1/public/{entity}?ts={ts}&apikey={public}&hash={hash}&name={name}')
    data = response.json()

    try: os.mkdir(f'./Marvel/raw_data')
    except FileExistsError: pass

    with open(f'./Marvel/raw_data/{entity}.json', 'w', encoding='utf-8') as jsonFile:
        json.dump(data, jsonFile, indent=4)


if __name__ == '__main__':
    collect_data('characters', 'Peter Parker')

    
