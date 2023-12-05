counter = 0
total = 0

def increase_counter():
    counter = counter + 2

for i in range(1,5):
    increase_counter()

print(counter)

# Function will not be able to affect counter variable because it's not in scope
# If you want global variables to be affected by a function you have to explicitly include them (global keyword)
# Functions can use / affect global variables but cannot REASSIGN them unless explicitly pointed at them
# e.g. 

list2 = []
def addHello():
    list2.append("Hello")

def increase_counter(amt):
    global counter # this line must precede any use of this variable in this function
    counter += amt

    # As written this function does not have any local variables. It is only messing with the global "counter"

# LØØPS
# break kills the loop early
# continue ends current iteration and progresses to next one

while counter < 1000:
    counter += 1
    if(counter % 5 == 0):
        continue            # next line will run EXCEPT when preceding line is true, in which case stop and go to next iteration
    if(counter == 201):
        break               # as soon as preceding line is true, loop is terminated altogether
    total += counter

# If you write an infinite loop, keyboard interrupt keyboardinterrupt force quit by click the terminal and ctrl+c