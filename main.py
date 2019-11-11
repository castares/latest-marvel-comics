#!/usr/bin/env python3 

import argparse
import subprocess
import os
import pandas as pd

def CharacterPreviews(name="Spider-Man"):
    with open("./output/dataset.csv") as data:
        data = data.readlines()
        for line in data:
            if name in line:
                line = line.split(',')
                print(f"Name: {line[0]}\nAlignment: {line[1]} \nGender: {line[2]} \nEyeColor: {line[3]} \nRace: {line[4]} \nHairColor: {line[5]} \nHeight: {line[6]} cm. \nWeight: {line[7]} lbs. \nComic Appearances: {line[9]}")

def FilterAlignment(alignment):
    data = pd.read_csv("./output/dataset.csv")
    data = data[data.loc[:,'Alignment'] == alignment]
    print(data[['Name', 'Gender', 'Race']])

def FilterRace(race):
    data = pd.read_csv("./output/dataset.csv")
    data[data.loc[:,'Race'] == race]
    print(data[['Name', 'Alignment', 'Gender']])

def parse():
    parser = argparse.ArgumentParser(description='Check issues available on previews for Marvel Characters') #analizador de argumentos
    group = parser.add_mutually_exclusive_group() # grupo mutuamente excluyente (solo una operacion)

    group.add_argument('-n', '--name', help='Get all available info from an specific Marvel character.')
    group.add_argument('-a', '--alignment', help= 'Filter the list of Characters by alignment')
    group.add_argument('-r', '--race', help= 'Filter the list of Characters by alignment')

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

if __name__=="__main__":
    main()