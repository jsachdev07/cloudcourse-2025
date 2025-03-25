import sys
n=int(sys.argv[1])

def factorial(n):       
    # If the number is negative, return an error message
    if n < 0:
        print ("Factorial is not defined for negative numbers")
    elif n == 0 or n == 1:
        print(1)
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        print(result)

factorial(n)
    