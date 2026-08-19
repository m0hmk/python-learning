#take inputs
s=input("Enter a string: ").lower()

digit=vowel=cons=space=special=0
vowels="aeiou"

for i in s:
	if i.isdigit():
		digit+=1
	elif i.isalpha():
		if i in vowels:
			vowel+=1
		else:
			cons+=1
	elif i==" ":
		space+=1
	else:
		special+=1

print (f"no. of Vowels: {vowel}\nno. of Consonants: {cons}\nno. of digits: {digit}\nno. of spaces: {space}\nno. of special characters: {special}")