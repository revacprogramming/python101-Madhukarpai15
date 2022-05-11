# Conditional Execution

hrs1=input("Enter the number of hours you have worked: ")
hrs=float(hrs1)
rate=float(input("Enter the rate per hour: "))


if hrs>40:
    pay1=hrs*rate
    hrs2=hrs-40
    rate1=rate*0.5
    pay2=hrs2*rate1
    pay=pay1+pay2
    print("Your pay for the day is: ",pay)

else:
    pay=hrs*rate
    print("Your pay for the day is: ",pay)
