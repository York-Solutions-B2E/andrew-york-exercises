# Dictionary: iterable collection of key-value pairs
# pretty much any datatype is an acceptable key or value

pets = {
    "dog": 3,
    "cat": 2,
    "fish": 6
}

# add
pets["bird"] = 1

# modify
pets["dog"] += 5

# delete
del pets["cat"]

# get
for z in pets:              # the keys  (pets.keys() is identical)
    print(z)
    print(pets[z])          # the values

for z in pets.values():     # the values
    print(z)

for z in pets.items():      # the pairs
    print(z)

print("dog" in pets) # <- True
print("orange" in pets) # <- False