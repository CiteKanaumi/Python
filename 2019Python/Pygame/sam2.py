# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
import sys
import pandas as pd
import random


def read_csv():
    global df
    df = pd.read_csv("list.csv", header=None)

def main():
    for i in range(df.size):
        print(df.iat[i, 0])
    print()
    for i in df[0]:
        print(i)
    



if __name__ == "__main__":
    read_csv()
    main()
    
