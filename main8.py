import random

# print(help(random))

low = 1
high = 100

number = random.randint(low, high)
print(number)

numberRand = random.random()

options = ("rock", "paper", "scisors")

option = random.choice(options)
print(option)

cards = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
card = random.shuffle(cards)
print(card)





