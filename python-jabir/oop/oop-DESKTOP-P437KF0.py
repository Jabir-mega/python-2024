# objects and classes

# Apart from what we have seen until now, python also has an object oriented approach to programming.

# Upto to this point we have seen one way of programming using functions()

# Object oriented programming is based on classes, objects and methods(functions).

# in short as a definition-> a class is a data type containing its own variables, attributes and functions (which are called methods in oop)

# stardard definition of a class  would tell a class is like a blue print/template for  creating objects 

# An object may be regarded as an instance of a defined class and the attributes values for a particular object define the state of the object.

# An object is a real world entity

# Another term that is very much used when it comes to or discussing classes is inheritance.
# This means that a new class may inherit all the names and functionalities from an exsisiting class.
# We will talk about inheritance later

# Inorder to properly define a class you will use the class keyword, then type in the class name.

# Now, be carefull here because the convention is to use camelcase for class names. This means each word in the  name of the class willl be capitalised and no spaces are allowed

# Actually, except the camelcase rule, all the rules regarding variables and function name apply to class names, as well

# SO, lets name our class simply MyRouter

# After the name of the class, in btwn parenthesis, you should type in the word "object", all lowercase.

# This is the new style of defining classes, starting with python 2.2
# The thing you should keep in mind here is, that if a class deosnt inherit from another class, then you should always type in the word object inside parenthesis, when defining a class

# This is a default  setting and it means that this class inherits from a default class name object

# I know this may seem confussing, so, we wont get into anymore details on this topic

# Just dont forget to add that word, object

# So we have class MyRouter(object)  then as for any other blocks of code we've seen  so far, we'll type in a colon 

# class MyRouter(object):

# On the next row using one level of indentation, we shall input the content of that class.

# As with functions on the first row fter the class definition you can type in a documentation string or docstring in btwn quotes, to provide a hint about that class functionality.

# So lets enter some text in double quptes 

# class MyRouter(object):
#     "This is a class that describes the characteristics of a router"
    
# Following the optional docstring the first thing you define inside a class is the special  __init__()method, also called a class constructor

# The word init will be preceeded and followed by double underscores.This is the way python identifys a special method

# The role of __init__is to innitialize some variables and the method is called whenever we create a new instance of the class in which it resides.

# Actually it is the first code  that is executed whenever you create a new instance of the class 

# Any special methods or regular method within the class is defined using the def keyword just as in regular functions

# The difference here is that each time you define a method inside a class, the first parameter inside the paranthesis is self  

# You have to remmeber to always input this word as the parameter of  every class method. 

# self is no more than just a reference to the current instance of the class.

# Now after typing in self, you define any other parameter that you want to be defined and initialized whenever you create a new instance of the class in which it resides 

# In our case we want to define some parameters that characterisedour router, so we will add router name, model, serialno, ios 

# Now,lets define the object or instance attributes we need to describe the router, according to the parameter of the __init__method

# Remember  that self is used to point out that we are reffereing to the current instance of the class 

# The next lines of code will again be indented under the definition of the __init__method
# thats how you define object attribute

# Now, lets also define a new method inside the class that will do nothing more than just print out the attribute and concatenate the model of the router with manufacturing date.

# The definition of this new method will sit at the samelevel of indentation as definition of the __init__ method 

# Notice that self is again inserted as the first parameter

# You should do this every time you define a method inside a class

# Next, inside the method again indenting our code on elevel to the right we enter the print() function we need

# Now lets see what the deal with the objects we talked about

# An object is actuallyy an instance of the class

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
         print("The router is:", self.rotername)
         print("The router model is:", self.model)
         print("The serial number is: ", self.serialno)
         print("The ios version: ", self.ios)
         print("The model and date combine is : ", self.model + manuf_date)
         
         
# Now. lets create create our first object
router1 = MyRouter('R1', '2600', '123456789', '12.4')

# print(router1)

# Indeed we see that we created an object and python confirms it

# Now what can you do with this object?

# First you can access each of its attributes lets see how
print(router1.rotername)
print(router1.model)
print(router1.serialno)
print(router1.ios)

router1.print_router('23-04-2024')

# second object
router2 = MyRouter('L2', '1260', '2453678', '17.5')

# Access the attiributes 
print(router2.rotername)
print(router2.ios)
print(router2.model)
router2.print('2019-5-20')

# you can also change an attribute of an object like this 

router2.ios = '50.5'
print(router1.ios) 
print(router2.ios) 

# or you can use the setattri() method to change the attribute

setattr(router1, "ios", "20.2")
setattr(router2, "ios", "10.2")
print(router1.ios) 
print(router2.ios) 


# python also provides some function to play around with object attributes
# First we have the getattr() for getting the value of an attribute
# lets use it on both routers

print(getattr(router2, "ios"))
print(getattr(router1, "ios"))

# Finally you can use the hasattri() to check whether an object attribute exists or not -> Returns either false or True 
# 
hasattr(router2, "ios")
    
# Finallty you can delete an attribute using delattri()
# delattr(router2, "ios")

# print(getattr(router2, "ios"))

# if you try to access ios it will the error below
# returns Error : AttributeError: 'MyRouter' object has no attribute 'ios'



# We can also verify if an object is an instance of a particular class 
# This is useful especially when you  have multiple classes and objects created and you want to keep track of them 
# lets see this in action for router2

print(isinstance(router2, MyRouter)) #-> Returns True

# In heritance
# When creating a new class you should type in the word object btwn the parenthesis when defining a class 
# we can say the new class inherits from the default class called object but for the sake of modularity and the DRY best practice which stands for Dont Repeat yourself 
# We can also create a class that inherits the attributes and methods from an already existing class 
# This iscalled inheritance 

# The Two classes create a parent - child relation
#To tell python that you want to inherit from acertain class you type in the class name in btwn the parenthesis

#Lets see this using the old MyRouter classes we created acting as the parent 
# Lets create a new class called MyNewRouter

# class MyNewRouter(MyRouter):


# When defining a new class that inherits from a exisisting class and not the default object class you can skip the init since the new class inherits everything

# But when you want to add extra attributes to this class you will redefine the constructor and  tell python you want all the attributes in the parent class to be availble in the child class  as well and then enter the new attribute

# Like this

class MyNewRouter(MyRouter):
    def __init__(self, routername, model, serailno, ios, portsno):
        MyRouter.__init__(self,routername, model, serailno, ios) 
        self.portsno = portsno
        
# EXP :
# After defiing the new class and putting the parent class btwn the parenthesis we definined the class constructor and specified the parameter in the brackets as they were defined in the parent class and then we added a new parameter "portsno" at the end. on the next row we called the init constructor of the parent class by typing the parent class name MyRouter then a dot then theinit method having the same parameters in btwn the paranthesis in other words we imported the init method attribute from the parent class.

# Finally we defined the new attribute specific to the child class


# Next lets define an additional method inside the child class that simply concatenates a stringas an argument when calling the method and the value of the model attribute inherited from the parent 