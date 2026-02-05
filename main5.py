#countdown timer in python

import time

time.sleep(3) #waits for a certain amount of time
print("Time's up")

my_time = int(input("Give a amount of seconds"))

for x in reversed(range(0, my_time)):
    print(x)
    time.sleep(1)

for x in range(my_time, 0, -1):
    print(x)
    time.sleep(1)

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int((x / 60) % 60)
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)