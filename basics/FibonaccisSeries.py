# Fibonacci Series

# taking input
n = int(input("Enter limit: "))

# starting values
a, b = 0, 1

# logic
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b