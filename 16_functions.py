# Functions
def greet_user():
    print("Hi There!")
    print("Welcome aboard")


print("Start")
greet_user()
print("Finish")


# Task # 1 - Convert the emojis program into function

def emoji_converter(message):
    words = message.split(' ')
    emojis = {

        ":)": "😃",
        ":(": "😢",
        ";)": "😉"
    }

    output = ""
    for i in words:
        output += emojis.get(i, i) + " "
    return output


message = input("> ")
print(emoji_converter(message))
