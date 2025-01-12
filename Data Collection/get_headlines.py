
import sys

sys.path.append("./API")

from API import archive

archive = archive.make_url(11,1961)

def get_headlines(data: list):

    for article in range(len(data)):

        print(f'{data[article]["headline"]["main"]}')
        print(f'{data[article]["snippet"]}')
        print("----------------------")

get_headlines(archive)


def get_headline(data: list, article: int) -> str:
    return f"----------\n{data[article]["headline"]["main"]}\n{data[article]["snippet"]}\n----------"


get_headline(archive, 35)