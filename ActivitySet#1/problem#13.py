# Tuples

def Input():
  fname=input("Enter the file name: ")
  return fname

def open_f(a):
  fh=open(a)
  return fh
  
l=[]
t1=()
t2=()

def hrs(b):
  for line in b:
      if line.startswith("From"):
          pos=line.find(":")
          time=line[pos-2:pos+6]
          sepa=time.split(":")
          hrs=sepa[0]
          try:
              hrs1=int(hrs)
              l.append(hrs1)
          except:
              continue
          if hrs1 not in t1:
              t1=list(t1)
              t1.append(hrs1)
              t1=tuple(t1)

def output():
  size=len(t1)
  for i in range(0,size):
      count=l.count(t1[i])
      t2=list(t2)
      t2.append(count)
      t2=tuple(t2)
      print(t1[i],  t2[i])

fname=Input()
fh=open_f(fname)
hrs(fh)
output()
