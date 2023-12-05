import math

temperatures = [20, 16, 19, 21, 15, 22, 20]

# 1. Find the sum of all temperatures.
print("Sum of temperature list:", sum(temperatures))

# or
sum = 0
for x in temperatures:
    sum = sum + x
print("Sum of temperature list:", sum)

# 2. Find the average temperature
print("Average temperature (mean):", sum / len(temperatures))

# 3. Create a range object that will cover all numbers divisible by 3 that are bigger than 14 and smaller than 100.
# sloppy:
thisRangeObj = range(15, 100, 3)
for x in thisRangeObj:
    print(x)

# better:
RangeObj2 = range(math.ceil(14/3)*3, 100, 3)

# 4. Create a list slice that gets all but the last four items in a list
print(temperatures[:-4])

# 5. Create a boolean expression that changes depending on the inclusion of parenthesis!
print(False and False or True)
print(False and (False or True))