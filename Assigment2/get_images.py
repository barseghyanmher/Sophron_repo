import json
import requests
import os
import threading

"""
Opening a "web_images" folder for adding imiges
"""
try:
    os.mkdir("web_images")
except FileExistsError:
    print("web_images folder already exists, skipping")

with open('task_urls.json') as file:
    urls = json.load(file)


def download(url, name):
    """
    download function for downloading
    images from urls and give names
    """

    try:
        response = requests.get(url)
    except requests.exceptions.ConnectionError:
        print("Connection is missing pleas check connection")

    if response.status_code == 200:
        with open("web_images/" + "image" + name + ".png", "wb") as file:
            file.write(response.content)


runs = []
for i, url in enumerate(urls["items"]):
    x = threading.Thread(target=download, args=(url["url"], str(i)))
    x.start()
    runs.append(x)

for x in runs:
    x.join()

# if web_images folder is empty delete it
try:
    os.rmdir("web_images")
except:
    pass
