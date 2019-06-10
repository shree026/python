#! /usr/bin/python3
import os
import datetime
username=input("ENTER NAME--")
userage=int(input("ENTER AGE--"))
currentyear=int(datetime.datetime.now() .year)
year=(95-userage)+currentyear
print(username+"will turn 95 by= ")
print(year)


