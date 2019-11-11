import requests
from bs4 import BeautifulSoup
import pandas as pd

def cooksoup(url, parser='html.parser'):
    #returns a BeautifulSoup for a given url. 
    html = requests.get(url).text
    return BeautifulSoup(html, parser)

def scrap_to_df(search):
    #Given a BeautifulSoup object and an iterable, 
    #returns a DataFrame without blankspaces and applyingline-breaks.
    lst= []
    for e in search:
        lst.append(e.text.strip().split('\n'))
    return pd.DataFrame(lst, index=False)

def main():
    #Cook the soup.
    soup = cooksoup('https://previewsworld.com/Catalog?batch=NOV19&pub=MARVEL%20COMICS')

    #Build a dataframe with previews from Marvel.
    data = scrap_to_df(soup.find_all("div", {"class": "nrgIC"}))
    data.drop([2], axis=1, inplace=True)
    data.set_axis(['Reference','Publisher','Title','Price'], axis=1, inplace=True)
    marvel_previews = data[data['Publisher'] == "MARVEL COMICS"]
    
    #Retrieve orders due date:
    due_disclaimer = soup.find_all("div", {"class" : "ordersDueDisclaimer"})
    due_date = due_disclaimer[0].text.strip()
    print(due_date)
    return marvel_previews.to_csv("../output/marvel_previews.csv")

if __name__=="__main__":
    main()

