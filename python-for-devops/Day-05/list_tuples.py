
# use variables
s1="john"
s2="ankit"
s3="David"
print(s1)
print(s2)
print(s3)

#sequence data types
# use lists, mutable, can be resized
student_names=["John", "Ankit", "David"]
print(student_names)

# print datatype
print(type(student_names))

# print length
print(len(student_names))

# add elements
student_names.append("Jai")
print(student_names)

# remove elements
student_names.remove("John")
print(student_names)

# print single element
print(student_names[0])

# slice a list
new_names=student_names[0:2]
print(new_names)

# sort list
numbers=[1,5,20,3]
numbers.sort()
print(numbers)

#concatenate 2 elements
print(student_names[0]+" "+student_names[1])

# list with different data types
new_list=[1,"student",3.5]
print(new_list)
########################################################################################

#use tuples, immutable list, cannot be resized, better memory allocation/footprint 
student_names=("John", "Ankit", "David")
print(student_names)

# print datatype
print(type(student_names))

# print single element
print(student_names[0])

# print length
print(len(student_names))

# add elemets
student_names.append("Jai")
print(student_names)

# remove elements
student_names.remove("John")
print(student_names)