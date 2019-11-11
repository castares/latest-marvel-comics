import os
import requests
import hashlib
from dotenv import load_dotenv
import time
import pandas as pd
import re

load_dotenv()

#MARVEL API KEYS
public_key = os.getenv("MARVEL_API_PUBLIC_KEY")
private_key = os.getenv("MARVEL_API_PRIVATE_KEY")

#timestamp
ts = str(time.time())

def hash(ts, public_key, private_key):
    #this function builds a hash of the 3 parameters required by Marvel to access their API.
    m_hash = hashlib.md5()
    ts_str_byte = bytes(ts, 'utf-8')
    private_key_byte = bytes(private_key, 'utf-8')
    public_key_byte = bytes(public_key, 'utf-8')
    m_hash.update(ts_str_byte + private_key_byte + public_key_byte)
    return str(m_hash.hexdigest())

def MarvelRequest(resource):
    #Given a resource, this function makes a call to the Marvel API
    url = "http://gateway.marvel.com/v1/public/characters?name={}".format(resource)
    payload = {
        'ts': ts, 
        'apikey': public_key, 
        'hash': hash(ts, public_key, private_key)
    }
    r = requests.get(url, params=payload)
    print(r.url)
    return r

def RequestLoop(dataset):
    names = []
    images = []
    series = []
    for e in dataset["Name"]:
        answer = MarvelRequest(e).json()
        print("Request for {} completed".format(e))
        data = answer['data']['results'][0]
        names.append(data['name'])
        #completing the path of the images: https://developer.marvel.com/documentation/images
        images.append(data['thumbnail']['path']+"/portrait_fantastic.jpg")
        #keeping only the name of the series.
        series.append([e['name'] for e in data['series']['items']])
        api_dataframe = pd.DataFrame({'Name':names, 'Images':images,'Series':series}, index=False)
    return api_dataframe


def main():
    #Getting Character's data.
    dataset = pd.read_csv("../output/dataset.csv")
    data_output = RequestLoop(dataset)
    data_output.to_csv("../output/api_dataset.csv")
    return "Done" #Filtering out name, images and series.



if __name__=="__main__":
    main()