# python 3 Conditionals - if / elif / else

# IN python we have the if, elif, and else statements for decision making.

# Using these statements, python evaluates expressions and runs a piece of code accordingly, meaning, if an expression is evaluated as true, then the code indented below the if statement will be executed. Otherwise python goes futher and evaluates the elif or else statement  and if any.

# Unlike many other programming languages that use curly braces or other delimeters, Python uses indentions to define code blocks, meaning, if, for and while, functions , and classes.

# Using indentation meaning that whitespaces are used as delimiters for code blocks.
# e.g in other language 
# if (condition) {
    # code to excute goes here
# }
# in python
# if codition:
#       code to excute goes here 

# Another thing to remember is that every if /for/while statement or function or class definition, you must use a colon, so that python will know that it should expect an indentedblock right after that statement 

# Now lets start working with if , elif, and else statements

# lets say we define a variable x = 10. And we want to make a decision,based on that value.Maybe the value of x will change at some point during execution of the programm and we want to handle that change in some particular way and run a piece of code.

# Lets use the if statement to excute a block of code, if the expression we provide will be evaluated as true 

x = 2

if x > 5:
    print("x is greater than 5.")
else:
    print("x is not greater than 5")    

x = 4 
if x > 5:
    print("x is greater than 5.")
    print(x * 2)

print("outside the if...")

# Now lets see how to use the else and return to our variable x which is equal to 4.

# lets print "x is greater than 5", if x is indeed greater than 5,and , "x is not greater than 5", in any other case.This accomplished in the following way

x = 4 

if x > 5:
    print("x is greater than 5.")
else:
    print("x is not greater than 5.")    

# The else statement is used to cover all other cases not covered by the if statement above it.So, if the expression following the if keyboard is True, the indented code below it will be excuted. Otherwise if the expression is evaluated as false, the indented below else gets excuted.

# But, what if we want to be more granular and specify more cases and possible outputs in ourprogram? THEN we would use an elif statement 

# Lets say we want to print "x is greater than 5." if x is indeed greater than 5, "x is equal to 5.", incase x is equal to 5 at some point and "x is less than 5", for all other casess.we should then add the elif statement inbtwn the if and else statement 

# the else statement should always be the last in an if/ elif/ else block.

if x > 5:
    print("x is greater than 5.")
elif x == 5:
     print("x is equal to 5.")
else:
    print("x is less than 5.")

     
# Next -> Pyhton 3 loops