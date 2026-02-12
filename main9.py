# *args = allows u to pass multiple non-key arguments
# **kwargs = allows u to pass multiple keyword arguments
# * = unpackging operator
#1. positional , 2. default, 3. keyword , 4. arbitrary


def print_adress(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

print_adress(street="123 Fake street",
             city="Detroit",
             state="Michigan",
             zit="23532")


def shiping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    # for value in kwargs.values():
    #     print(value, end=" ")
    print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('state')}, {kwargs.get('zipcode')}")


shiping_label("Dr.", "Spongebob", "Squarepants", "III",
              street="123 Fake street",
              apartment="Apt 234",
              city="Detroit",
              state="Michigan",
              zipcode="23532")