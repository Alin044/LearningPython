#indexing = accesing elements of a sequence using []

credit_number = "1234-3345-3523-3423"

print(credit_number[2])
print(credit_number[3:6])
print(credit_number[0::4])

credit_number = credit_number[::-1] #this will reverse the whole string
print(credit_number)

# format specifiers = {value:flags} format a value based on what flags are inserted

price1 = 3.14159
price2 = -9087.65
price3 = 12.34

#.xf  -index decimal precision
# x   -spaces that the value ocupy

print(f"Price 1 is : {price1:.2f}")
print(f"Price 2 is : {price3:.2f}")
print(f"Price 3 is : {price2:.2f}")

print(f"Price 1 is : {price1:.10}")
print(f"Price 2 is : {price3:.010}")
print(f"Price 3 is : {price2:.<10}") #left justified

print(f"Price 1 is : {price1:>10}") #right justified
print(f"Price 2 is : {price3:.^10}") #centered on a number of spaces (10)
print(f"Price 3 is : {price2:+}")  #will add in front of the positive numbers

print(f"Price 1 is : {price1: }")   #space will put them all inlined if there are negative numbers
print(f"Price 2 is : {price3:,}")   #each thousand is separated with a comma (,)
print(f"Price 3 is : {price2:+,.2f}") #u can make combination of flags


#while loops
name = input("Enter your name : ")

while name == "" :
    print("u did not enter your name")
    name = input("Enter your name : ")
print(f"Hello, {name}")


food = input("Enter a food u like (q - to quit")

while not food == 'q' :
    print(f"You like {food}")
    food = input("Enter a food u like (q - to quit")
print("bye")


#for loops
credit_card = "1234-3242-2345-2342"

for x in credit_card:
    print(x)


for x in range(1, 21):
    if x ==13 :
        continue
    else:
        print(x)

for x in range(1, 21):
    if x ==13 :
        break
    else:
        print(x)



















