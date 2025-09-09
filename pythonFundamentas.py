# variables 
x = 10 # integer variable
y = 3.14 # float variable
name = "Alice" # string variable
is_active = True # boolean variable

# strings

print(name.upper()) # name in uppercase ALICE
print(name.lower()) # name in lowercase alice
print(name[0]) # indexing A
print(name[0:3]) # slicing Ali (first 3 characters)
print(name[::-1]) # reversing the string ecilA
print(name[0:5:2]) # slicing with step (start:stop:step) - Aie looks at every 2nd character but stops BEFORE index 5
print(len(name)) # length of the string 5
print(name + " Smith") # string concatenation - Alice Smith
print(f"Hello, {name}!") # formatted string - Hello, Alice!
print(name.replace("A", "E")) # string replacement - ELice
print(" Hello".strip()) # stripping whitespace - Hello (no leading space)
print(name.split("i")) # splitting the string ['Al', 'ce'] 
print(name.find("l")) # finding substring index 2 (first occurrence of 'l)

# Lists (ordered, changeable)

fruits = ["apple", "banana", "cherry"]
fruits.append("mango") # adding an element to the end
fruits.remove("banana") # removing an element
fruits[1] = "grapes" # modifying an element
print(fruits) # ['apple', 'grapes', 'mango'] no cherry because banana was removed and index 1 was changed to grapes

# Tuples (ordered, unchangeable)

fruits_tuple = ("apple", "banana", "cherry")
print(fruits_tuple[1]) # accessing an element by index - banana

# Sets (ordered, unindexed, no duplicates)

s = {1, 2, 3, 4, 5}
s.add(6) # adding an element
s.remove(3) # removing an element

# dictionaries (unordered, changeable, key-value pairs)

person = {
    "name" : "Alice",
    "age" : 30,
    "city" : "New York"
}

print(person["name"]) # accessing value by key - Alice
person["age"] = 31 # modifying a value
person["job"] = "Doctor" # adding a new key-value pair
print(person) # {'name': 'Alice', 'age': 31, 'city': 'New York', 'job': 'Doctor'}

# operators
a = 10
b= 3

print(a + b) # addition 13
print(a - b) # subtraction 7
print(a * b) # multiplication 30
print(a / b) # division 3.3333333333333335
print(a // b) # floor division 3
print(a % b) # modulus 1
print(a ** b) # exponentiation 1000

# comparison operators
print(a == b) # equal False
print(a != b) # not equal True
print(a > b) # greater than True
print(a < b) # less than False
print(a >= b) # greater than or equal True
print(a <= b) # less than or equal False

# Logical operators
print(True and False) # logical AND - False
print(True or False) # logical OR = True
print(not True) # logical NOT - False

# control flow 
# make sure to use proper indentation (4 spaces or a tab)

# conditional statements
if a < b:
    print("a is less than b")
elif a == b:
    print("a is equal to b")
else:
    print("a is greater than b")

# Loops

# While loop
count = 0
while count < 5:
    print(count) # will print numbers 0 - 4
    count += 1 # increment count by 1

# For loop

for i in range(5) : # range(5) generates numbers from 0 - 4
    print(i) # will print numbers 0 -4

for fruit in fruits: 
    print(fruit) # will print each fruit in the fruits list

# break and continue

for i in range(10):
    if  i == 5:
        break # exit the loop when i is 5
    print(i)

for i in range(10):
    if i == 2:
        continue # skip 2 and
    print(i) # will print numbers 0 - 9 except 2

# functions

def greet(name = "World"): # function with a default parameter
    return f"Hello, {name}!" # returns a greeting string

print(greet()) # calling function without argument - Hello, World!
print(greet("Alice")) # calling function with argument - Hello, Alice!

# lambda functions (anonymous functions)
# its a small one line function

square = lambda x: x * x # lambda function to calculate square, x is the input and x*x is the output
print(square(5)) # calling lambda function - 25

# another example of lambda function
greet = lambda name: f"Hello, {name}!"
print(greet("Bob"))

# modules and packages
# import standard library module
# by default python comes with many built-in modules like math, datetime,os, sys etc
import math
from math import pi, sqrt # importing specific functions from math module, so you can use them directly without math. prefix

print(sqrt(16)) # using sqrt function directly not math.sqrt, 4.0
print(math.factorial(5)) # using factorial function with math. prefix, 120

# built-in functions

print(abs(-10)) # absolute value 10
print(round(4.6)) # rounding 5
print(type(name)) # checking variable type <class 'str'>
print(len("Alice")) # length of string 5
print(int(3.14)) # converting float to integer - 3
print(max(1, 2, 3, 4, 5)) # maximum value 5
print(min(1, 2, 3, 4, 5)) # minimum value 1
print(sum([1, 2, 3, 4, 5])) # sum of list elements 15
print(sorted([5, 2, 9, 1])) # sorting a list [1, 2, 5, 9]

# input and output
user_input = input("Enter your name: ") # taking user input in the console
print(f"Hello, {user_input}!")

# Exception handling
try: 
    x = int("abc") # this will raise a ValueError
except ValueError as e:
    print(f"Error: {e}")
finally:
    print("Execution completed. ")

# another example of exception handling
try:
    result = 10 / 0 # this will raise a ZeroDivisionError
except ZeroDivisionError as e:
    print(f"Error: {e}")
finally:
    print("Execution completed.")

# File handling

# writing to a file
with open("test.txt", "w") as file: # open file in write mode, w stands for write
    file.write("Hello, World from created file!\n") # write to the file

# reading from a file
with open("test.txt", "r") as file: # open file in read mode, r stands for read
    content = file.read() # read the file content
    print(content)

with open("test.txt", "a") as file: # open file in append mode, a stands for append
    file.write("Appending a new line. \n")

# Classes and Objects 
# Class is a blueprint for creating objects

class Person: # defining a class
    def __init__(self, name, age): # constructor method, self refers to the instance of the class,
                                 # name and age are parameters
        self.name = name
        self.age = age
    def greet(self): 
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


p1 = Person("Alice", 30) # creating an object of the Person class
p1.greet() # calling the greet method 

# List comprehension (advanced)

numbers = [1,2,3,4,5]
squared = [x * x for x in numbers] # list comprehension to create a new list with squared values
print(squared) # [1, 4, 9, 16, 25]

even_numbers = [x for x in numbers if x % 2 == 0] # filtering even numbers using list comprehension
print(even_numbers) # [2, 4]

# Dictionary comprehension (advanced)
person_dict = {
    "name" : "Alice",
    "age" : 30,
    "city" : "New York"
}

for key, value in person_dict.items():
    print(f"{key} : {value}")

# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a.union(b)) # union {1, 2, 3, 4, 5, 6}
print(a | b) # union using | operator {1, 2, 3, 4, 5, 6}

print(a.intersection(b)) # intersection {3, 4}
print(a & b) # intersection using & operator {3, 4}

print(a.difference(b)) # difference {1, 2}
print(a - b) # difference using - operator {1, 2}

print(a.symmetric_difference(b)) # symmetric difference {1, 2, 5, 6}
print(a ^ b) # symmetric difference using ^ operator {1, 2, 5, 6}

# important ket words to remember

# import, def, class, ifm elif, else, for, while,
# break, continue, pass, try, except, finally, return
# with, as, lambda, global, nonlocal, True, False, None, in, is, and, or, not

