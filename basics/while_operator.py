#sum of digit, reverse, palindrome, Armstrong

original=num=num1=num2=int(input("Enter a number: "))


#sum of digit
s=0
while num>0:
	d=num%10
	s+=d
	num//=10
print(f"sum of digits of {original}: {s}")

#reverse
r=0
while num1>0:
	d1=num1%10
	r=r*10+d1
	num1//=10
print (f"reverse of {original}: {r}")

#palindrime
if original==r:
	print (f"{original} is Palidrome")
else:
	print (f"{original} is not Palidrome")

#armstrong number
a=0
l=len(str(original))
while num2>0:
	d2=num2%10
	a=d2**l+a
	num2//=10
if original==a:
	print (f"{original} is an Armstrong Number")
else:
	print (f"{original} is not an Armstrong Number")