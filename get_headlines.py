import get_data

archive = get_data.make_url(11,1961)

def get_headlines(data):

    for article in range(len(data)):

        print(f'{data[article]["headline"]["main"]}')
        print(f'{data[article]["snippet"]}')
        print("----------------------")

get_headlines(archive)


def get_headline(data, article):
    return f"----------\n{data[article]["headline"]["main"]}\n{data[article]["snippet"]}\n----------"


get_headline(archive, 35)