#check no. of prime numbers in a particular range

#taking inputs
R=input("Enter range of numbers (syntax: start-end) (e.g. 1-100): ")

#spliting inputs
start,end=map(int,R.split("-")) 

#printing info
print(f"\nPrime Numbers in the range {R} are:")

#creating logic
n=0
for i in range(start,end+1):
	if (i>1):
		if i==2:
			print (i, end=", ")   #printing 2
			n+=1
		elif i%2==0:
			continue
		else:
			is_prime=True
			for j in range(3,int(i**0.5)+1,2):
				if (i%j==0):
					is_prime=False
					break
			if is_prime:
				print (i, end=", ")   #printing prime numbers
				n+=1

#printing no. of prime numbers
print(f"\nNo. of Prime Numbers in the range of ({R}) is: {n}")  #printing prime numbers

#printing no. of prime numbers
print(f"\nNo. of Prime Numbers in the range of ({R}) is: {n}")