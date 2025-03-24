import sys as sys

def add(a,b):
    add=a+b
    return add
def sub(a,b):
    sub=a-b
    return sub
def mul(a,b):
    mul=a*b
    return mul


a=float(sys.argv[1])   # a will be treated as float
operation=sys.argv[2]  # will be treated as string 
b=float(sys.argv[3]) # will be treated as float

if operation=="add":
    output=add(a,b)
    print(output)
elif operation=="sub":
    output=sub(a,b)
    print(output)
elif operation=="mul":
    output=mul(a,b)
    print(output)
else:
    print("invalid operation") 







