#  python 3 - Variables 

#  what is a variable? how to  define a variable? what is it good for, in python

# a variable is nothing more than just a reserved location in your computers memory used to store info ~ values to be more precise. this means that when we create a variable you reserve some space in memory.

# you canstore diffenrent types of data using a variable ~ you can store a string , a number, a list or other data type you can think of.

# unlike other languages in python you dont have to explicitly declare a variable - instead, the declaration is done automatically when you assign a value to that variable,na matter what type of data you decide to assign to that memory location
# e.g. String username = "Dennis"; in alanguage like java 
# in python -> username = "dennis" 

#  futhermore, you can later access the value referenced by that variable and use in other areas of your python program.

# / lets think of how you should properly name a variable in python     
# / there are several rules considered for a clean and compliant code andalso for avoiding any conflict with python's in-built names.set

# 1- A variable name should always start with a letter, usually lowercase and never strat with a number or a symbol. However there is an exception to this rule -> some variable start with an underscore '_', or double underscore '__', but these are python specific structure, so lets leave them to python.

# the variable name may contain lowercase or uppercase letters, numbers, and the underscore, but as i said , not as the first character 

#  Also do not include spaces or any other special characters inside names.

# / AND remember python name s are case sensitive, so a variable named 'my_Var' is a different variable from 'my_var', with a lowerase 'v'

# Another thing about variable names is that they should keep a reasonable name length, so that it will be easier for you to remember it and reference it inside your code.

# the last thing is that there are some python reserved names, which you can use as a variable name example; def, if, break, return, list, str, while, for

#  lets see  how we can assign a value to a variable 

#  The rule is to use the equall sign '=', -> this should be regarded as an assignment operator rather than the usual equal sign used in math

# in the left side of the equal sign you type the variavle name and in the right side you type the value you want to assign to that variable 

# it doesnt matter if you leave a space btwn each side of the equal sign. Actually it is better to leave a space on each side of the equal sign for a clean code 
num1 = 7 # recommended 

#  You ae also able to do multiple assignment, so you can assign  a value to multiple variables, at the same time.  The syntax for this would be :
a = b = c = x = y = 10
print(a)
print(b)
print(c)
print(x)
print(y)

# Also,you can assign a diff value for each variable within the same line of code, like this :
a, b, c = 10, 20, 30

print(a)
print(b)
print(c)

# Next -> Data types 