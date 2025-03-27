# dict data type used to hold attributes for an object
# dict have concept called as key=value pair

student_info= {
"name": "John",
"age": 15,
"grade": 9
}
print(student_info)
print(student_info["name"])
print(student_info["grade"])

# problem with list how will you remember what you are storing at that index number

student_info=["John", 15, 9]
print(student_info[2])  # problem is we need to remember that index 2 is grade not age


# how can we store multiple students attributes in a dictionary
# create seperate dictionary for each student, will end with lot many dict
# else create a list of dict
# students_info=[{},{},{}]

students_info= [
{
"name": "John",
"age": 15,
"grade": 9
},

{
"name": "David",
"age": 14,
"grade": 8
},

{
"name": "Ankit",
"age": 16,
"grade": 10
}
]
print(students_info)
print(students_info[0]["name"])
print(students_info[1]["name"])
print(students_info[2]["name"])

######################################################################
# Modifying and Adding Elements in dictionary 

my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
print(my_dict["age"])

my_dict["age"] = 26  # Modifying/update the value for a key 
print(my_dict["age"])

my_dict['occupation'] = 'Engineer'  # Adding a new key-value pair
print(my_dict["occupation"])
print(my_dict)

######################################################################

# Removing Elements in dictionary

del my_dict["city"]  # Removing a key-value pair
print(my_dict)
# print(my_dict["city"]) #if you print city it will give error as the key value pair is removed
######################################################################

# Checking Key Existence
if 'age' in my_dict:
    print('Age is present in the dictionary')
else :
    print ('Age is not present in the dictionary')
######################################################################

# Iterating Through Keys and Values:
print(my_dict.items())
for key, value in my_dict.items():
   print(key, value)

