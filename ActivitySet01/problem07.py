# Strings

def extract(a):
    l=["0","1","2","3","4","5","6","7","8","9"]
    for i in range(0,size):
        if a[i] in l:
            pos=a.find(a[i])
            Str2=a[pos:size]
            num=float(Str2)
            return num

Str="X-DSPAM-Confidence:    0.8475"
size=len(Str)
Num=extract(Str)
print(Num)
