#Conditional Execution 2

def Input():
    score=float(input('Enter the score: '))
    return score

def find_grade(a):
    if a>1.0 or a<0.0:
        return 'The grade entered is out of range.'
    else:
        if a>=0.9:
            return 'A'
        elif a>=0.8:
            return 'B'
        elif a>=0.7:
            return 'C'
        elif a>=0.6:
            return 'D'
        elif a<=0.6:
            return 'F'

def output(c):
    print(c)

score=Input()
grade=find_grade(score)
output(grade)