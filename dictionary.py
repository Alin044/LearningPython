#dictionary = a collection of {key:value} pairs ordered and changeable. No duplicates


capitals = {
    "USA" : "Washington DC",
    "India" : "New Delhi",
    "China" : "Beijing",
    "Russia" : "Moscow"
}

print(dir(capitals))
print(help(capitals))

print(capitals.get("USA"))

if capitals.get("Japan"):
    print("That capital exists ")
else:
    print("That capital does not exist")


capitals.upadte({"Germany" : "Berlin"})
capitals.uptad({"USA": "Detroit"})
capitals.pop("China")
capitals.popitem() # will remove the last inserted item

keys = capitals.keys()
print(keys)

for key in  capitals.keys()
    print(key)

values = capitals.values()
print(values)
for value in capitals.values():
    print(value)

items = capitals.items()
print(items)
for key, value in capitals.items():
    print(f"{key} : {value}")

print(capitals)
capitals.clear()
