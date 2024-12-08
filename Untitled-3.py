import os
import requests
from urllib.parse import urlparse

def count_clicks(token, short_link):
    vk_linkstats="https://api.vk.ru/method/utils.getLinkStats"
    parameters = { 
        "access_token":token,
        "v":5.199,
        "key":urlparse(short_link).path[1:],
        "interval":"forever",
        "extended":0
    }
    response = requests.get(vk_linkstats, params=parameters)
    response.raise_for_status()
    return response.json()["response"]["stats"][0]["views"]

def shorten_link(token, url):
    vk_shortlink="https://api.vk.ru/method/utils.getShortLink"
    parameters = {
        "access_token":token,
        "v":5.199,
        "url":url
    }
    response = requests.get(vk_shortlink, params=parameters)
    return response.json()["response"]["short_url"]

def is_shorten_link(url, token):
    vk_linkstats="https://api.vk.ru/method/utils.getLinkStats"
    parameters = { 
        "access_token":token,
        "v":5.199,
        "key":urlparse(url).path[1:],
        "interval":"forever",
        "extended":0
    }
    response = requests.get(vk_linkstats, params=parameters)
    response.raise_for_status()
    try:
        response.json()["response"]["stats"][0]["views"]
        return True
    except:
        return False

def main():
    url=input("Введите ссылку: ")
    token=os.environ["TOKEN"]
    if is_shorten_link(url, token):
        try:
            print(count_clicks(token, url))
        except: 
            print("Произошла ошибка")
    else:
        try:
            print(shorten_link(token, url))
        except: 
            print("Произошла ошибка")

if __name__=="__main__":
    main()