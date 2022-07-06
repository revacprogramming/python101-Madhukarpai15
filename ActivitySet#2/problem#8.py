

#commitdone 
class Menu:
  """fill in class definition here"""
  def __init__(self):
      self.d={}
  def __setitem__(self,a,b):
    '''self.a=a
    self.b=b'''
    self.d[a]=b
  def __str__(self):
      return self.d.__str__()
    

m = Menu()
m["idly"] = 10
m["vada"] = 20

print(m)
