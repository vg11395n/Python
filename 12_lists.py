# Lists:

name = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr']
print(name[0])
print(name[-1])
print(name[-2])
print(name[2:4])

# Find the largest number from a List

number = [12, 34, 67, 678, 89, 12, 42, 134, 78, 31, 89]
largest = number[0]

for number in number:
    if number > largest:
        largest = number
print(f"Largest Number : {largest}")

# 2D Lists:

# [
#    1 2 3
#    4 5 6
#    7 8 9
# ]

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# print(matrix[0][1])

for row in matrix:
    for item in row:
        print(item)