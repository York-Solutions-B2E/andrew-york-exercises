import math

# print(type(1.0))
# temperature = int(2.999999999)
# print(temperature)
# temp2 = int(round(2.9))
# print(temp2)
# temp3 = math.trunc(3.566612)
# print(temp3)
# temp4 = str(temp3)
# print(type(temp4))
# print(round(1/3, 2))

temperatures = [20, 23, 24, 23, 21, 19, 22]

## Bad way to loop through this. Counter does not track index
# day = 0
# for temp in temperatures:
#     print("Temp on day", str(day), "is", str(temp))
#     day = day + 1
# print("Done")

## Gooder
# for i in range(len(temperatures)):
#         print("Temp on day", i + 1, "is", temperatures[i])
# print("Done")

## range loops 3 args: start, end, step
# for i in range(0, 5, 1) -> 0, 1, 2, 3, 4
# for i in range(3, 12, 2) -> 3, 5, 7, 9, 11

## range is an object! 
taco = range(0, 55, 2)

## if you pass 2 args they are start and end. step will be default (1)
## if you pass 1 arg it is end. start will be default (0)

## enumerate takes something normally iterable and adds a counter
for i, temp in enumerate(temperatures, 0):
    print ("day " + str(i) + " temp " + str(temp))

## does the same thing as
# for temp in temperatures:
#   print(temp)
## but includes that counter
## can be as many variables as you want???

## slicing
# myList[:] -> everything
# myList[0:2] or [:2] -> first two
# myList[5:] -> fifth item to end
## negatives count from end

## Conditionals
ages = [1, 12, 14, 18, 22, 36, 44, 66, 90]

categories = []
for user_age in ages:
    if user_age < 13:
        categories.append("child")
    elif user_age < 20:
        categories.append("teenager")
    elif user_age < 65:
        categories.append("adult")
    else:
        categories.append("senior")
print(categories)

def categorize_age(age, name):
    if user_age < 13:
        category = "child"
    elif user_age < 20:
        category = "teenager"
    elif user_age < 65:
        category = "adult"
    else:
        category = "senior"
    print(name, "is", age, "years old, making them a", category)
    # return category

print(categorize_age(55, "Dave"))

list1 = [1,2,3,4,5]
print(type(list1))
print(type(list1) == list)