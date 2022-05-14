# Files

fname=input("Enter the file name: ")
fh=open(fname)
l=[]

for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        pos=line.find(":")
        flt=line[pos+3:]
        flt2=float(flt)
        l.append(flt2)
    else:
        continue
        

size=len(l)
total=0
for i in range(0,size):
    total+=l[i]
avg=total/size

print("Average spam confidence: ",avg)
