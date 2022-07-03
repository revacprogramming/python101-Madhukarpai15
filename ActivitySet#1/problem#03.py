# Variables, Expressions & Statements

def inputhrs():
  hrs=int(input("Enter the number of hours you have worked: "))
  return hrs

def inputrate():
  rate=float(input("Enter the rate per hour: "))
  return rate

def computepay(a,b):
  pay=hrs*rate
  return pay

def output(c):
  print("Your pay for the day is: ",pay)


hrs=inputhrs()
rate=inputrate()
pay=computepay(hrs,rate)
output(pay)