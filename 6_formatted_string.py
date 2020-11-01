first = 'John'
last = 'Smith'

message = first + ' [' + last + '] is a coder'
print ('Without use of formatted string: ', message)

# Such concatenation is not possible all the time. For such time we formatted string.
# Formatted string starts with 'f' and uses curly braces to hold values of variables.
# e.g. print the same message

msg = f'{first} [{last}] is a coder'
print('With use of formatted string: ', msg)

# String Methods:
# len()         : Provides length of the string
# upper()       : Converts string to upper case
# lower()       : Converts string to lower case
# find()        : Find the index of a character in given string
# replace()     : Replace a character or word in given string
# in operator   : Find the character or word in given string

print('Length of msg is: ', len(msg))
print('msg in UPPER CASE:', msg.upper())
print('msg in lower case:', msg.lower())
print('find the index of the character in a string:', msg.find('J'))
print('replace the character/word in a string:', msg.replace('Smith', 'Cena'))
print('find the whether the character/word exists in a string or not:', ('Smith' in msg)) # Returns boolean result

