# Regular Expressions
# https://www.py4e.com/lessons/regex

import re

def Input():
  fname=input("Enter the file name: ")
  return fname

def open_f(a):
  fh=open(a)
  return fh
  
Sum=0

def Sum_num(b):
  for line in b:
      strnum=re.findall('[0-9]+',line)
  size=len(strnum)
  for i in range(0,size):
      Sum+=int(strnum[i])

def output():
  print(Sum)

fname=Input()
fh=open_f(fname)
Sum_num(fh)
output()