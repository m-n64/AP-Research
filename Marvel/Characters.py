import requests

url = "https://gateway.marvel.com:443/v1/public/characters?name=Peter%20Parker&apikey=ad7bdc0c0a8f960f5e30974657f735fe&hash="
response = requests.get(url, verify=False)


if __name__ == "__main__":
    print(response.status_code)
