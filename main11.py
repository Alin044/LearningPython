#List Comprehension = A concise way to create lists in python

doubles = [x * 2 for x in range(1, 11)]

tripes = [y * 3 for y in range(1, 11)]
print(doubles)
print(tripes)


square = [z * z for z in range(1, 11)]
print(square)

fruits = ["apple", "orange", "banana", "coconut"]
fruits = [fruits.upper() for fruit in fruits]
print(fruits)

numbers = [1, -3, 5, -23, 54]
positive_num = [num for num in numbers if num >= 0]
print(positive_num)


