
def input_two_numbers():
    a=int(input('enter the 1st number: '))
    #b=int(input('enteer the 2nd number: '))
    return a

def add(a, b):
   c=a+b
   return c
    


def output(a, b, sum):
    print('The sum of ',a,'and ',b,'is ',sum)


def main():
    a= input_two_numbers()
    b= input_two_numbers()
    sum = add(a, b)

    output(a, b, sum)


if __name__ == '__main__':
    main()
