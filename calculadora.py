#!/bin/python3
"""
A simple calculator with a simple menu
this code is native from shell script of linux
"""
# variable input
print("Let's start:")
number_a = int(input('Insert a number:'))
number_b = int(input('one more time:'))

# making a simple menu:
print(""""	
Select the operation:"
	a - Addiction
	b - Subtraction
	c - Multiplication
	d - Division
	""")
choice = input("Input the letter of correspondent operation:")
# Let's start we program:

# setting addiction
if choice == "a" or choice == "A":
	result = number_a + number_b
	print(f"The sum of {number_a} and {number_b} it's: {result}")

# setting subtraction
elif choice == "b" or choice == "B":
	result = number_a * number_b
	print(f"The subtraction of {number_a} and {number_b} it's: {result}")

# setting multiplication
elif choice == "c" or choice == "C":
	result = number_a * number_b
	print(f"The product of {number_a} and {number_b} it's: {result}")

# setting division

elif choice == "d" or choice == "D":
	if number_b == 0:
		print("Its impossible division per 0")
	else:
		result = number_a / number_b
		print(f'The division of {number_a} per {number_b} is: {result}')

else:
	print('invalid operation, please try again')

print('thanks for use this program')

'''
Batalha.ISD, 2022
'''
