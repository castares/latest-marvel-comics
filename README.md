# Marvel Characters Database
    
- This tool provides information about Marvel Characters. It combines a local dataset with a series of data extracted from Marvel's API. 
    
- The local dataset includes Name, Alignment, Gender, Eye Color, Race, Height, Weight & the number of appearances in comics for a number of Marvel Characters. 
    
- API's extracted information includes an image of each character stored online, and a list of comic series in which the character appears. 
    
## Local Dataset

- The local dataset used in this project is extracted from Kaggle's [Marvel SuperHeroes](https://www.kaggle.com/dannielr/marvel-superheroes#charcters_stats.csv) dataset.
    
- The full dataset is stored in /input. The selection and cleaning process is executed from /src/clean.py. Resultant dataframe is stored at /output/dataset.csv.

## API Dataset

- API requests are built from the "Name" column on local dataset. New names to local dataset must respect Marvel's API character name. 

- Requests are executed from /src/api_requests.py. Resultant dataframe is stored at /output/api_dataset.csv

## Previews Web Scrapping

- The integration of this process with local and API's datasets is in progress. 

- Scrapping is executed from /src/web_scrapping.py. Results are stored at /output/marvel_previews.csv

## /main.py

- /main.py obtains information from the /output files and returns a standard output depending on the parameters included. Available parameters are referenced at --help.  
