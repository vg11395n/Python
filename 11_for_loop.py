# For loop:
# for iteration in condition:
# for iteration in range (starting iteration, ending iteration, increment by)

# Display total of a List

prices = [10, 20, 30, 40, 50]
total = 0
for price in prices:
    total += price
print(f"Total: {total}")

# Nested Loop

# Display co-ordinates
# (x, y)
# (0, 0)
# (0, 1)
# (0, 2)
# (1, 0)
# (1, 1)
# (1, 2)

for i in range(4):
    for j in range(3):
        print(f"Co-ordinate: ({i} ,{j})")

# Using nested loop draw below shape 'F'

#   xxxxx
#   xx
#   xxxxx
#   xx
#   xx

number = [5, 2, 5, 2, 2]
for x_count in number:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)


# Other method
for i in range(5):
    if i in (0, 2):
        print('x' * 5)
    else:
        print('x' * 2)



