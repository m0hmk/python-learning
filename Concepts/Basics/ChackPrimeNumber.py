#check prime numbers

#taking Input
num=int(input("Enter a number: "))

#logic
if(num<=1):
    print(num,"is a non-prime number.")
else:
    is_prime=True
    for i in range(2,int(num**0.5)+1):
        if(num%i==0):
            is_prime=False
            break

#print output    
    if is_prime:
        print(num,"is a prime number.")
    else:
        print(num,"is a non-prime number.")
            