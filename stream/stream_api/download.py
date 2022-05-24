from bs4 import BeautifulSoup
import requests, lxml, json
import urllib.request as req
import os, urllib.request, json # json for pretty output
from serpapi import GoogleSearch
def download_image(query):
    params = {
        "api_key": "995a8345142338b995a9eed1e2c249046fa3d11dfd3c7e9fb54da82772bac435",
        "engine": "google",
        "q": query,
        "tbm": "isch"
        }
    url=[]
    search = GoogleSearch(params)
    results = search.get_dict()

    # print(json.dumps(results['suggested_searches'], indent=2, ensure_ascii=False))
    

    # -----------------------
    # Downloading images

    for index, image in enumerate(results['images_results']):
        if index<4:
            url.append(results['images_results'][0]["original"])
            print(f'Downloading {index} image...')
            
            opener=urllib.request.build_opener()
            opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582')]
            urllib.request.install_opener(opener)

            urllib.request.urlretrieve(image['original'], f'input/original_size_img_{index}.jpg')
        else:
            break
    return url