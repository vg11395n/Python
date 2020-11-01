# Information is stored as a Key-Value pair

customer = {
    "name": "John Smith",
    "age": "30",
    "is_verified": True
}

print(customer)

# Access values of dictionary
print(customer["name"])

# If Key is not defined and we can add a new key-value pair to the dictionary
print(customer.get("birthdate", "Jan 1 1980"))

# Update value of existing key
customer["name"] = "Jack Sparrow"
print(customer["name"])

# Task # 1 - We enter a value in digits and then program should translate it to words
# e.g. Phone: 1234 >>> Translate it to one two three four

phone = input("Phone: ")
digits_mapping = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)

# Task # 2 - Map Characters into a smiley faces
# e.g. if I type I am happy :) should translate last characters :) to a smiley face

message = input("> ")
words = message.split(' ')
emojis = {

    ":)": "😃",
    ":(": "😢",
    ";)": "😉"
}

print(words)
output = ""
for i in words:
    output += emojis.get(i, i) + " "
print(output)



