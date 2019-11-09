import os
import requests
import hashlib
from dotenv import load_dotenv
import time

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
    url = "http://gateway.marvel.com/v1/public{}".format(resource)
    payload = {
        'ts': ts, 
        'apikey': public_key, 
        'hash': hash(ts, public_key, private_key)
    }
    r = requests.get(url, params=payload)
    print(r.url)
    return r



def main():
    answer = MarvelRequest("/characters?").json()
    data = answer['data']['results']
    names = []
    images = []
    series = []    
    for e in data:
        names.append(e['name'])
        images.append(e['thumbnail'])
        series.append(e['series'])


if __name__=="__main__":
    main()