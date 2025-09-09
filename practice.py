name = "Jhon"
age = 21
city = "Manila"

print(f"My name is {name}, I am {age} years old, and I live in {city}")

fruits = ["apple", "banana", "watermelon", "mango", "strawberry"]

print(fruits[0])
fruits[1] = "cherry"
fruits.append("star fruit")
print(fruits)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

my_sum = lambda a,b: a + b
diff = lambda a,b: a - b
prod = lambda a,b: a * b
quotient = lambda a,b: a / b

print(my_sum(num1, num2))
print(diff(num1, num2))
print(prod(num1, num2))
print(quotient(num1, num2))

input_number = int(input("Enter random number: "))

if input_number > 0:
    print("Positive")
elif input_number < 0:
    print("Negative")
else: 
    print("Zero")

for i in range(11):
    if(i == 0):
        continue
    print(i)

print("End of for loop")

num = 1
while num <= 10:
    print(num)
    num += 1

print("End of while loop")

def square(num):
    squared = num * num
    print(squared)

square(5)

import math

new_list = [3, 9, 1, 7]
print(max(new_list))
print(min(new_list))

print(sum(new_list))

name_input = input("Enter your name: ")
color_input = input("Enter your favourite color. ")

print(f"Hello {name_input}, your favourite color is {color_input}")


try: 
    random_num = int(input("Enter random number: "))
    quotient = 100 / random_num
    print(f"Quiotient is: {quotient}")

except ZeroDivisionError:
    print("Invalid number")
except ValueError as e:
    print(f"Error: {e}")
finally: 
    print("\nCongratuations, you have done exception handling")

with open("test.txt", "w") as file:
    file.write("Python is fun!")
with open("test.txt", "r") as fileread:
    content_of_file = fileread.read()
    print(content_of_file)

class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    
    def drive(self):
        print("The car is driving")
    
    def details(self):
        print(f"The car is {self.brand}, made from the year {self.year}")
    

car1 = Car("Honda", 2025)
car1.drive()
car1.details()

import math

print(math.sqrt(144))
print(math.factorial(5))

comprehension_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_num = [x for x in comprehension_list if x % 2 == 0]

print(even_num)

student = {
    "name" : "Juan",
    "age" : 21,
    "course" : "Programming"
}

for x, y in student.items():
    print(f"{x} : {y}")

set1 = {1,2,3}
set2 = {3,4,5}

print(set1 | set2)
print(set1 & set2)

# 15. write simple program that uses if, elif, else
# for loop
# break or continue
# def for function
# return inside the function


try:
    age = int(input("Enter your age: "))

    if age >= 18: 
        secret_number = 55

        num_of_try = int(input("How many you want to try to guess the secret number? "))

        if num_of_try > 0:
            for i in range(num_of_try):
                guess = int(input("Guess the secret number 1 - 100: "))

                if guess == secret_number:
                    print("You guessed it!")
                    break
                else:
                    i += 1
                    print("Wrong guess, try again")
            if i == num_of_try:
                print("Your tries has been exceed!")
        
        else: 
            print("Ok done")
    else:
        print("You can't guess the number right now")

except ValueError as e:
    print(f"Error: {e}")