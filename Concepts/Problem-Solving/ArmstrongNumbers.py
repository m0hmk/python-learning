#armstrong number

#pre-values
pl=1
power=list(range(10))

#create function
def armstrong (n):
    global pl,power
    if n<0:
        return False
    n1=n
    a=0
    l=len(str(n))
    if pl!=l:
        power=[d**l for d in range (10)]
        pl=l
    while n1:
        d=n1%10
        a+=power[d]
        n1//=10
    return n==a

#check armstrong number
num=int(input("Enter a number: "))    
if armstrong (num):
	print (f"{num} is an Armstrong Number.")
else:
	print (f"{num} is not an Armstrong Number.")

#print armstrong numbers in range
print("\nEnter a range:")    
x=int(input("\tStart: "))
y=int(input("\tEnd: "))
print (f"All armstrong numbers in the range ({x}-{y}) are:")
f=0
for i in range (x,y+1):
    if armstrong(i):
        print(i, end=" ")
        f+=1
if f:
    print("\nTotal armstrong numbers:",f)
else:    
    print("<empty>")        