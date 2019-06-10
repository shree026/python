#! /usr/bin/python3
import time
from googlesearch import search
web=input("ENTER WHAT YOU WANT TO SEARCH ----")
url=[]
for i in search(web,stop=10):
    print(i)
    time.sleep(1)
url.append(i)
print("result is stored permanently \n")
print(url)

