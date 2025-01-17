# -*- coding: utf-8 -*-
"""Python_Class03.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nVIOYFMJfe6fuAsSMyBZTVptDKczQI2D
"""

# prompt: standard syntex create in python

# This is a single-line comment

"""
This is a multi-line comment.
It can span multiple lines.
"""

# Variable assignment
my_variable = 10

# Data types
integer_variable = 5
float_variable = 3.14
string_variable = "Hello, world!"
boolean_variable = True

# Basic operators
sum_result = 5 + 3
difference_result = 10 - 2
product_result = 4 * 6
quotient_result = 15 / 3
remainder_result = 10 % 3
power_result = 2 ** 3


# Conditional statements
if integer_variable > 0:
  print("Positive number")
elif integer_variable == 0:
  print("Zero")
else:
  print("Negative number")


# Loops
for i in range(5):
  print(i)

j = 0
while j < 3:
  print(j)
  j += 1


# Functions
def my_function(param1, param2):
  """This is a function docstring."""
  return param1 + param2

result = my_function(5, 3)
print(result)

# Classes
class MyClass:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

my_object = MyClass(15)
print(my_object.get_value())


# Exception handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero")


# Modules and packages
import math
print(math.sqrt(25))

# Input/Output
user_input = input("Enter your name: ")
print(f"Welcome " + user_input + "!")

# this is an loop immutable syntex
for x in range(1,11):
    # using two type of methode for print
    # print("10 x", x ,"=", x *10)
    print(f"10 x {x} = {x *10}")

age = 1
while age >= 0:
    print(age)
    age += 1
    if age == 6:
        break
else:
    print("age is not match equal to value")

password: str = "abc@123"
user = input("Enter your password: ")
while user != password:
    user = input("Try again: ")
else:
    print("Correct password")

# prompt: list and tupple syntex

# List example
my_list = [1, 2, 3, "apple", True]
print(my_list)
print(my_list[0])  # Accessing elements
my_list.append(4)  # Adding elements
print(my_list)

# Tuple example
my_tuple = (1, 2, 3, "banana", False)
print(my_tuple)
print(my_tuple[1]) # Accessing elements
# my_tuple.append(5)  # This will raise an error as tuples are immutable.
# print(my_tuple)

# Example of accessing list and tuple elements in loops:
for item in my_list:
  print(f"Item from list: {item}")

for item in my_tuple:
  print(f"Item from tuple: {item}")

"""Loop List Function"""

my_list = [1, 2, 3, "apple", True]
print(my_list)
print(my_list[0])  # Accessing elements
my_list.append("false")  # Adding elements
print(my_list)

"""Loop Tupple function"""

my_list = (1, 2, 3, "apple", True)
print(my_list)
print(my_list[3])  # Accessing elements
# print(my_list + ("56,98,635,544",)) # Adding elements

try:
    result = 20 / 0
except ZeroDivisionError:
    print("Error: Division by zero")