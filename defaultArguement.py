# default arguments


def net_price(list_price, discount = 0, tax = 0.05):
    return list_price * (1 - discount) * (1 + tax)

price = net_price(500, 0, 0.05)
print(price)

import time
def count(start, end):
    for x in range(start, end+1)
        print(x)
        time.sleep(1)
    print("Done")

count(0, 30) 
