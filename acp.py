def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def print_fibonacci_sequence(count):
#Print Fibonacci sequence up to user input
    if count < 0:
        print("Please enter a positive integer")
    else:
        print("Fibonacci sequence:")
        for i in range(count):
            print(fibonacci(i), end=" ")

# Get user input
terms = int(input("How many terms of the sequence would you like? "))

# Print the sequence
print_fibonacci_sequence(terms)