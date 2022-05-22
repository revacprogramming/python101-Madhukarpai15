# Network Programming
# https://www.py4e.com/lessons/network

#Request Response Cycle
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()

#Scraping HTML Data with BeautifulSoup
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('span')
Sum=0

for tag in tags:
  Sum+=int(tag.contents[0])
    
print(Sum)

#Following Links with BeautifulSoup
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

l=[]
l2=[]
l3=[]
seq=[]
i=0
while i<=6:
    if i==0:
        url = input('Enter - ')
        l3.append(url)
    else:
        url=l3[i]
        
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    for tag in tags:
        x=tag.get('href', None)
        y=tag.contents[0]
        l.append(x)
        l2.append(y)
    l3.append(l[17])
    seq.append(l2[17])
    l.clear()
    l2.clear()
    i+=1

print('Last name: ',seq[i-1])
