import pandas as pd

def GetFromApi(name, column):
    api = pd.read_csv("./output/api_dataset.csv", index_col=0)
    return api.loc[name,column]