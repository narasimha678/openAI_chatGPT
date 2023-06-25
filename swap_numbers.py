# Program to swap two numbers

# Store input numbers
num1 = input('Enter first number: ')
num2 = input('Enter second number: ')

# Swapping
temp = num1
num1 = num2
num2 = temp

# Displaying swapped numbers
print("Value of num1 after swapping: {}".format(num1))
print("Value of num2 after swapping: {}".format(num2))