# Conditional Execution

def inputhrs():
  hrs1=input("Enter the number of hours you have worked: ")
  hrs=float(hrs1)
  return hrs

def inputrate():
  rate=float(input("Enter the rate per hour: "))
  return rate


def compute_ot(a,b):
  if hrs>40:
    pay1=hrs*rate
    hrs2=hrs-40
    rate1=rate*0.5
    pay2=hrs2*rate1
    pay=pay1+pay2
  
  else:
    pay=hrs*rate

  return pay

def output(c):
  print('Your pay for the day is: ',pay)

hrs=inputhrs()
rate=inputrate()
pay=compute_ot(hrs,rate)
output(pay)