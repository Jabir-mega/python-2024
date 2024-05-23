 # Python 3 lists - Introduction 

#  what is list?
# A list is, actually, a sequence consisting of elements separeted by comma
# The sequence of element is enclosed by square brackets.
# you can have any data type as elements of a list - strings, numbers, tuples, or even other lists and a list may have any number of elements 

# similary to strings, which can be regarded as sequence of characters, lists are indexed meaning each element has a certain position inside the list, starting at 0.

#  You can also use the "len()"" function to see the number of elements in the list and slices to extracta portion of the list 

# as opposed to strings lists are mutable meaning that you can modify a list by adding or removing elements 

# lets create our first list, we will name it list1 and will be iniatially empty 
# in order to have empty list you have to type the square brackets and thats it nothing else needed 
list1 = []

#  to check that this is indeed a list lets use the old type() function on list1
print(type(list1))
#  now lets add some elements to our list 

list1 = ['cisco', 'juniper', 'avaya', 10, 10.5, -11]

# so now we have a list with some string and numbers as elements

# lets remember the len() function from strings section and use it on our list1

print(len(list1)) # returns 6
# Now, lets see how we access elements inside the list
# Well, the same as we did with characters inside string using index so:

# Access the first element
print(list1[0])  # returns 'cisco'
# Access the third e;ement 
print(list1[2]) # returns 'Avaya' 
# Access the last element from right to left
print(list1[-1]) #returns '-11'
# Access thte 2nd last element from right to left
print(list1[-2])#returns '10.5'

#  As with strings, if we enter an invalid index we will get an "indexerror" in return, stating that the list is out of range i.e
# print(list1[100])

# To check that the lists are indeed mutable, lets try to replace an element in the list.
# We still have list1 in memory, so, list[2] will return 'avaya' element Now lets replace it with another vendor, say 'HP'
print(list1)

list1[2] = "HP"

print(list1)

# Plain simple, this is how you can update  a list. Just type in the name of the variable and in btwn the square brackets, you have to insert the index at which you want the replacement to be made. 
# Finally following the equal sign, just enter the new element and thats it you are good to go 

# python 3 lists - methods 
#  Now its time to see how to handle lists and lists element and what tools does python provide for this.

# We've already seen the len() function being used on a list. but what if you want to find out the max and min value within the list? well you have the max() and min() function for that

#  consider list2 
list2 = [-11, 2, 12]

# min value
print(f"The minimum value in '{list2}' is {min(list2)}")

# max value
print(f"The maximum value in '{list2} is {max(list2)}")

# What about a list of strings
list3 = ['a', 'b', 'c']

# min element 
print(min(list3)) #returns  'a' -> every letter has an interger assigned to it 

# max element
print(max(list3)) #returns  'c'  -> every letter has an interger assigned to it 

# However, if we have a list with various types of elements, say numbers and strings mixed together, like list1 , how does python compare a string with and interger and return the maximum value in the list1 

list1 = ['cisco', 'juniper', 'avaya', 10, 10.5, -11]

# list1 = [1, 2, 3, 'a', 'b', 'c']
# print(min(list1)) # returns-> TypeError: '<' not supported between instances of 'int' and 'str'

# Now lets check the available methods we have at hand 

#  First, we should learn how to append(add) a new element to a list 
# its simple, we have list1 

# to append an element to a list just use the append() method 
list1.append(100)

print(list1)

# Now lets remove an element from our list.we have three options for this 

# 1 =>First we can use the 'del' command 
del list1[4] # where 4 is the index of the element we want to remove
print(list1)
      
# 2 ->Another way to remove an element by its index is using pop() function 
list1.pop(0)# removes the first element 
print(list1)

#  The third way is actually remove an element  by specifying the element itself using remove() method
list1.remove('avaya')
print(list1)

# Now lets see how we can add an element at aparticular index in the list .This is accomplished by using the insert() method

list1.insert(2, 'naima') #the element at the second index is pushed to the third index --> in our case '-11' is pushed to the 3 index     and                       'naima' placed in the second index   

print(list1)

#  A nother interesting list operation is appending a list to another list 
# lets say we have 
list2 = [9, 99, 999]

# To add the elements of list2 to list1, we can use the extend() method
# lets see both list first
print(list2)
print(list1)

# Now we can just exyen list 1 with the content of list2 like this
list1.extend(list2)

print(list1)

# Now, remember the index() count() methods from strings Python makes them available for lists as well. So lets find the index of an element in our lists and how to count the occurence of an element in the list

# consider list1
print(list1)
print(list1.index(-11))# returns 3

# lets append the value 10, thus having this value thrice in the list
list1.append(10)
list1.append(10)

print(list1)

# count the occurence of 10 --> 3
print(list1.count(10))# returns 3

# Now lets have a look at ways of sorting the elements of a list

# 1 -> First,we can use the sort() function
# So returning to list2, lets add a couple elements firts
list2.append(1)
list2.append(25)
list2.append(500)

print(list2) 

# Now we want to have them sorted in Ascendind order. simply amply the sort()function method on list2

list2.sort()

print(list2)

#  What if want the element to be sorted in reverse or descending order ? well we have the reverse() method for this 
list2.reverse()
print(list2)
print(";)")
# The two method above are modfying the list in place, meaning that after you apply the method there is no other list created - you have the same list, only that the element are displayed in a specific order 

# T o sort the element of the list and create a new list in memory at the same time you have a new method called sorted() function available.
sorted_list= sorted(list2)
print(sorted_list)
print(";)")

print(list2)

# if you want to use the same function, sorted(), to reverse the order, just add an argument inside th paranthesis . the argument is called reverse and it must have the value True assigned to i t
print(sorted(list2, reverse = True))

# TWO more things worth mentionig here.
# You can concatenate or repeat a list, as you did with strings, using the plus and multiplication operators, so:

# conctenation
print(list1 + list2)

# Repetition
print(list2 * 5)
# Tomorrow -> list Slices 

#  Remember, list slices allow us to extract various parts of a sequence. We already used them to  slice strings and in many ways all the rules applying to string slicing also applys here

#  the general syntax is

# Type the name of the variable pointing to that list followed by square bracjets,  next, in btwn the bracjets, we have a colon, on the left side of the colon we can specify the index at which to start slicing, then , the slice will go upto , but not including the index specified on the right side of the colon 

#  having said that lets create a new list and do a couple of list slices 

list3  = [1, 2, 3, 'a', 'b', 'c']

# lets extract the first three elements of the list 

print(list3[0:3])

# Another way to extract the first three elements of the lists would be 

# not to specify the first index in btwn the brackets 
print(list3[:3])

# [3, 'a', 'b']
print(list3[2:5])
# ][3, 'a', 'b', 'c']
print(list3[2:])
# [[1, 2, 3, 'a', 'b', 'c']
print(list3[:])

# use -ve indexes
# [3, 'a', 'b']
print(list3[-4:-1])
# ['a', 'b' , 'c']
print(list3[-3:])
# [1, 2, 3]
print(list3[-6:-3])
# [1, 3, 'b']
print(list3[::2])
# # ['c', 'b', 'a', 3, 2, 1]
list3.reverse()
print(list3)
# print(list3[-1:-6])

# Next -> Sets 