
def cooksoup(url, parser='html.parser'):
    #returns a BeautifulSoup for a given url. 
    html = requests.get(url).text
    return BeautifulSoup(html, parser)

def scrap_to_df(items):
    #Given a BeautifulSoup object and an iterable, 
    #returns a DataFrame without blankspaces and applyingline-breaks.
    lst= []
    for e in items:
        lst.append(e.text.strip().split('\n'))
    return pd.DataFrame(lst)

def main():
    soup = cooksoup('https://previewsworld.com/Catalog?batch=NOV19&pub=MARVEL%20COMICS')
    return scrap_to_df(soup.find_all("div", {"class": "nrgIC"}))

if __name__=="__main__":
    
    import requests
    from bs4 import BeautifulSoup
    import pandas as pd
    main()

