# Python 3 Modules - Importing 


# Technically speaking, a module is nothing more than just a Python file containing spceific functions, variables or classes. Of course, these functions and other data types inside a module are not randomly grouped inside that file. They are grouped together to provide some functionality, which can then be used further inside  other programs.
# There are a lot of Python Modules - hundreds, maybe even thousands - that can you can use into your programs. Some of them are default modules, belonging to the Python built-in namespace, and others can be downloaded, unzipped and installed separately.
# You can also create your own modules, meaning you can write some code into a file and use that code further, inside the application you are building, by simply importing the file.
# Now, lets consider the math module, which is a Python built-in module and see its contents, using the dir() function. Also dont forget to import it first, using the import statement.


# import the math module
import math


# Display the contents of the math module
print(dir(math))


# The general rule for accessing module functions and variables when using the "import" statemnt is typing in the name of the module, a dot, and then the name of the function or variable you need to access.
# We can do the same thing , using the math module, to access the value of pi

print(math.pi)

# Remember that if you firget to import the module you need need and try to access one of its variables or functions, you will get a NameError: name 'math' is not defined exception
print(math.pi)

# Now, lets create our own module and see the three ways in which you can import data from within a module.

# I will create two files -> my_module.py and python_app.py

# As we've seen so far, we can use the import statement in order to make use of the code, variables and functions inside a module.

# An important thing to remember here is that when you import a module into your program, Python will automatically execute the code inside that module. 

# This will happen only once, no matter how many times you import that module.


# Lets test this by importing my_module into python_app. Both files are in the same directory, so the module is automatically found by our application.

# As I said, when importing a module for the first time, the code within that module gets executed. So, this time, we got the string printed out by the print() function at the end of the module and then the string printed out by our application. Cool!

# Now, to prove that the code inside the module gets executed just once, let's say that, for some reason, you import that module twice into your application.So, let's go ahead and enter another import statement.

# So, there's the proof! The string printed out by the print() function at the end of the module is displayed just once, even though we have imported the module twice inside our main application.

# Another thing to add here is that now you have all the variables and functions inside my_module available in the namespace of your main program. You can reference and use them by typing in the name of the module, a dot and then the variable or function you need to use.

# Let's test this. I want to print out my_var from within the module and also execute my_function() inside the main application. So, let's add some code at the end of our main file.
# Ok, this was the first way of importing code from an external source, a  module.


# Let's see the second way, now.
# You can use the "from ... import ..." statement to import only some variables or functions from within a module into your application's namespace, thus reducing the resource usage of your program.


# Let's say that from my_module you only need to use the my_var variable into your application, not the entire module.
 
# You can do this very easily, like this



# The last way of importing is using the from import * method, where the asterisk means import all names from within that module. 
# This method is generally not recommended because it overloads the local namespace of the main application you are importing to. So, if you want to import all the names from within a module, you should use the import statement instead.


# The last thing we are going to talk about in this lecture is how to skip the execution of some code when importing a module.
# Let's return to our custom module from earlier and let's say that we don't want to execute the print() function at the end of the file when importing the module into our main application.
 
# We want to keep the print() function inside the module and skip its execution when importing that module.
# For this, we are going to use a trick. Inside the module, we are going to include the code we don't want to be executed at import inside an if block. I will write this first and then I will translate it.
if __name__ == "__main__":
    print("This will be executed")
    
# Now, in our main application file, let's return to the old import statement and add the module name as a prefix to my_var and my_function().

# Returning to our module, the if statement can be translated like this: 

# if this file is going to be executed as a stand-alone program, then go ahead and execute the code below, in addition to the rest of the code inside the module.

# On the other hand, if the file is not going to be executed as a stand-alone application, instead it is going to be used as a module and imported somewhere else, then do not execute the code below the if statement.


# You can access al modules through:
help("modules")
