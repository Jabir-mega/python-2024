# python 3 Tuples

#  you can consider tuples as being immutable lists, meaning there contents cannot be changed by adding, removing, replace elements 

# Tuples may prove to be useful when you want to store data in the form of a sequence and keep that data untouchable 

# However unlike sets, tuples are ordered collections of non-unique elements, meaning indexes and duplicates are allowed 

#  lest create our first tuples

# Tuples are enclosed by parentheses (round) and there elements are separeted by commas 

my_tuple = ()

# check the type
print(type(my_tuple)) # returns <class 'tuple'>

#  If you want to create a tuple with a single element you have to use a trick meaning that, although you have only one element inside the tuple you have to write a cooma after it, ottherwise it will not be regarded as a tuple 

my_tuple = (9)
print(type(my_tuple)) #returns <class 'int'>

my_tuple = (9,)
print(type(my_tuple))#returns <class 'tuple'>

# Now you have a tuple set up.you should always remember this when creating tuples having only one element 

# Next, lets populate our tuple with more element 
my_tuple = (1, 2, 3, 4, 5)

# Just like string and list tuples support indexing, so if you want to access an element within a tuple the indexing rule are still applicable.

# A ccess the first element 
print(my_tuple[0])

# Access the last element 
print(my_tuple[-1])
print(my_tuple[4])

# Since tuples are immutable you cannot modify an element of a tuple.
# let check it 
# my_tuple[0] = 10 # returns -->TypeError: 'tuple' object does not support item assignment

# Also removing removing element is not permitted when working with tuples 
# del my_tuple[0] # returns -->TypeError: 'tuple' object doesn't support item deletion

# Another thing you can do with tuple is tuple assignment. This means you can assign a tuple of variables to a tuple of values and map each variable in the first tuple to the correspom=nding  value in the second tuple

# lets see this as well 
# lets define tuple1  with the following elemets
tuple1 = ('cico', '2600', '12.4')

# And now lets assign a tuple of variable to tuple 1
(vendor, model, ios) = tuple1

# Finally lets check if theassignment and variable-to-value mapping have been properly assigned
print(vendor)
print(model)
print(ios)

# THis is also called tuple packing and unpacking and you can see it as a kind of mapping btwn elements of different tuples.

#  An important thing to remeber is that both tuples should have same number of elements. otherwise if you have different number of elements a value error will be returned. 

# tuple2 = (1, 2, 3, 4)
# (x, y, z) =  tuple2 #ValueError: too many values to unpack (expected 3)
# print(x)
# print(y)
# print(z)

# You can also assign in a tuple to a avariable in another tuple within a single statement, which is even more convinient 
(a, b, c,) = (10, 20, 30)
print(a)
print(b)
print(c)

# tommorow set operation and mthods 

# python 3 sets ->methods 


tuple2 = (1, 2, 3, 4)

#  check the number of items in the tuple -> len() function 
print(len(tuple2)) #returns 4

# also we have the min() and max() function available for finding the lowest and highest element 
# value in tuple
print(max(tuple2)) #returns 4
print(min(tuple2))# returns 1

# we can also concatenate and multiply a tuple using the old plus and multiplication 

# tuple concatenate 
print(tuple2 + (5, 6, 7))# returns (1, 2, 3, 4, 5, 6, 7)

# tuple multiplication
print(tuple2 * 4)# returns (1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4)

# since indexing applies to tuples as it does to strings and lists, slicing is also possible with tuples 
print("OVER HERE")
# lets seee a couple of examples without entering into detail in slicing simce the rules are basically identical
print(tuple2)
# (1, 2)
print(tuple2[:2])
# (1, 2)
print(tuple2[0:2])
# (2, 3, 4)
print(tuple2[1])
# (1, 2, 3, )
print(tuple2[:3])
# (1, 2, 3, 4)
print(tuple2[:])# or [0:]
# -ve 

# (1, 2)
print(tuple2[-4:-2])
# 3, 4
print(tuple2[-2:])
# (4, 3, 2, 1)
print(tuple2[::-1])
# tuple2.reverse()
# print(tuple2)
# (1, 3)
print(tuple2[::2])

# Another thing you can doo with tuple is you can check if an element is a memeber or not using 'in' or 'not in' 

print(3 in tuple2) # returns True 
print(3 not in tuple2)# returns False
print(5 in tuple2) #returns False

# last thing on tuples -> we can ue del command to delete a whole tuple 

del tuple2
print(tuple2)# name error :name tuple2 is not defined

# next -> python ranges - intronduction 