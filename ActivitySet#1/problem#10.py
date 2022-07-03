#Lists 1

def Input():
  fname=input("Enter the file name: ")
  return fname

def open_f(a):
  fh=open(a)
  return fh

l=[]

def find_word(b):
  for line in b:
      x=line.split()
      for word in x:
          if word in l:
              continue
          else:
              l.append(word)
          
        
def output(c):
  l.sort()
  print(l)

fname=Input()
fh=open_f(fname)
find_name(fh)
output()
