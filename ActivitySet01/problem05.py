# Functions

def computepay(h,r):
    if hrs>40:
        pay1=hrs*rate
        rate2=rate*0.5
        pay2=(hrs-40)*rate2
        pay=pay1+pay2
        
    else:
        pay=hrs*rate2
        
    return pay

hrs=float(input("Enter the number of hours you worked: "))
rate=float(input("Enter the rate per hour: "))

payment=computepay(hrs,rate)
print("Your payment is: ",payment)
