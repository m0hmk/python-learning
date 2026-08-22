a=[]
n=int(input("Enter Length of the list: "))
for i in range (n):
    x=int(input("Enter a number:"))
    a.append(x)

y=int(input("Enter a number to search in the list: "))
result=False
for i in a:
    if i==y:
        result=True
        break
if result:
    print("The number you entered is founded in the list.")
else:
    print("The number you entered is not founded in the list.")
     