# Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.


# Psuedo Code


# Ask user input for 2 numbers
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

# Get the product of the two numbers
product = first_number * second_number


# Add the sum of two numbers
sum = first_number + second_number


# Write it so that you'll return the product of the two numbers if equal to or lower than 1000 otherwise return their sum
if product <= 1000: 
    print("Since the product of the two numbers is less than or equal to 1000,""\n"f"The product of {first_number} and {second_number} is {product}")
else:
    print(("Since the product of the two numbers is more than 1000,""\n"f"The sum of {first_number} and {second_number} is {sum}"))