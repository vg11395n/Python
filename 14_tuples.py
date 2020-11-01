# We can't modify tuples. Tuples are immutable.

numbers = (1, 2, 3)

print(numbers.count(1))

print(numbers.index(2))

# Unpacking
coordinates = (1, 2, 3)
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]

w = x * y * z

# Below syntax is same as assigning single item of tuple to a variable in sequential manner
x, y, z = coordinates
print(x)
print(y)
print(z)