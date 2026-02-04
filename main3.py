# if statements

# age = int(input("Enter your age : "))
#
# if age >= 18:
#     print("You are now signed up")
# elif age < 0:
#     print("U havent been born yet")
# else :
#     print("Try again")
#


#one line conditional statements
num = 5

print("Positive" if num >= 0 else "Negative")

result = "Even" if num % 2 == 0 else "Odd"
print(result)

#string methods

phone_number = input("Enter your phone number : ")

result = phone_number.count("-")

name = input("Enter your name : ")
result = name.find("a")
result = name.rfind("P")
name = name.capitalize()
name = name.upper()
name = name.lower()
result = name.isdigit()
result = name.isalpha()

phone_number = phone_number.replace("-", " ")
print(phone_number)

auf = input("type 1 if u need information about the str methods and 0 if not")

if int(auf) == 1:
    print(help(str))
else :
    print("ok")

#Exercise
# validate user input exercise
# username is no more than 12 characters
# username must not contain spaces
# username must not contain digits

username = input("Enter a valid username to continue : ")

if len(username) > 12 :
    print("Username if to long, it must contain at most 12 chars")
elif not username.find(" ") == -1 :
    print("Your username can not contain spaces")
elif not username.isalpha() :
    print("Your username can not contain digits")
else:
    print("Welcome to the site " + username)





