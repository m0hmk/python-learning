#Identify No. of Vowels

s = input("Enter a string: ")
v = 0

for i in s.lower():
    if i in "aeiou":
        v += 1

print(f"Number of vowels: {v}")