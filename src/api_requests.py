import os
import requests

def MarvelRequest(resource):
    authToken = os.getenv("MARVEL_API_TOKEN")
    if not authToken:
        raise ValueError("NECESITAS UN TOKEN")
    else:
        print("We have a MARVEL token: ", authToken[0:4])
    headers = {
        "Authorization": "token {}".format(authToken)
    }
    url = "http://gateway.marvel.com/v1/public/comics{}".format(resource)
    print("Requesting authorized {}".format(url))
    res = requests.get(url, headers=headers)
    return res

MarvelRequest("?name=Spider-Man")