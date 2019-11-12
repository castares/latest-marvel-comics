#!/usr/bin/env python3 

import argparse
import subprocess
import os
import pandas as pd

import src.functions as fn

def CharacterPreviews(name="Spider-Man"):
    with open("./output/dataset.csv") as data:
        data = data.readlines()
        for line in data:
            if name in line:
                line = line.split(',')
                print(f"""Name: {line[0]} \nAlignment: {line[1]} \nGender: {line[2]} \nEyeColor: {line[3]} \nRace: {line[4]} \nHairColor: {line[5]} \nHeight: {line[6]} cm. \nWeight: {line[7]} lbs. \nComic Appearances: {line[9]} 
                \nImage: \n{fn.GetFromApi(name,'Images')} \nSeries: \n{fn.GetFromApi(name,'Series')}""")

def FilterAlignment(alignment):
    data = pd.read_csv("./output/dataset.csv")
    data = data[data.loc[:,'Alignment'] == alignment]
    print(data[['Name', 'Gender', 'Race']])

def FilterRace(race):
    data = pd.read_csv("./output/dataset.csv")
    data[data.loc[:,'Race'] == race]
    print(data[['Name', 'Alignment', 'Gender']])

def gender(column):
    dataset = pd.read_csv("./output/dataset.csv")
    print(dataset.groupby(column).Gender.value_counts(normalize=True).round(2))

def lst():
    data = pd.read_csv("./output/dataset.csv")
    print(data["Name"])

def parse():
    parser = argparse.ArgumentParser(description='Provides information about Marvel Characters') #analizador de argumentos
    group = parser.add_mutually_exclusive_group() # grupo mutuamente excluyente (solo una operacion)

    group.add_argument('-n', '--name', help='Get all available info from an specific Marvel character.')
    group.add_argument('-a', '--alignment', help= 'Filter the list of Characters by alignment. Values are: good, neutral or evil')
    group.add_argument('-r', '--race', help= 'Filter the list of Characters by alignment. Most frequent values are: Human, Mutant & Inhuman')
    group.add_argument('-c', '--column', help= 'Filters the given column by gender, returning the ratio of Males and Females for the chosen column')
    group.add_argument('-l', '--list', help= 'Returns a list of all available characters by name')

    return parser.parse_args()

def main():
    
    #Config
    args=parse()
    
    #Functions:
    if args.name:
        CharacterPreviews(args.name)

    if args.alignment:
        FilterAlignment(args.alignment)
    
    if args.race:
        FilterRace(args.race)
    
    if args.column:
        gender(args.column)

    if args.list:
        lst()


if __name__=="__main__":
    main()