num=num1=int(input("Enter a number: "))

#negative-positive
if num>0:
    print (num,"is a positive number.")
elif num<0:
    print (num,"is a negative number.")
else:
    print ('"Zero" is neither positive nor negative.')
	
# odd/even numbers, count and sum
limit = abs(num)
print (f"\nAll Odd Numbers in range (1-{limit}):")
n=s=0
for i in range (1,limit+1,2):
    print (i, end=" ")
    n+=1
    s+=i
print ("\nnumber of odd:",n)
print ("sum of odd:",s)
print (f"\nAll Even Numbers in range (1-{limit}):")
n=s=0
for i in range (2,limit+1,2):
    print (i, end=" ")
    n+=1
    s+=i
print ("\nnumber of even:",n)
print("sum of even:",s)

#greaset number (nested)
print ("\nEnter Numbers:")
a= int(input("1st: "))
b= int(input("2nd: "))
c= int(input("3rd: "))
print ("The Greaset number is", end=" ")
if a>b:
    if a>c:
        print(a)
    else:
        print(c)
else:
    if b>c:
        print(b)
    else:
        print(c)

#factorial
fact=1
while num1>0:
    fact*=num1
    num1-=1
print (f"factorial of {num}: {fact}")

#total marks, avg, grade, for 4 subjects. grade: if avg: A,B,C>=80,60,40 and F<40
print ("Enter marks:")
py= int(input("Python: "))
c= int(input("C: "))
ds= int(input("Data Structure: "))
al= int(input("Algorithms: "))

total= (py+c+ds+al)
avg= total/4

print ("Total Marks: ",total,"\nAverage Marks: ",avg)
print ("Grade: ",end="")

if avg>=80:
    print("A")
elif avg>=60:
    print("B")
elif avg>=40:
    print("C")
else:
    print("F")