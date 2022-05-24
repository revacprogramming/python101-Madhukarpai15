#Strings

Str="X-DSPAM-Confidence:    0.8475"

def find():
    pos=Str.find(':')
    strnum=Str[pos+1:].lstrip()
    num=float(strnum)
    return num

def output(c):
    print(c)
    
num=find()
output(num)
