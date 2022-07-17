#Loops and Iterations

#largest=None
#smallest=None
#index=1
l=[]

while True:
    user=input("Enter a number: ")
    if user=="done":
        break
    try:
        user2=int(user)
    except:
        print("Not an integer.")
        continue
    l.append(user2)
    #user2=None
    #index+=1
    
    
size=len(l)
l.sort()
print("Minimum: ",l[0])
print("Maximum: ",l[size-1])

