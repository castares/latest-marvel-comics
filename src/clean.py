import pandas as pd

def main():
    #1st DataFrame: Characters Info.
    dataset = pd.read_csv("../input/marvel_characters_info.csv")
    dataset.drop(['ID','SkinColor', 'Publisher'], axis=1, inplace=True)
    dataset.drop_duplicates(subset='Name', keep='first', inplace=True)
    #Only 35 rows (of a total of 388) have a value in skin color. 
    #Since this column is not necessary for the objectives of this work, we are going to remove it. 
    #Publisher column is no longer necessary, since later we keep only the rows matching Marvel Characters
    #The ID on this column will be replaced by the one from the Marvel API. We drop this one.
    #Some rows were duplicated, with slight differences on some values. We remove duplicates keeping the first unique value.

    #2nd DataFrame: Characters comics:
    df2 = pd.read_csv("../input/charactersToComics.csv")
    df2 = df2.groupby(['characterID']).count()
    df2.rename({'comicID': 'comics_count'}, axis=1, inplace=True)
    #This dataframe contains only Marvel's API character's IDs and comicsID. 
    #We are grouping the Character IDs to know on how many comics they appear.

    #3rd DataFrame: Characters names:
    df3 = pd.read_csv("../input/characters.csv")
    comics_count = df3.merge(df2,on='characterID')
    comics_count.rename({'name': 'Name'}, axis=1, inplace=True)
    #This dataframe allow us to link the count of comics to the character's name, and therefore to the 1st dataframe.
    #This merge removes all non-Marvel Characters.
    #Finally, we merge both datasets and export the result to a csv.
    dataset = dataset.merge(comics_count, on='Name')
    dataset.to_csv("../output/dataset.csv", index=False)

if __name__=="__main__":
    main()