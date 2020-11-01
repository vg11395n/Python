numbers = [5, 2, 1, 7, 4]
# Append at the end of the list
numbers.append(20)
print(numbers)

# Insert an item at defined index
numbers.insert(0, 10)
print(numbers)

# Remove any number from the list
numbers.remove(5)
print(numbers)

# To clear all the items from the list
# numbers.clear()
# print(numbers)

# Display List
numbers.pop()
print(numbers)

# To print an item at index 2
print(numbers.index(2))

# To find whether the particular number exists in a list or not
print(50 in numbers)

# To count the occurrence of an item
print(numbers.count(5))

# To sort a list in an ascending order
numbers.sort()
print(numbers)

# To sort a list in a descending order
numbers.reverse()
print(numbers)

# To make a copy of a list
numbers2 = numbers.copy()
print(numbers2)

# Task # 1 - Remove duplicates from the list

original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4]
for i in original:
    counter = original.count(i)
    if counter > 1:
        original.remove(i)
    i += 1
original.sort()
print(original)

# or

original2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4]
unique = []

for i in original2:
    if i not in unique:
        unique.append(i)
print(unique)

