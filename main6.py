#nested loops

rows = int(input("Enter the number of rows : "))
columns = int(input("Enter the number of columns : "))
symbol = input("enter the symbol to use : ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()


# colection
# lists
# sets
# tuples

fruits = ["apple", "orange", "banana", "coconut"]
print(dir(fruits))
print(help(fruits))

print(len(fruits))
print("apple" in fruits)

fruits[0] = "pineaple"
fruits.append("mango") #to add an element to the end of the list
fruits.remove("apple")
fruits.insert(0, "pineapple")
fruits.sort()
fruits.reverse()
#fruits.clear()
print(fruits.index("apple"))
print(fruits.count("bannana"))



print(fruits)
print(fruits[0])
print(fruits[1])

print(fruits[0:3])
print(fruits[::2])
print(fruits[::-1])

for fruit in fruits:
    print(fruit)

#sets = {} unordered and imutable,but add, remove ok. no duplicates
fruits1 = {"apple", "orange", "banana", "coconut"}

fruits1.add("pineapple")
fruits1.remove("apple")
fruits1.pop() #removes the first element but its random
#fruits1.clear()
#fruits1.add("coconut") u cant add duplicates

#Tuple = () ordered and unchangeable. Duplicates ok, faster

fruits2 = ("apple", "orange", "banana", "coconut")
print(len(fruits2))
print(fruits2.index("banana"))
print(fruits2.count("coconut"))

for fruit2 in fruits2:
    print(fruit2)


