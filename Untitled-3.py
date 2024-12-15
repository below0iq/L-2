import os
import requests
from urllib.parse import urlparse


def count_clicks(token, short_link):
    url = "https://api.vk.ru/method/utils.getLinkStats"
    parameters = { 
        "access_token": token,
        "v": 5.199,
        "key": urlparse(short_link).path[1:],
        "interval": "forever",
        "extended": 0
    }
    response = requests.get(url, params=parameters)
    response.raise_for_status()
    return response.json()["response"]["stats"]


def shorten_link(token, url):
    url = "https://api.vk.ru/method/utils.getShortLink"
    parameters = {
        "access_token": token,
        "v": 5.199,
        "url": url
    }
    response = requests.get(url, params=parameters)
    response.raise_for_status()
    return response.json()["response"]["short_url"]


def is_shorten_link(url, token):
    url = "https://api.vk.ru/method/utils.getLinkStats"
    parameters = { 
        "access_token": token,
        "v": 5.199,
        "key": urlparse(url).path[1:],
        "interval": "forever",
        "extended": 0
    }
    response = requests.get(url, params=parameters)
    response.raise_for_status()
    try:
        response.json()["response"]["stats"]
        return True
    except:
        return False


def main():
    url = input("Введите ссылку: ")
    token = os.environ["VK_SERVICE_TOKEN"]
    if is_shorten_link(url, token):
        try:
            if len(count_clicks(token, url)) == 0:
                print("По ссылке еще не переходили")
            elif count_clicks(token, url)[0]["views"] > 0:
                print(f"По ссылке перешли {count_clicks(token, url)[0]["views"]} раз")
        except:
            print("Неправильный ввод ссылки")
    else:
        try:
            print(shorten_link(token, url))
        except KeyError: 
            print("Неправильный ввод ссылки")


if __name__ == "__main__":
    main()
