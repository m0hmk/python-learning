#WAP in Python to search number in a list using binary search, merge sort.
import sys
#input
list_size=int(input("Enter Length of the list: "))
attempts=1
while (list_size<=0):
    if attempts==3:
        print ("You should quit. 🥲")
        sys.exit()
    else:
        print ("Give us some space! 🥺")
        list_size=int(input(f"Chance {'I'*(attempts+1)}: "))
        attempts+=1
#input function for creating list
def create_list(list_size):
    numbers=[]
    for i in range (list_size):
        if i==0:
            numbers.append(int(input("Enter a number: ")))
        else:
            numbers.append(int(input("Another one: ")))
    print ("\nYour List:",numbers)
    return numbers
numbers=create_list(list_size)
#Function for Marge Sort
def merge_sort (unsorted_list):
    size=len(unsorted_list)
    if size<=1:
        return unsorted_list
    mid=size//2
    a=merge_sort(unsorted_list[:mid])
    b=merge_sort(unsorted_list[mid:])
    updated_list=[]
    i=j=0
    while i<len(a) and j<len(b):
        if a[i]<=b[j]:
            updated_list.append(a[i])
            i+=1
        else:
            updated_list.append(b[j])
            j+=1
    return updated_list+a[i:]+b[j:]
numbers=merge_sort(numbers)
print ("\nSorted list:",numbers)
#Function for binary search
def search(numbers,num):
    start=0
    end=len(numbers)-1
    while start<=end:
        mid=(start+end)//2
        if numbers[mid]==num:
            return True
        elif numbers[mid]>num:
            end=mid-1
        else:
            start=mid+1
    return False
#Output
required_numbers=set(numbers)
found_numbers=set()
attempts={}
while (required_numbers!=found_numbers):
    x=int(input("\nEnter a number to search in the list: "))
    if x in found_numbers:
        print (f"We've already found {x}. 😁")
    elif search(numbers,x):
        print(f"Yeah! We got {x}. 🤗")
        found_numbers.add(x)
    else:
        attempts[x]=attempts.get(x,0)+1
        if attempts[x]==1:
            print(f"Sorry, we couldn't find {x}. 😮‍💨")
        elif attempts[x]<=3:    
            print (f"Don't you dare searching {x} AGAIN! 🤨")
        else:
            print ("You have potential to win Oscar! 😱")
            sys.exit()