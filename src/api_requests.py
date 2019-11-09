import os
import requests
import hashlib
from dotenv import load_dotenv
import time

load_dotenv()

#keys
public_key = os.getenv("MARVEL_API_PUBLIC_KEY")
private_key = os.getenv("MARVEL_API_PRIVATE_KEY")

print(public_key, private_key)

#ts
ts = str(time.time())

def hash(ts, public_key, private_key):
    m_hash = hashlib.md5()
    ts_str_byte = bytes(ts, 'utf-8')
    private_key_byte = bytes(private_key, 'utf-8')
    public_key_byte = bytes(public_key, 'utf-8')
    m_hash.update(ts_str_byte + private_key_byte + public_key_byte)
    return str(m_hash.hexdigest())

def MarvelRequest(resource):
    print(ts)
    print(public_key)
    url = "http://gateway.marvel.com/v1/public{}".format(resource)
    payload = {
        'ts': ts, 
        'apikey': public_key, 
        'hash': hash(ts, public_key, private_key)
    }
    r = requests.get(url, params=payload)
    print(r.url)
    return r

answer = MarvelRequest("/characters?name=Spider-Man").json()

print(answer)