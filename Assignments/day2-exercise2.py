# Create a function that gets a list of numbers, and returns the sum of all positive ones.
def sumPositivesFromList(listArg):
    if type(listArg) != list:
        print("Argument must be a list. Exiting function")
        return
    sum = 0
    for x in listArg:
        if type(x) != int and type(x) != float:
            print("Function only accepts numbers. Exiting function")
            return
        else:
            if x > 0:
                sum += x
    return sum

list1 = [1,2,3,4,5]
list2 = [5,10,15,-10,-5]
list3 = "potato"
list4 = ["potato", 5, 10, -1]
print("*** Function sumPositivesFromList ***")
print("List 1:", list1, ":", sumPositivesFromList(list1))
print("List 2:", list2, ":", sumPositivesFromList(list2))
print("List 3:", list3, ":", sumPositivesFromList(list3))
print("List 4:", list4, ":", sumPositivesFromList(list4))

# Create a function that takes a boolean value and returns a "Yes" for true and "No" for false
def isTrueBool(input):
    if type(input) != bool:
        print("Boolean values only. Exiting function")
        return
    elif input:
        return "Yes"
    return "No"

    # return "Yes" if input else "No" <- also works in Python

print("*** Function isTrueBool ***")
print("True", isTrueBool(True))
print("False", isTrueBool(False))
print("Potato", isTrueBool("Potato"))

def isTrueAny(input):
    if bool(input):
        return "Yes"
    return "No"

print("*** Function isTrueAny ***") 
print("True", isTrueAny(True))
print("False", isTrueAny(False))
print("Potato", isTrueAny("Potato"))
print("None", isTrueAny(None))
print("4.1", isTrueAny(4.1))
print("0", isTrueAny(0))
print("0.0", isTrueAny(0.0))
print("[0]", isTrueAny([0]))

# Create a function that when given a list of numbers returns the smallest number in the list.
def smallestNumberInList(listArg):
    # error handling
    if type(listArg) != list:
        print("Argument must be a list. Exiting function")
        return
    for x in listArg:
        if type(x) != int and type(x) != float:
            print("Function only accepts numbers. Exiting function")
            return
    
    # function
    target = listArg[0]
    for x in listArg:
        if x < target:
            target = x
    return target

list5 = [90, 5, 22, -15, 0, 222]
list6 = [3, 2, 1, 4, 5]
list7 = [2, 2, 1, 1, 2, 1, 0]
list8 = [0.5, 0.6, 0.2]

print("*** Function smallestNumberInList ***")
print("List 1:", list5, ":", smallestNumberInList(list5))
print("List 2:", list6, ":", smallestNumberInList(list6))
print("List 3:", list7, ":", smallestNumberInList(list7))
print("List 4:", list8, ":", smallestNumberInList(list8))

# Create a function that calculates the average of the values in a list
    # (omitting error handling going forward)
def getAverage(listArg):
    sum = 0
    for x in listArg:
        sum += x
    return sum / len(listArg)

list9 = [1, 2, 3, 4, 5]
list10 = [55, 123, 53, 201]
list11 = [-24, 1, 0, 55]

print("*** Function getAverage ***")
print("List 1:", list9, ":", getAverage(list9))
print("List 1:", list10, ":", getAverage(list10))
print("List 1:", list11, ":", getAverage(list11))

# For every number from 1 to 20 do the following:
    # if the number is a multiple of 3, print "Fizz"
    # if the number is a multiple of 5, print "Buzz"
    # if the number is a multiple of both 3 and 5 print "FizzBuzz"
    # Otherwise, just print the number

print("FizzBuzz 1-20:")
for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print(i, ": FizzBuzz")
    elif i % 3 == 0:
        print(i, ": Fizz")
    elif i % 5 == 0:
        print(i, ": Buzz")
    else:
        print(i)