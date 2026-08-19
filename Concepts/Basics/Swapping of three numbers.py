#Taking Inputs
print ("Enter three numbers:")
a = int (input ("a= "))
b = int (input ("b= "))
c = int (input ("c= "))

#Print Originals
print (f"Before Swapping: {a}, {b}, {c}")

#Operation
a,b,c = b,c,a

#Print Swapping
print (f"After Swapping: {a}, {b}, {c}")
