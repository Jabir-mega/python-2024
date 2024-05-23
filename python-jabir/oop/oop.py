# objects and classes

# Apart from what we have seen until now, python also has an object oriented approach to programming.

# Upto to this point we have seen one way of programming using functions()

# Object oriented programming is based on classes, objects and methods.

# in short as a definition-> a class is a dattype containing its own variables, attributes and functions (which are called omethods in oop)

# stardard definition of a class  would tell a class is like a blue print/template for  creating objects 

# An onject may be regarded as an instance of a defined class and the attributes values for a particular object and define the state of the object.

# An object is a real world entity

# Another term that is very much used when it comes to or discussing classes is inheritance.
# Rhis means that a nest class may inherit allt he names and functionalities from an exsisiting class.
# We will talk about inheritance later

# Inorder to properly define a class you will use the class keyword, then type in the class name.

# Now, be carefull because the convention is to use camelcase for class names. This means each word in the  name of the class willl be capitalised and no spaces are allowed

# Actually, escept the camelcase rule, all the rules regarding variables and function name apply to class names, as well

# SO, lets name our class simply MyRouter

# After the name of the class, in btwn parenthesis, you should type in the word "object", all lowercase.

# This is the new style of defining classes, starting with python 2.2
# The typing you should keep in mind here is that in a class deosnt inherit from another class, then you should always type int he word object inside parenthesis, when defining a class

# This is a difuclt setting and it means  that this class inherits from adefault class name object

# I know this may seem confussing, so, we wont get into anymore details on this topic

# Just dont forget to add that word, object

# So we have class MyRouter(object)  then as for aby other blocks of code we've seen  so far, we'll type in a colon 

# class MyRouter(object):

# On the next row using one level of indentation, we shall input the content of that class.

# As with functions on the first row sfter the class definition you can type in documentation stirng or docstring in btwn quotes, to provide a hint about that class functionality.

# So lets enter some text in double quptes 

# class MyRouter(object):
#     "This is a class that describes the characteristics of a router"
    
# Following the optional docstring the first thing you define inside a class is the special  __init__()method, also called a class constructor

# The word init will be preceeded and followed by double underscores.This is the way python identifys a special method

# The role of __init__is to innitialize some variables and the method is called whenever we create a new instance of the class in which it resides.

# Actually it is the first code  that is executed whenever you create a new instance of the class 

# Any special methos or regular method within the class is defined using the def keyword just in regular functions

# The difference her eis that each itme you define a method inside a class, the first parameter inside the paranthesis is self  

# You have to remeber to a;ways input this word as the parameter of  every class method 

# self is no more than just a reference to the current instance of the class.

# Now after typing in self, you define any other parameter that you want to be defined and initialized whenever you create a new instance of hte class in which it resides 

# In our case we wnt to define some parameters that characterisedour router, so we will add router naem, maodel, serialno, ios 

# Now,lets define the object or instab=nce attributes we need to describe the router, according to the parameter of the __init__method

# Rename that self is used to point out that we are reffereing to the current instance of the class 

# The next lines of code will again be indented under the definition of the __init__method
# thats how you define object attribute

# Now, lets also dedine a new method inside the class that will do nothing more than just print out the attribute and concatenate the model of the router with manufacturing date.

# The definition of this new method will sit st the same level of indentation as definition of the __init__method 

# Notice that self is again inserted as the first parameter

# You should do this every time you define a method inside a class

# Next, inside the method again indenting our code on elevel to the right we enter the print() function we need

# Now lets see what the deal with the objects we talked about

# An obkect is actuallyy an instance of the class

# You can create as many objects as you want, by simply calling the class name and eneterung the argument required by the __init__method, in btwn paranhtesis- all of them, except self, ewhich is automatically passed by oython.


class MyRouter(object):
    "This is a class that describes the characteristics of a router"
    def __init__(self, routername, model, serialno, ios):
        self.rotername =  routername
        self.model = model
        self.serialno = serialno
        self.ios = ios
    
    # a method to print the router properties)
    def print_router(self, manuf_date):
         print("The router is:", self.print_router)
         print("The router model is:", self.model)
         print("The serial number is: ", self.serialno)
         print("The ios version: ", self.ios)
         print("The model and date combine is : ", self.model + manuf_date)
         
         
# Now. lets create create our first object
router1 = MyRouter('R1', '2600', '123456789', '12.4')

print(router1)

# Indeed we see that we created an object and python confirms it

# Now what can you do with this object?

# First you can access each of itd attributes lets see how
print(router1.rotername)
print(router1.model)
print(router1.serialno)
print(router1.ios)

router1.print_router('23-04-2024')