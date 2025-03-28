
#open() function in Python is used to open a file in a specific mode (for reading, writing, appending, etc.) so you can interact with it.
#rw, wr, ar, open()--> r, w, a, r+, w+, a+
# open() --> filepath and the operation 
# open() will only pen the file in certain mode 
# if you want to perform any operation like read , write , you need to call read() or write()

file_path = 'c:/Users/jaiprakash/Desktop/python/example.txt'
file = open(file_path, 'r')
content = file.readlines()
print(content)
print(type(content))  # type will be a list, readlines() will return a list of lines
file.close()

##############################################################

file_path = 'c:/Users/jaiprakash/Desktop/python/example.txt'

# Open the file in read mode
file = open(file_path, 'r')

# Read the content of the file
content = file.read()
print(content)
print(type(content))   # type will be a string , read() will return a string of all lines

# Don't forget to close the file when done
file.close()
##############################################################


file_path = 'c:/Users/jaiprakash/Desktop/python/example.txt'

# Open the file in write mode (this will overwrite existing content)
file = open(file_path, 'w+')   # w+ will do write and then read, w will only do write no read

# Write content to the file
file.write("hello everyone" + "\n")
file.write("welcome to python program")

file.seek(0)  # move the pointer to position zero before you read the file
# Read the content of the file
new_content = file.read()
print(new_content)

# Close the file after writing
file.close()

##############################################################


file_path = 'c:/Users/jaiprakash/Desktop/python/example.txt'

# Open the file in append mode (this adds new content at the end)
file = open(file_path, 'a+')   # a+ will open file in append + read mode

# Append content to the file
file.write("\nThis is appended content!")
file.seek(0)
new_content = file.read()
print(new_content)

# Close the file after appending
file.close()

##############################################################

# open() is a function used to open files in Python.
# with open() is a more reliable way to open files because it ensures proper file closure.

# Instead of manually calling close(), Python provides a cleaner and safer way to work with files using the with statement. 
# The with statement automatically takes care of closing the file when you're done, even if an error occurs.

# Open the file using the 'with' statement (automatically closes the file after use)

with open('c:/Users/jaiprakash/Desktop/python/example.txt', 'r') as file:
    content = file.read()
    print(content)  # Do something with the content (in this case, printing it)
# No need to explicitly close the file, it gets closed automatically after the block'


##############################################################



