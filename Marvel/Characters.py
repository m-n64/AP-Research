import requests

url = "https://gateway.marvel.com:443/v1/public/characters?name=Peter Parker&apikey=ad7bdc0c0a8f960f5e30974657f735fe"
response = requests.get(url)


if __name__ == "__main__":
    print(response.json())
