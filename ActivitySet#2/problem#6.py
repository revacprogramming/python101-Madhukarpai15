
class Menu(dict):
    """fill in class definition here"""
    def __init__(self):
        self={}
    
    def add(self,a,b):
        self[a]=b
    
    def show(self):
        x=list(self.keys())
        for i in x:
            print(i,self[i])


m = Menu()  # Menu is a class
m.add("idly", 10)
m.add("vada", 20)

m.show()
