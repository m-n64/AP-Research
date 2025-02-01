from fpage_stats import fpage_stats
import json

def get_values(key: str):

    articles = fpage_stats()
    values = []

    for file in articles:

        with open(f'./data/{file}', 'r') as jsonFile:

            # open the file and load the json in "data"

            data = json.load(jsonFile)['response']['docs']

            # for every saved index
            for index in articles[file]:
                try: 
                    term = data[index][key]

                    if term not in values:
                        values.append(term)
                        print(f'New Value: {term}')
                except KeyError:
                    pass
    return values

if __name__ == '__main__':
    print(get_values('print_section'))
