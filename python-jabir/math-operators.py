# python 3 - math operators

# pythons defines three numerical types namely 
# -> intergers
# -> floating-point numbers 
# -> complex numbers 

#  the complex numbers are usually used in some advanced  math operation and are of not great interest for our current needs instead we will work alot with intergers and floating-point numbers and thats why we will forcus on these two numerical types and there corresponding operators and functions. 

#  lets define a variable and assign an interger and another variable associated with a floating-point number or float 
#  consider the following variables: 
num1 = 10  # interger
num2 = 2.5  # float

#  check the type of this variables -> of course python provides the type() function for this
print(type(num1)) # returns <class 'int'> 
print(type(num2)) # returns <class 'float'>

#  lets dee what operation we are able to perforn using itergers and floating-point numbers 

# 1.arithmetic operators  I.E
x = 20
y = 6

#  you can do : 
#  1  addition -> '+'
print(x+y)
#  2  subtraction -> '-'
print(x-y)
#  3  multiplication -> '*'
print(x*y)
#  4  division -> '/'
print(x/y)
#  5 interger division  -> '//' (returns the interger(whole number) of  a division )
print(x//y)
#  6  modulus -> '%' (this means finding out the remeinder after the division of a number by another)
print(x%y)
#  7 rasing by a power -> '**' 
print(x**2)

#               / challenge time 
#  write a python program that asks the user the radius of a circle and returns the perimeter and area of the circle 
#  define pie 
PI = 22/7 
#  ask the user for the radius
radius = float(input("enter radius "))

#  compute the perimeter of the circle 
perimeter = PI * (radius + radius)

# //compute the area 
area = PI * (radius * radius)
# area = PI * (radius ** 2)
# output the result in a nice format 
print(f"the perimeter and area of a circle whose radius is {radius}cm, is {perimeter}cm, and {area}cm\u00b2 , respectively ")

print(f"dollar sign:\u0024 ")

# 2. comparison operators -> used to compare values and returns Boolean values (true or false)
x = 20
y = 6

# less than -> '<'
print(x < y)
# greater than -> '>'
print(x > y)
#  less than or equal to -> '<='
print(x <= y)
#  greater or equal to -> '=>'
print(x >= y)
#  equals to -> '=='
print (x == y)
# not equal to -> '!='
print(x != y)

# order of evaluation in python 
#  lets talk about the order of evaluation for these operators inside a mathematical expression 
#  what if  we have to deal    with multiple operators within the same expression ? which operators have apriority over others 

# well the order is as follows
# 1. raising to a power has the highest priority 
# 2. then we have multiplication, division, and modulo operations withn equal priorities. and lastly 
# 3. we have addition  and substraction, also with equal properties 
# lets use an example 
100 - 5 ** 2 / 5 * 2 
100 - 25 / 5 * 2 
100 - 5 * 2 
100 -  10
90

#                            conversion 
# lets see how we can an interger to a float and vice-versa 
# well, python has two function available for these operation. lets see them 
print(int(1.7))  # returns 1 due to truncation
print(int(19.9999)) # returns 19 becoz of truncation
# the result is one becoz the the int() function will round down the number in btwn the paranthesis to the nearest interger which is 1 

print(float(2)) # returns 2.0
# the result is 2.0 the float() function will add .0 converting 2 from interger to a floating-point number 

# finally 
# lets have a look at a few functions which may come in handy in the fututre when working with numbers 
# 1. abs(); returns the absolute value . this is actually the distance btwn the number that we provide and zero 

print(abs(5)) # returns  5 
print(abs(-15)) # returns 15

# 2, max() : returns the largest number btwn 2 numbers 
print(max(2,10)) # returns 10

# 3, min() : returns the smallest number btwn 2 numbers 
print(min(2, 10)) #returns 2

# 4, pow() ; another way of raising a number to a power using built in python function 
# e.g pow(a, b) where a is the base number and b is the exponent 

print(pow(10, 3)) # returns a thousand 

#                       challege timez
# write a python program that prompts the user to enter there name and age the programm will than output the decades and the minutes the user has lived 
# a decade is 10 yrs e.g if you are 22 yrs  you have lived 2 decades 

#  ask theuser for name 
user_name = input("what is your name? ")
# aske the user for age 
user_age = int(input("what is your age? "))

# compute decades lived (DL)
decades = user_age // 10

# convert user_age into minutes lived (ML)
age_in_minutes = user_age * 365  *  24 * 60 

# output 
print(f"Hello {user_name}, you have lived for {decades} decade, and {age_in_minutes} minutes, which means you are {user_age} years old.")

#  next -> python 3 Booleans - logical operators   /
 
