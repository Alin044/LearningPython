#Concession stand program

menu = {
    "pizza" : 3.00,
    "nachos" : 4.00,
    "hod-dog" : 2.50,
    "popcorn" : 1.50,
    "chips" : 3.49,
    "soda" : 2.25,
    "pepsi" : 2.20,
    "lemonade" : 3.00
}

cart = []
total = 0

print("--------Menu----------")
for key, value in menu.items():
    print(f"{key:10} : ${value:.2f}")

print("----------------------")

while True:
    food = input("Enter an item to order (q to quit) : ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print(cart)

print("--------Your order--------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")
print()

print(f"Total is : {total:.2f}")
