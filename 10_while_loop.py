# while loop:
# while condition:
#    statements to be executed

i = 1
while i <= 5:
    print('*' * i)
    i += 1
print('Done')

guess_num = 0
guess_count = 3
number = 9
while (guess_num < guess_count):
    guess = int(input('Guess a number '))
    guess_num += 1
    if guess == number:
        print('You Won!')
        break
else:
    print('Sorry, you failed!')

# Task #1: Car Simulation Program

started = False
stopped = False

command = ""
while command != "quit":
    command = input("> ").lower()
    if command == "start":
        if started:
            print("What you doing car already started!")
        else:
            started = True
            print("Car Started! Let's go!")
    elif command == "stop":
        if not started:
            print("What you doing car already stopped!")
        else:
            started = False
            print("Car Stopped! You can get down!")
    elif command == "help":
        print('''
start - to start the car
stop - to stop the car
quit - to quit the menu
        ''')
    elif command == "quit":
        break
    else:
        print("Enter correct command!")
