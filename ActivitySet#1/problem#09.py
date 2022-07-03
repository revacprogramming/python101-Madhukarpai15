#Files

def Input():
  fname=input("Enter the file name: ")
  return fname

def open_f(n):
  fh=open(n)
  return fh

l=[]

def find_num(b):
  for line in b:
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
  return avg


def output():
  print("Average spam confidence: ",avg)

fname=Input()
fh=open_f(fname)
avg=find_num(fh)
output(avg)
