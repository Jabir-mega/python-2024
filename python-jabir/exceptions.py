# Python 3 -> exceptions 


# In Pyhthon you may encounter two main types of errors-> syntax errors and exceptions

# A syntax error occurs when you dint follow pythons syntax and maybe you forget to add a colon, or the indentation is not proper

# lets tyr this and skip the colon following a for statement on purpoose 

#  for i in range(10)

# We got SyntaxError as expexted. This is an example of an error in python.

# Now lets talk about exceptions

# Unlike syntax errors, exceptions areraised during the executionof the programm, interrupting the normal flow of the application.

# Letsv see a couple of example

# First, lets use the same for loop to generate one of the amny types of exceptions, called NameError

# I will misspell the name of the range () function and wait for python to notice my mistake 
# for i in rnge(10):
#     print(i)

# NameError:  name 'rnge' is not defined. Did you mean: 'range'?
# The above means either i misspelled a word in the code, in this case the name of a function, or the variable you are trying to use is not yet defined in my namespace.

# Another type of exception raised when trying to divede a number by 0

print(4 / 0)

# ZeroDivisionError: division by zero
# Fair enough, we cannot divide a number by zero, so Python raises a special exception for that particular case 

# There are many types of exceptions in python.we wont analyze all of them becoz we will likely encounter most of them as you start creating and troubleshooting your own real programs.

# However you can find a comprehensive lots of python 3 exceptions below->
# https://docs.python.org/3/tutorial/erros.html
# https://docs.python.org/3/library/exceptions.html

# Next -> pthon 3 functions '-'basics