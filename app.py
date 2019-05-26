import requests, json
import urllib.request
from requests.auth import HTTPBasicAuth
from PIL import Image
from InstagramAPI import InstagramAPI

try:
    file = open('credentials.json', 'r')
    data = file.read()
    credentials = json.loads(data)

    url = credentials['reddit']['url']

    querystring = {"sort":"old", "limit": 100}

    payload = ""
    headers = {
        'User-Agent': credentials['reddit']['user-agent'],
        }

    reddit_username = credentials['reddit']['username']
    reddit_password = credentials['reddit']['password']
    instagram_username = credentials['instagram']['username']
    instagram_password = credentials['instagram']['password']
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring, auth=HTTPBasicAuth(reddit_username, reddit_password))

    dict = json.loads(response.text)

    data = dict['data']['children']

    posts = dict['data']['children']
    InstagramAPI = InstagramAPI(instagram_username, instagram_password)
    InstagramAPI.login()
    for post in posts:
        if not post['data']['score']:
            continue

        if post['data']['is_video']:
            continue

        if "jpg" not in post['data']['url']:
            continue

        if post['data']['score'] < 39:
            continue

        print(post['data']['url'])
        print(post['data']['score'])

        phrase_file = open('caption.txt', 'r')
        phrase = phrase_file.read()
        hashtags_file = open('hashtags.txt', 'r')
        hashtags = hashtags_file.read()
        caption = phrase + hashtags
        image = "images/" + post['data']['id'] + ".jpg"
        urllib.request.urlretrieve(post['data']['url'], image)
        img = Image.open(image)
        new_width = 1080
        new_height = 1350
        width, height = img.size
        img = img.resize((new_width, new_height), Image.ANTIALIAS)
        print(caption + "\n")
        img.show()
        answer = input("Do you want to post this?\n")
        if "n" in answer:
            img.close()
            continue
        elif "y" in answer:
            # Do something and post on instagram
            posted = InstagramAPI.uploadPhoto(image, caption=caption)

        if posted:
            break
except Exception as e:
    print(e)

