# Regular Expressions
# https://www.py4e.com/lessons/regex

import re

fname=input("Enter the file name: ")
fh=open(fname)
Sum=0

for line in fh:
    strnum=re.findall('[0-9]+',line)
    size=len(strnum)
    for i in range(0,size):
        Sum+=int(strnum[i])

print(Sum)