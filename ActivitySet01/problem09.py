# Lists

fname=input("Enter the file name: ")
fh=open(fname)
l=[]

for line in fh:
    x=line.split()
    for word in x:
        if word in l:
            continue
        else:
            l.append(word)
        

l.sort()
print(l)
