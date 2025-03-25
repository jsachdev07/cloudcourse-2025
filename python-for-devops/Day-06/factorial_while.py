# Function to calculate factorial using a while loop
def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

# Input from the 
# The input() function in Python is used to get user input from the console.
number = int(input("Enter a number to calculate its factorial: "))

# Ensure the number is non-negative
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"The factorial of {number} is {factorial(number)}.")

"""
 last line is an example of f-string formatting in Python, which is a way to embed expressions inside string literals. Here's how it works:
 f"..."
 The f before the string tells Python that it's an f-string. 
 This means you can include variables or expressions inside curly braces {} within the string
 And Python will evaluate them and insert their values into the string.
"""