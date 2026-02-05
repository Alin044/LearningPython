
fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["pork", "beef", "chicken"]

groceries = [fruits, vegetables, meats]

print(groceries)
print(groceries[0])
print(groceries[1])
print(groceries[2])

for colection in groceries:
    print(colection)

for colection in groceries:
    for food in colection:
        print(food, end=" ")
    print()


#num pad with tuple

num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()
