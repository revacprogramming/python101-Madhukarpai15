#Web Services JSON


import urllib.request, urllib.parse, urllib.error
#import xml.etree.ElementTree as ET
import ssl
import json


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


Sum=0

def Json(a):
    while True:
        address = input('Enter location: ')
        if len(address) < 1: break
    
        uh = urllib.request.urlopen(address, context=ctx)
        data=uh.read()
        #print(data)
        info=json.loads(data)
        user_count=len(info)
        for i in range (0,user_count):
            ele=info['comments']
            size=len(ele)
            for i in range (0,size):
                sub=ele[i]
                a+=sub['count']
            return a
            break

def output(c):
    print(c)
    
result=Json(Sum)
output(result)