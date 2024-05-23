# Pyhton 3 -  Break, continue and  pass

# The break and continue statement are used to handle the flow of a while or for loop in a python program,meaning the programmer can interupt or restart the excution of a loop structure, in certain conditions.

# lets start with the break statement, which is used to terminate the loop in which it resides 

for number in range(10):
    if number == 7:
        break
    print(number)
    
print("hello")   
for number in range(10):
    if number == 7:
        continue
    print(number)
# Now, what if we have a for loop nested inside another for loop
list1 = [4, 5, 6]
list2 = [10, 20, 30]

for i in list1:
    for j in list2:
        if j == 20:
            break
        print(i * j)
    print("outside the nested loop - over here")

# now lets see the continue statement 
#when python stumbles upon a continue satatement inside a for loop or while loop, it ignores the rest of the code below, for the current iteration, goes up to the top of the loop and immediately starts the next iteration

# in order to see this in practice, lets consider the same list for for loop as ealier, but replace break with continue

list1 = [4, 5, 6]
list2 = [10, 20, 30]

for i in list1:
    for j in list2:
        if j == 20:
            continue
        print(i * j)
    print("outside the nested loop")

# Finally, lest talk about the pass statement 

# Pass is equivalent to "do nothing" it is actually a place holder, for whenever you want to leave the addition of a piece of code for later and move on to write other segment of your program.

# lets see a short example of this 

for i in range(10):
    pass
print("hello everyone!")


# Next -> exceptions 