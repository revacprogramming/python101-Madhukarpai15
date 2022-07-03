

def get_cs():
  """get string input"""
  a=input("Enter the string: ")
  return a


def cs_to_lot(cs):
    """convert connected string to list of strings"""
    final=[]
    x=cs.split(';')
    for i in x:
        y=i.split('=')
        z=tuple(y)
        final.append(z)
    return final


def main():
    cs = get_cs()
    lot = cs_to_lot(cs)
    print(lot)


if __name__ == '__main__':
    main()
