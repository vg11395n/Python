# Use single quotes for normal string variable
single_quote = 'Python for beginners!!'
print('Print using single quotes: ', single_quote)

# Use Double quotes if we have apostrophe in string variable
double_quotes = "Python's course for beginners!!"
print('Print using double quotes: ', double_quotes)

# Use Triple quotes if we have multiple lines of string variable
triple_quote = '''Hi John,
This is a tutorial for multiline string variable
Thank you!!
Sincerely,
Support Team'''
print('Print using triple quotes: ', triple_quote)

# [0]
# To print first character of the str variable we use square bracket and 0 as the starting address
single_quote = 'Python for beginners'
#               012345678910
print('Print first character of the string: ', single_quote[0])

# [-1]
# To print last character of the str variable we use square bracket and -1 as the starting address
single_quote = 'Python for beginners'
#                             -3-2-1
print('Print last character of the string: ',single_quote[-1])

# [-2]
# To print second last character of the str variable we use square bracket and -2 as the starting address
single_quote = 'Python for beginners'
print('Print second last character of the string: ',single_quote[-2])

# [0:5]
# To print first 5 characters but NOT the 5th character of the str variable we use square bracket and 0:5 as the range
single_quote = 'Python for beginners'
#               012345
print('Print first 5 characters of the string: ',single_quote[0:5])

# [0:]
# To print all the characters  from the beginning of the str variable we use square bracket and 0: as the starting index
# We DO NOT supply ending index
single_quote = 'Python for beginners'
#               012345
print('Print all the characters of the string from the beginning: ',single_quote[0:])

# [:5] = [0:5]
# To print the characters up to specific index let's say 5th of the str variable, we use square bracket and :5 as the ending index
# We DO NOT supply ending index
single_quote = 'Python for beginners'
#               012345
print('Print first 5 characters of the string: ',single_quote[:5])

# [:] means all the characters, mostly use to clone/copy variable
# To print all the characters of the str variable, we use square bracket and : operator and no indexes
single_quote = 'Python for beginners'
#               012345
print('Print all the characters of the string from the beginning: ',single_quote[:])

# if we want to clone single_quote variable into another variable e.g. course we use the same operator
course = single_quote[:]
print('Print all the characters of the string from the beginning but using CLONED variable: ',course)

# Task #1: Play with indexes

name = 'Jennifer'
# This syntax will print all the characters from the 1st index to last index BUT EXCLUDE THE LAST INDEX as there is a minus sign
print(name[1:-1])
