# Positional Parameters:
def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print("Welcome aboard")


print("Start")
greet_user("John", "Smith")
print("Finish")


# Keyword Parameters:
def greet_user2(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print("Welcome aboard")


# Note we passed last name first in below argument but since we are using keyword arguments,
# it will still prints first_name and last_name
print("Start")
greet_user2(last_name="Smith", first_name="John")
print("Finish")