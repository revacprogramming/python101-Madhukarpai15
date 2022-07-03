

def get_cs():
    """get string input"""
    a=input("Enter the string: ")
    return a


def cs_to_dict(cs):
    """convert connect string to a dictionary"""
    d={}
    x=cs.split(';')
    for i in x:
        y=i.split('=')
        d[y[0]]=y[1]
    return d


def dict_to_cs(d):
    """convert a dictionary to connect string"""
    final=''
    x=list(d.keys())
    y=list(d.values())
    size=len(x)
    for i in range(0,size):
        eql=x[i]+'='+y[i]
        col=eql+';'
        final+=col
    size2=len(final)
    return final[:size2-1]
        
    

def main():
    cs = get_cs()

    d = cs_to_dict(cs) # convert connect string to a dictionary
    print(d)

    cs = dict_to_cs(d)
    print(cs)


if __name__ == '__main__':
    main()
