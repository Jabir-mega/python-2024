#  Python 3 sets - introduction 

#  WHta is a set? you may ask yourself ?

# Well a set is basically an unordered collection of unique elements.

# Generaly speaking you may regard sets as being lists that have no duplicate elements.

# Lets see how we create a set. in fact there are two ways 

# The first way is by using the set() function which is a built in function 

# To also prove that sets do not allow duplicate lets create a list with a duplicate lements and apply the set() function on it

list4 = [1, 2, 3, 4, 5, 2, 3 ]
print(list4)
print(type(list4))
set(list4)   
#   convert the list to a set 
print(set(list4)) # returns {1, 2, 3, 4, 5}
print("Look here")
# you see that the set() removes the duplicate  element in list4 which is avery usefull feature to have at hand 

# We can also directly create a set by passing a raw sequence to the set() like a string or list and referencing the result using a variable

set1 = set([11, 12, 13, 14, 15, 15, 15, 11])
print(set1)
print(type(set1))

# The second way to create a set is to use the {} braces this method of creating a set is available in version of python starting with 2.7 according to www.python .org

set2 = {11, 12, 13, 14, 15, 15, 15, 11}

print(set2)
print(type(set2))
print("over here")
# you can also find out the NO of elements in a set, using the same len() function, aswe did with strings and lists 
print(len(set2)) # returns 5

# cheking weather an element is or not a member of a set is also possible  using 'in' and 'not in' keywords
print(11 not in set2)# returns False
print(11 in set2) # returns True
print(16 not in set2) # rteturns True 

# We have  to remeber that sets are mutable, so we can add or remove elements from a set in the following manner 

# Adding an element to a set -> add() method 
set2.add(16)
print(set2)
# remove an element from a et-> remove()
set2.remove(13)
print(set2)


set2.add(16)
set2.add(16)
print(set2)

# Notice that if you try to add an element which already exists in the set, python  will not agree with you, although no error wll be returned it just doesnt add it.

# lets see some operation andmethods that can be applied on sets

# pyhton3 sets -  methods

#  TO better understand set methods and operations lest create two sets first

set1 = {1, 2, 3, 4}
set2 = {3, 5, 8,}
print(set1)
print(set2)
#  python defines some methods for identifying the simmilarities or diferences btwn two sets of elements but also other methods to better make use of this data types lets see them in action  

# First lets see how we can identify the common elements of the two sets defined
# To do this,we can use the intersection() method, like this 

print(set1.intersection(set2))
print(set2.intersection (set1) )
# now lets which elements does set1 have and set2 doesnt 

print(set1.difference(set2))
print(set2.difference(set1))

# to unify the two  sets you can use the union() method and the result also being a set will include element three just once. So do not confuse the union of sets with concatenation
print(set1.union(set2))
print("look here")
# Another thing you can do is to remove a random element in the set is by using the pop() method,
print(set1.pop())# returns the element removed from the set 
print(set1.pop())# returns the element removed from the set 
print(set1)
print(set1)
# Finally you can clear a set using the clear() method 
set1.clear()
print(set1) #returns set() to indicate an empty set 
print({}) #returns an empty dictionaries 
print(type({}))# returns class dictionary
print(type({1}))# returns a class set 

# next -> tuples