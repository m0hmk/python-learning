#PRIME NUMBERS

#create function
def prime(n):
    if n<2 or (n!=2 and n%2==0):
        return False
    for i in range (3,int(n**0.5)+1,2):
        if n%i==0:
            return False
    return True
    
#prime numbers in range
print("Enter a range:")
a=int(input("\tStart: "))
b=int(input("\tEnd: "))
print(f"All prime numbers in the range ({a}-{b}) are:")
no=0
for  i in range (a,b+1):
    if prime(i):
        no+=1
        print(i, end=" ")
print("\nTotal no. of prime numbers:",no)
        
#check prime number
num=int(input("\nEnter a number to check: "))
if prime(num):
    print(num,"is a prime number.")
else:
     print(num,"isn't a prime number.")           