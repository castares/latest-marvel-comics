import pandas as pd

def GetFromApi(name, column):
    api = pd.read_csv("./output/api_dataset.csv", index_col=1)
    return api.loc[name,column]