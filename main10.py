#Membership operators = used to test whether a value or a variable is found in a sequence
#                       (string, list, tuple, set or dictionary)
#                        1. in
#                        2. not in


word = "apple"

letter = input("Guess a letter in the secret word: ")

if letter in word:
    print(f"There is {letter}")
else:
    print(f"Letter {letter} not found")

students = {"Spongebob", "Patrik", "Sandy"}
