# Pthon 3 Functions -> Basics

# This is a very complex and diverse topic

# This is a core topic in python, and in anyother programming language
# we are going to use functions alot to build applications

# before anything, What is a function?
# Well you can use function to organise your code in blocks that can be later reused. This is helpful if you want better readibility of your code, modularity and also time saving when designing and running your code

# Before we starting writting code rememeber that functions follow the same syntax rules as other structures that we have seen but also add some features that we are going to anaylze 

# First a function is defined using the "def" keyword followed by the name of the function, then a pair of paranthesis and then a colon,After the colon, on the next row you will type in the code you want to store in this function indented one level to the right,as we did with 'if' or 'for' statements.

# Lets see this 

def my_first_function():
    "This is my first function!"
    print("Hello Python!")

my_first_function()
# So, as said before, we have the def keyword, the name of function, my_firdt_function, then the parantheses, and finally the colon. THis is how you define a function

# one important thing to remember here is that in btwn the parantheses you can specify one or several parameters for the functions. We will see how to do that in a comment.

# Until then, lets further study our function definition

# After the colon, which signals the start of an indented block, we type in the code we want thus function to excute - indented, of course.

# Notice that on the first row inside the function a string has been typed in. This is a docstring and its role is to describe function. However it is entirely optional - maybe you can use it when you define complex functions with complex applicaton, to remember the role of the function and how it is connected to other segments of your programme 

# You can access the docstring by using the help() command

print(help(my_first_function))


# Now, i said earlier that functions are usuable blocks of code.lets see why

# After definning a function with or without any parameters inside the parantheses, we can call that function whenever we need to run the code inside it.

# in order to call a function you just need to type in that functions name followed by the parantheses and thats it.I.E

my_first_function()
my_first_function()
my_first_function()

# Another advantage of functions is that you can change the code within a function and see the results changing, as weell,the next time you call that function
# So we can functions -are dynamic structures

# Lets redefine our function and change the code in=nside it then on the next call the result should reflect the update we've just made 

def my_first_function():
    print("Hello java!")

my_first_function()

# okay, now lets talk abit about parameters and argument and the diffference btwn the two concepts

# Lets modify our existing function and insert our first parameter into the picture Remember parameters are written inside the parantheses

# lets see how they work

def my_first_string(x):
    print(x)

my_first_string("My World!")

# so in this case, x is passed as a parameter to the function and then used inside the code within the fuction. This means that whenever we're going 
# to call the function and pass an argument of our choice to the function, that arguments will be further passed to the code inside the function

# Asa side note - keep in mind the terminologys 

# parametrs are the one wriiten inside paranthesis when defining the function

# Argument are the ones written inside parantheses when 'calling' the function.

# Most of the time, they are used interchangeably, but you should try to follow and use this terminology, though.

# For now, lets returnto our function and call it by passing an argument to the function cal.


# my_first_function("Hello Everyone!")

# So what we did is we called our function and told python to use the string inside the parantheses as an argument.then, the string was passed to print() function and finally printed out on the screen.

# You can also enter multiple parameters within a function defifniton like this :

def my_first_function(x, y):
    print(f"hello {x}")
    print(f"Hello {y}")

# S0 according this piece of code, we expect that calling the function and passing two strings as argument inside the paranthesis, they will both be printed out, preceeded by the "hello" string lets see it

my_first_function(" python", "jave" )

# Notice that x was mapped to "python"  and y was mapped to "jave"  becoz that was the order we used when pasing the arguments. pretty intuitive, i think 

# Now we are gooing to touch on another topic and that use  the "return" statement 

# This statement is used to exit a function  and return something when the function is called 

# lets create a new function and see how the return statement works, lets me write this first.

def add_two_numbers(x, y):
    sum = x + y

# So we have created a variable inside our function, that will reference the result of adding x and y, which are the functions parameters lets see if our function returns something when we call it. 
add_two_numbers(3, 7)

# So nothing is returned thats becoz we haven't specfied what exactly we are lookin to get back from the function

# the function in its current form does nothing more than creating a variable name sum  and storing the result of adding 3 and 7 
 
# However it doesnt return anything it keeps the result secret, for now. That why we need the return statement

# lets see how to use it

def add_two_numbers(x, y):
    sum = x + y
    return sum 

print(add_two_numbers(3, 7))
result = add_two_numbers(23, 27)
print(result)

# so this time we told python to return the value stored by sun and we got the expected resukt in return

# We  can change the function even more and call it by using another set of arguments.

# lets add another parameter z, change the expression inside the function and then return the value of sum squared 

def add_two_numbers(x, y, z):
    sum = (x + y) * z
    return sum ** 2

print(add_two_numbers(1, 2, 3))

# The last thing to add is that if you just use the return statement without specifying what exactly do you want to get out of the function pyton will return the 'none' value. So,'return' without specifying what to return is, actually, the same thing as return None. Lets test this
def greet_user(name):
    greeting = f"Hello, {name}!"
    return

print(greet_user("Jabir"))

# challenge time
# create a python programm using 5 or 4 functions that asks the user for their name and age. Then the programm should output the user info in a nice format displaying the name, age, decades lived, and age in second that the user has lived.


# a function to get the name of the user
def user_name():
    name = input("Please enter your name: ")
    return name

# a function to get the age of the user 
def user_age():
    Age = int(input("Enter your age too: "))
    return Age

# a function to compute the user age in decades
def user_decades():
    age =  user_age() // 10
    return age 

# a function to compute the user age in seconds
def user_age_in_seconds(age):
      seconds = age * 365.25 * 24 * 60 * 60
      return seconds
# function to display the user info
def display_user_info():
    name = user_name()
    age = user_age()
    decades = user_decades()
    age_in_seconds = user_age_in_seconds(age)
    print(f"Hello {name}, you have lived for  {decades} decade, {age_in_seconds}seconds,  which means you are {age} years old.")


#  call the display_user_info() here    
display_user_info()

# create a function that takes in a list of intergers and then returns the smallest odd interger in that list
#  create a function that takes in a list of intergers and then returns the smallest odd interger in that list
# solution
def smallest_interger(number_list):
    odd = []
    for number in number_list:
        if number % 2 == 1:
            odd.append(number)
    # return min(odd) 
    odd.sort() # sorts the lists in an ascending order 
    return odd[0] # selects the first element/interger


print(smallest_interger([12, 40, 45, 30, 20, 23, 40, 37, 37, 7, 17]))