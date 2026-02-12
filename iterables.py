#Iterables = An object/collection that can return its elements one at a time,
#            allowing it to be iterated in a loop

numbers = [1,2,3,4,5]

for number in reversed(numbers):
    print(number, end="-")


numbers = [1,2,3,4,5]

for number in numbers:
    print(number)

fruits = {"apple", "orange", "banana", "coconut"}  #sets are not reverseble

for fruit in fruits:
    print(fruit)


name = "BroCode"

for character in name:
    print(character, end="-")

my_dictionary = {
    "A" : 1,
    "B" : 2,
    "C" : 3,
    "D" : 4
}

for key, value in my_dictionary.items():
    print(f"{key} : {value}")