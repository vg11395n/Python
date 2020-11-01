# Task #1: Get the input from user and calculate his/her age

# Note: Whenever we use 'input' function for user input, it always stores the data as a string and we need to convert
#       it to a different datatype if we want to use it differently.

# User input datatype conversion
birth_year = input('Birth Year: ')

# This line should return <class 'str'>
print(type(birth_year))

# to perform this calculation we need to convert str datatype to int datatype
age = 2020 - int(birth_year)

# This line should return <class 'int'>
print(type(age))

# To concatenate results we use '+' operator within print command but it works only with str datatype
# To concatenate int value we need to use ',' operator within print command
print('Your age is: ', age)

# Task #2: Ask user their weight (in pounds), convert it into kilograms and print it on the terminal

weight_lb = input('What is your weight in pounds: ')
weight_kg = float(weight_lb) * 0.453592
print('Your weight in pounds is:', weight_lb, 'lbs')
print('Your weight in kilograms is:', float(weight_kg), 'kgs')

