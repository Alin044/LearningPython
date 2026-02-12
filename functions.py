#functions

def happy_birthday(bro):
    print("Happy birthday!")
    print("Happy birthday to you!")
    print("Happy birthday, dear friend.")
    print(f"Happy birthday {bro}")

happy_birthday("Alin")

#return
def add(a, b):
    return a + b

print(add(2, 3))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

print(create_name("isil", "karahan"))