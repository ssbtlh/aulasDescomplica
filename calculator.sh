#!/bin/bash

#an simple calculator made in shell, code by Isaias.

# we will take two simple user inputs.

echo "Input two integrer numbers:"
read number_a
read number_b

# making a simple menu:

echo "	Select the operation:"
echo "	a - Addiction"
echo "	b - Subtraction"
echo "	c - Multiplication"
echo "	d - Division"
echo
echo "Input the letter of correspondent operation:"
read choice
echo

# Let's start we program:

# setting addiction
if [ $choice = "a" ];
then
	result=$((number_a+number_b))
	echo "The sum of $number_a and $number_b it's: $result"

# setting subtraction
elif [ $choice = "b" ];
then
	result=$((number_a-number_b))
	echo "The subtraction of $number_a per $number_b it's: $result"

# setting multiplication
elif [ $choice = "c" ]; 
then
	result=$((number_a*number_b))
	echo "The product of $number_a and $number_b it's: $result"

# setting division
elif [ $choice = "d" ]; 
then
	if [ $number_b -eq 0 ];
	then
		echo "I'ts impossible division per 0"
	else
		result=$((number_a/number_b))


	echo "The division of $number_a per $number_b is: $result"
	fi

else
	echo "Please input letters only "

fi

echo
echo
echo "Thanks for use our program"
