#!/usr/bin/env python3 

import sys
import argparse
import subprocess

def recibeConfig():
    parser = argparse.ArgumentParser(description='Saludar a la gente')
    parser.add_argument('--nombre',
                        help='nombre de quien quieres saludar',
                        default="Pepe"
                        )
                        
    args = parser.parse_args()
    print(args)
    return args

def saludameSay(nombre):
    cmd = ['/bin/bash', '-c', "espeak \"{}\"".format(nombre)]
    print(cmd)
    subprocess.Popen(cmd)
    print("Saludado")


def main():
    # Pipeline

    print(sys.argv)
    
    # PASO 1 - Recibir flags y estandarizarlos en un dict
    config = recibeConfig()
    
    # PASO 2 - Saludar
    print("Hola {}".format(config.nombre))
    for _ in range(5):
        saludameSay(config.nombre)

if __name__=="__main__":
    main()