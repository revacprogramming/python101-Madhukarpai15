# Dictionaries

fname=input("Enter the file name: ")
fh=open(fname)
l=[]
d={}
l1=[]

for line in fh:
    if line.startswith("From"):
        x=line.rstrip().split()
        mail=x[1]
        l.append(mail)

size=len(l)
for i in range(0,size):
    count=l.count(l[i])/2
    ele=l[i]
    if ele in d:
        continue
    else:
        d[ele]=count
        l1.append(ele)
    
#dsize=len(d)
l1size=len(l1)

keys=list(d.keys())
vals=list(d.values())

maxkey=keys[vals.index(max(vals))]
maxval=max(vals)

print(maxkey,maxval)




        
