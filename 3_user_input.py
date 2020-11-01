# Task: Get the input from user e.g. his/her name and their favourite color
#       and print a message like 'John likes Black'

# User Input
name = input('What is your name? ')
print('Hi ', name)
color = input('What is your favourite color? ')
print(name, 'likes', color)

# Note: Whenever we use 'input' function for user input, it always stores the data as a string and we need to convert
#       it to a different datatype if we want to use it differently.