# Python 3 Dictionaries ->

# This is another important data type in python 

# A dictionary is an unordered set of 'key-value' pairs, separeted by comma and enclosed by curly braces 

# they are very useful for storing info in aspecific format.for instance, considering a router, you can store data about the device in the following format:
# {'vendor': 'cisco', 'model' : '2600', 'ios', : '12.4', 'ports' : 4}

# dictionaries are mutable- which means we can modify their content using dictionary specific procedures.Why do i say dictionaries-specific? Because, unlike strings or lists, dictionaries are indexed by the position of each element, like we previously h ad zero for first element ,and so on 

# Dictionaries sre indexed by key. The key is the value on the left side of the colon of each key-value. as we will see

# For now lets create empty dictionary

dict1 = {}

print(dict1) # returns {} -> empty dictionaries 

# check the the type of dictionary
print(type(dict1)) # returns <class 'dict'>

# This is how you create an empty dictionary
# lets add some data 

dict1 = {'vendor': 'cisco', 'model' : '2600', 'ios' : '12.4', 'ports' : '4'}

# lets notice afew things:

# First, becoz the keys in the dictionaries are actually strings, each key is enclosed by quotes.This may be the most widely spread data type used for a dictionary. You may also use a number as a key, in order to have some kind of numbering system ,like this :

d1 = {1: 'first Element', 2: 'Second Element', 3: 'Third Element'}

# okay lets get back to our dictionary

# A key thing to remeber here is that each key in the dictionary must be unique and should be of an immutable type -> this means strings, numbers or tuples as keys but  not lists

# On the other hand, values dont have to be unique and can be either mutable or immutable data type 


# python 3 dictionaries - methods 

# Lets consider 'dict1'

# First, lets extract the corrosponding value for a specific key. This can be done similarly to accessing elements inside a list , only that you dont specify an index. we specify the associated key for the value we want to extract.

print(dict1)

# output 12.4
print(dict1['ios'])
print(dict1.get('ios'))
# Remember, we said that dictionaries are mutable.
# So lets try to add a new value to our dictionary. This is done by simply assigning a new value to  the new key 
# 'RAM' : '128'
dict1['RAM'] = '128'
print(dict1)

# change IOS  to 15.8
dict1['ios'] = '15.8'
print(dict1)

# We can also delete a pair from the dict using del command  -> delete key :'ports'

del dict1['ports']
print(dict1)

# Next, remeber the len() function  from strings, lists and tuples we can use it here as well. To find out the number of key-value pairs inside a dictionary
print(len(dict1)) # returns 4 

# We can verify if a certain string is a memeber in our dictionary or not like

print('IOS' in dict1) # returns False
print('IOS' not in dict1) # returns True 

#Now, there are three important methods to deal with keys and values in a dictionary

#  1 ->The first method is keys(). This method is used to obtain a list having the keys in a dictionary as element 
print(list(dict1.keys()))

#  2 -> The second is called value(), this method is used to obtain a list having the values in a dictionary  as elements 
print(list(dict1.values()))

# 3 -> The last one is called item(),returns list of tuples, each tuple containing the key and value of each dictionary pair. lets check this out 
print(list(dict1.items()))

# challenge time

# 1. create  a list of "person" in dictionaries with a name , age and list of hobbies for each person. fill in any data you want 
persons =[ {  'name' : 'jabir', 
              'age' : '18', 
              'hobbies' : ['games']
           },
           {   'name' : 'jackson', 
              'age' : '20', 
              'hobbies' : ['football', 'cooking', 'swimming']
           }, 
           {'name' : 'pedro',
            'age' : '20', 
            'hobbies' : ['jogging', 'eating']
           }
 ]

print(persons)

#  output: "jackson likes cooking  and pedro loves eating"

print(f"{persons[1]['name']} likes {persons[1]['hobbies'][1]} and {persons[2]['name']} loves {persons[2]['hobbies'][1]}")
print(f"{persons[1]['name']} likes {persons[1]['hobbies'][1]} and {persons[2]['name']} loves {persons[2]['hobbies'][1]}")

# 2. a-> create a python dictionary with keys a, b, and c having lists as values of the keys, 1-10, 11-20, and 21-30 respectively
dict2 = {'a': list(range(1,11)), 'b': list(range(11,21)), 'c': list(range(21,31)) }
print(dict2)
# 2. b -> from the above dictionary access elements 13 and output it
print(dict2['b'][2])

# create a python that captures the name and list of 5 subject scores and then stores that info to a dictionary.the program then outputs the average scores of the students .


# ask for the students name
student_name = input("what is your name ")
print(student_name)


# ask for tthe students score subject as a variable in each subject
mathematics = int(input("score in math:"))
english = int(input("score in eng:"))
kiswahili = int(input("score in kisw:"))
science = int(input("score in science:"))
ire = int(input("score in ire:"))

# print(mathematics)
# print(english)
# print(kiswahili)
# print(science)
# print(ire)
# # add scores to a list
# scores = [mathematics, english, kiswahili, science, ire]
# scores = []
# scores.append(mathematics)
# scores.append(english)
# scores.append(science)
# scores.append(kiswahili)
# scores.append(ire)
# average = sum(scores) / len(scores)





# # store them in a dictionary
# students =[{'student Name' : student_name }, {'math' : mathematics, 'eng' : english, 'kisw' : kiswahili, 'science' : science, 'ire' : ire }]
# print(students)
 
students = {
      'name' : student_name,
      'math' : mathematics,
      'eng' : english,
      'kisw' : kiswahili,
      'science' : science,
      'ire' : ire
}

scores_list = list(students.values()) # ['dennis', 89, 90, 92, 67,67]
scores_list_without_name = scores_list[1:] #[ 89, 90, 92, 67,67]
average = sum(scores_list_without_name) / len(scores_list_without_name)
# compute the average score
#  AV = allfive subjects combined / by number of subjects 
# AV = ((mathematics + english + kiswahili + science + ire) / 5 /)


# average = (students['math'] + students['eng'] + students['kisw'] + students['science'] + students['ire']) / 5
print(average)

#for later in the course 
students_info = [
    {
        'name' : student_name, 
        'marks' : []
    }
]
print(list(students.values()))

# uotput the average score 


# print(AV)
# print(f"Dear {students[0]['student Name']} your subject scores are as follows mathematics:{students[1]['math']}, english:{students[1]['eng']},science:{students[1]['science']}, ire:{students[1]['ire']} and your average is {AV}")

# Net -> conversion 