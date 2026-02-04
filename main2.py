#input() = A function that prompts the user to enter data
#          returns the entered data as a string

import math

# name = input("What is your name?")
# age = input("How old are you?")
# print(f"Hello {name}")
# print(f"You are {age} years old")


#math stuff

x = 3.14
y = 4
z = 5

result = round(x)
print(result)

result = abs(y)   #modul de un numar abs(-4) = 4

result = pow(4, 3)
print(result)

result = max(x, y, z)
result = min(x, y, z)

print(math.pi)
print(math.e)
result = math.sqrt(x)
print(result)

result = math.ceil(x)  #round a number up
result = math.floor(x)  #rounds a number down

radius = float(input("Enter the radius of a circle"))

circumference = 2 * math.pi * radius
print(f"The circumference of the circle id {round(circumference, 2)} cm")

#Aflam ipotenuza unui triunghi drept
a = float(input("Give the lenght of a"))
b = float(input("Give the lenght of b"))

c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"The hipotenuze is : {c}")




