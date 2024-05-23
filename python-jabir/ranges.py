# python 3 Ranges -> introduction

# in this lecture we will have a brief look over the range type and, to make things even more interesting, we will start with a quick comparisso with the meaning of 'range' in the previous major version of python, namely Python 2.

# for this wew will open up codeskulptor.org, which is online python 2 interpreter and we will use the range() function by passing the value 10 as an argument 

# In Python 2, what range() does is, it generates a list of intergers, starting at 0 and going up to but not including, the value 10.

# As you can see, the range() function has a default starting point at 0 and a defalt step of 1, since we get these consecutive intergers returned
# print(range(10))

# But dontworry, these can be customized, for example, lets start our list at 5, instead of 0 to do this we just have to enter a new argument, also called start, in btwn paranthesis
# print(range(5, 10))

# python 3 methods 

# Ok following up on the previous example, lets gett into the python 3 interpreter and see how does range work() behave in here

# lets consider basic below

r = range(10)

print(r) # returns range (0, 10)
print(type(r)) # returns <class 'range'

# you can easily notice that, unlike in python version 2, where we would've got a list returned, in python 3, range gets its own data type, class 'range'

# However, if you want a list instead of a range object, you can simply apply the list() function to this range 

print(list(r))


# what else can we do with range 

# you can use indexes, as we did with strings or lists, to extract elements from this range for instance 

print(r[0]) # returns 0

print(r[-1])# returns 9

#  You can also verify if a certain value is a member of the range, by using the 'in' and 'not in' keywords 
print(10 in r) # returns False 
print(7 not in r)#returns False 

# moreever, you can apply, for instance the index() method to find out the index of acertain element of therange 
print(r.index(4))#returns 4

# Finally keep in mind that you cannot slice a range, but what you can do is you can convert the range to  a list, using the list() function, and then apply your slice.for instance
print(list(r))
print(list(r[2:5]))

# Pyhton 3 Dictionaries - Introduction
