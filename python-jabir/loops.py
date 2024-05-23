# Python 3 Loops - For loops 

# For loop

# The for statement is used whenever you want to iterate(repeate) over a sequence and excute a piece of code for all or some of that sequence - lists or strings, or whatever you have

# Lets start with an example of repeating or looping over a sequence and first, lets define a list 

vendors = ['Cisco', 'HP', 'Notel', 'Avaya', 'Juniper']

# Now lest see how we can work with a for-loop

# First, you'll notice that there are some similarities to the if/elif/else syntax, meaning that the colon is again used to signal that an indented code block folows the for statement, so speaking about indentetion, we must indent the code inside a for-loop

# Syntax
# We start by typing the for keyword, then we enter the repeating variable, which is a user-defined temporary variable. so you can name it however you like, then we type in the 'in' keyword, to tell python tahat we are going to repeat over the sequence following this keyword and, finally we enter the sequence itself, followed by a colon. 
vendors = ['Cisco', 'HP', 'Notel', 'Avaya', 'Juniper']

for each_vendor in vendors:
    print(each_vendor)
    
# We can also repeate over a string
my_string = "Cisco"

for letter in my_string:
    print(letter)
    print(letter * 2)
    print(letter * 3)

#  Now its time to see how to use a for-loop to repeate over a range. Remember the range datatype that can be used to generate an iterator over which we can repeate and then extract some values.

# Lets consider a range starting at zero and going upto but not including, 10, with the default step of 1. That would return the interger 0 to 9 in ascending order.

# Lets create this range
my_range = range(10)

# Now lets use a for-loop to repeate over this range
for i in my_range:
    print(i)

# output -> 1 2 3 4 5 6 7 8 9
# Challenge -> output this-> 0 2 4 6 8 10 12 14 16 18
for i   in my_range:
    print(i * 2)
    
# Now lets see a more common use of the range() function inside a for statement. What if we want to repeate over a list using list indexes? what do i mean by that? Okay, we still have the vendors list in memory.

print(vendors)

# Now lets remeber the len()function. lets apply itto our list.
print(len(vendors)) #returns 5

# we know that rannge(5) returns the intergers starting with 0 upto but not including 5. Moreover we can convert this range  to a list using list() function. Lets do this
print(list(range(5))) #Returns [0, 1, 2, 3, 4]

# We can look at the element of the list as being the indexes of each element of our list, vendors. So element 'cisco' would be positioned at index 0 and so on.

# This means that if we want to get a list of indexes to repeate over , using the for-loop, we can use range(len(vendors))
print(range(len(vendors)))

# For now lets create a for-loop that prints out each element of the vendi=ors list by its index

# Challenge
for index in range(len(vendors)):
    print(vendors[index])

# wonder
x = 1 
# syntax for a while loop
# to create a while loop, you have to type in the while keyword, followed by the condition you want to evaluate and then a colon. Below, after indentation you will specify the code to be excuted as long as the condition is evaluated as true.

while x <= 10:
    print(x)
    x = x + 1 # x += 1 or x++

# Another way to work with while loops is by using an expression as true, in order to make python do something over and over again untill you tell it to print.

# A great example would be an interactive menu, where the user can select a value and execute a piece of code, then return to the main menu and so on.

# The way to do this is by simply using "while True:", which makes sure that the expression always evaluated as true.

# the syntax for this would be:
# while True:
    # do something ....

#output -> 0 2 4 6 8
y = 0
while y >= 16:
    print(y)
    y =y + 2
print("=====" * 20)
# output -> 60 45 30 15 0 -15 -30 -45 -60
x = 60
while  x >= -60:
    print(x)
    x= x - 15

print("=====" * 20)

# often you will see for loops within other loops - same thing with 'if' and 'while' statement. you will also need to use 'if' statements inside 'for' loops or ;while; lopps, depending on what you are trying to achieve in your programs.
# Next we are going to take a look at this kind of structures called nested structures.


# Next -> Nested Structure 