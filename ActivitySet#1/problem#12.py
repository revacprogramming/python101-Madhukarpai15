# Dictionaries

def Input():
  fname=input("Enter the file name: ")
  return fname
  
def open_f(a):
  fh=open(a)
  return fh
  
l=[]
d={}
l1=[]

def mail_count(b):
  for line in b:
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
  vals=[]
  vals.append(maxkey)
  vals.append(maxval)
  return vals

def output(c):
  print(c[0],c[1])

fname=Input()
fh=open_f(fname)
result=mail_count(fh)
output(result)