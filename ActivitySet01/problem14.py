# Using Web Services
# https://www.py4e.com/lessons/servces


import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

Sum=0
l=[]
while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    #parms = dict()
    uh = urllib.request.urlopen(address, context=ctx)
    data = uh.read()
    tree = ET.fromstring(data)
    results=tree.findall('.//count')
    size=len(results)
    for i in range(0,size):
        Str=ET.tostring(results[i],encoding='utf8',method='xml').rstrip()
        sstr=str(Str)
        x=sstr.split()
        
        y=x[2].split()
        
        y2=str(y[0])
        l.append(y2)
      
    size=len(l)
    for i in range (0,size):
        strnum=re.findall('[0-9]+',l[i])
        Num=int(strnum[1])
        Sum+=Num
    break
print(Sum)