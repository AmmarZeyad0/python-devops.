# A = "Hello, World!"
# B = "Python is great!"
# result = A + " : " + B
# print(result)


# # Integer Variable
# num1 = 10
# num2 = 5
# # Integer addition
# Addition = num1 + num2
# print("The sum of", num1, "and", num2, "is:", Addition)

# # Integer subtraction
# Subtraction = num1 - num2
# print("The difference between", num1, "and", num2, "is:", Subtraction)  

# # Integer multiplication
# Multiplication = num1 * num2
# print("The product of", num1, "and", num2, "is:", Multiplication)   

# # Integer division
# Division = num1 / num2
# print("The quotient of", num1, "divided by", num2, "is:", Division)

# # Float Variable
# num3 = 10.5
# num4 = 2.5
# # Float addition
# Addition = num3 + num4
# print("The sum of", num3, "and", num4, "is:", Addition)

# # Float subtraction
# Subtraction = num3 - num4
# print("The difference between", num3, "and", num4, "is:", Subtraction)

# # Float multiplication
# Multiplication = num3 * num4
# print("The product of", num3, "and", num4, "is:", Multiplication)

# # Float division
# Division = num3 / num4
# print("The quotient of", num3, "divided by", num4, "is:", Division) 

# Length of a string
# text = "Hello, World Mother fuicker!"
# # String length
# print(text)
# length = len(text)
# print("The length of the string is:", length)  # This line has an error, it should print length instead of text

# UPPERCASE and LOWERCASE
# text = "Hello, World Mother fuicker!"
# print(text)
# length = len(text)
# print("The length of the string is:", length)  # Corrected line to print the length of the string
# upper = text.upper()
# print("Uppercase:", upper)
# lower = text.lower()
# print("Lowercase:", lower)

# Replacing a substring
# text = "I love programming in Python. Python is great!"
# new_text = text.replace("Python", "Java")
# print("Original text:", text)
# print("Modified text:", new_text)

# String Splitting
# text = "Hello, World Mother fuicker!"
# new_text = text.split( )
# print("Original text:", text)
# print("Modified text:", new_text)  # This will print the list of words in the string

# # Print soecific object in split    
# arn = "arn:partition:service:region:account-id:resource-type/resource-id"
# new_arn = arn.split("/")
# print(arn.split("/")[1])  # This will print the first part of the ARN before the first slash

# List

# my_list = [1, 2, 3, 4, 5]
# # Accessing elements
# print("My List:", my_list)  # Accessing the first element
# my_list[0] = 9  # Modifying the first element
# print("Modified List:", my_list)  # Printing the modified list
# # Adding elements
# my_list.append(6)  # Adding an element to the end of the list
# print("List after appending 6:", my_list)  # Printing the list after app


# # Tuple
# my_tuple = (1, 2, 3, 4, 5)
# print("My Tuple:", my_tuple)  # Printing the tuple

# Set, you can add or remove item there's no modification of item in set
# my_set = {1, 2, 3, 4, 5}
# print("My Set:", my_set)  # Printing the set
# my_set.add(6)  # Adding an element to the set
# print("My set", my_set)  # Printing the set after adding an element
# my_set.remove(3)  # Removing an element from the set
# print("My set after removing 3:", my_set)  # Printing the set after removing an element

# Dictionary it's a key value pair, you can modify the value of the key but you can't modify the key and it's mutable

# my_dict = {"name": "John", "age": 30, "city": "New York"}
# print("My Dictionary:", my_dict)  # Printing the dictionary
# my_dict["age"] = 31  # Modifying the value of the "age" key
# print("My Dictionary after modifying age:", my_dict)  # Printing the dictionary after modifying the value

# text = "Python programming is fun and powerful!"
# upper_text = text.upper()
# lower_text = text.lower()
# print("Original text:", text)
# print("Uppercase:", upper_text)
# print("Lowercase:", lower_text)

x = [1, 2, 3]
 
print(type(x))