# Python 3 Nesting - if/ for / while

# You can use nesting with control flow statements like , if, for, and while, to enable a acertainbehaviour and logic insideyour python programm .
# Think of nesting asusing an if statement inside anotherif statement, a for loop inside another for loop, or a while loop within another while loop.

# lets use some basic example, to see what i mean

# First, lets refer to if statement and code 

# When nesting an if statement inside another if statement, we are actually telling python that the indented code below the nested  if statement  should be executed only if both the inner statemeny and outerr statement  are evealuated as True. lets see what i mean by that 

x = "cisco"

if "i" in x:
    if len(x) > 3:
        print(x, len(x))

# this code is actually thesame thing as using the 'and' logical operators btwn the two expression

if ("i" in x) and (len(x) > 3):
    print(x, len(x))

# Now, lets have a look at a nested for loop
# Lets assume we have two lists and we want to multiply each elemnt of the first list by each element of the second list. For this, we should iterate over both lists at the same,take each elemnt into account, do the multiplication and return the result.

# lets write this and we discuss it afterwards

list1 = [4, 5, 6]
list2 = [10, 20, 30]

for i in list1:
    for j in list2:
        print(i * j)


# Lets say that after doing the multiplacation we did for each element of list1, we want to also print that element of list1, just to have it printed out after each iteration    

list1 = [4, 5, 6]
list2 = [10, 20, 30]

for i in list1:
    for j in list2:
        print(i * j)
    print(i)

# Now lets write a nested while structure and then we analyze it as always

x = 1
while x <= 10:
    z = 5
    x = x + 1
    while z <= 10:
        print(z)
        z += 1

# the result is 5 6 7 8 9 10, printed out 10 times ...
# the first while loop does the same thing as it did before. it checks weather x is less than or equal to 10, and ...........


# The lats thing i'll add here is nesting structures inside a diff structure. so, lets try nesting an if statement inside a for loop, as an example

for number in range(10):
    if  number <= 5:
        print(number)

# Next -> Break, continue, pass

    