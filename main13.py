#module = a file containing code you want to include in your program
#         use "import" to include a module (built-in or your own)

#print(help("modules"))

import math

print(math.pi)

import random as r

print(r.randint(1, 10))

from math import pi
print(pi)


import exampleModule

result = exampleModule.pi
print(result)
print(exampleModule.square(3))
print(exampleModule.cube(3))
print(exampleModule.circumference(3))
print(exampleModule.area(3))