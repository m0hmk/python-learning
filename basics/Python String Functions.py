#Python String Functions

text = "Python"

# Print taken string
print(f'Taken string:\n text = "{text}"')

# Data type
print(f'Data type of "{text}": {type(text)}')

# String slicing
print(f'Characters from index 1 to 3 in "{text}": {text[1:4]}')
print(f'Characters from index 2 to the end in "{text}": {text[2:]}')
print(f'Characters from the beginning to index 3 in "{text}": {text[:4]}')
print(f'Copy of the whole string "{text}": {text[:]}')
print(f'Every second character in "{text}": {text[::2]}')
print(f'"{text}" in reverse order using step -1: {text[::-1]}')
print(f'"{text}" in reverse order using step -2: {text[::-2]}')

# Length
print(f'Number of characters in "{text}": {len(text)}')

# Count
print(f'Number of times "P" occurs in "{text}": {text.count("P")}')

# Find
print(f'First index of "t" in "{text}": {text.find("t")}')

# Lowercase
lower_text = text.lower()
print(f'"{text}" in lowercase: "{lower_text}"')

# Check lowercase
print(f'Is "{lower_text}" completely lowercase? {lower_text.islower()}')

# Uppercase
upper_text = text.upper()
print(f'"{text}" in uppercase: "{upper_text}"')

# Check uppercase
print(f'Is "{upper_text}" completely uppercase? {upper_text.isupper()}')

# Check digits
number = "12345"
print(f'Does "{number}" contain only digits? {number.isdigit()}')

# Add spaces for strip methods
spaced_text = "  Python  "
print(f'String with extra spaces: "{spaced_text}"')

# Remove leading spaces
left_clean = spaced_text.lstrip()
print(f'After removing leading spaces from "{spaced_text}": "{left_clean}"')

# Remove trailing spaces
right_clean = spaced_text.rstrip()
print(f'After removing trailing spaces from "{spaced_text}": "{right_clean}"')

# Remove spaces from both sides
clean_text = spaced_text.strip()
print(f'After removing spaces from both sides of "{spaced_text}": "{clean_text}"')

# Replace
replaced_text = text.replace("Python", "Java")
print(f'After replacing "Python" with "Java" in "{text}": "{replaced_text}"')

# Split
sentence = "Python is easy"
words = sentence.split(" ")
print(f'After splitting "{sentence}" into words: {words}')

# Join
joined_text = "-".join(words)
print(f'After joining {words} with "-": "{joined_text}"')