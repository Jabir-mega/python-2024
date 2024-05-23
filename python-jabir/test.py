# # import math

# # print(dir(math))


# # def my_first_function():
# #     "This is my first function!"
# #     print("Hello Python!")

# # my_first_function()    

# # x = [10]

# # for i in x:
# #     if i > 5:
# #         print("x is greater than 5")
# #     else:
# #         print("x is less than 5") 



#               / challenge time 
#  write a python program that asks the user the radius of a circle and returns the perimeter and area of the circle 
#  define pie 
PI = 22/7
# Ask the user the radius of the cicle 
Radius = int(input("Enter the radius of the circle: "))
print(Radius)

# Return perimeter
Perimeter = PI * (Radius * 2) 

# Calculate area 
area = PI * (Radius * Radius)

# Print the result 

Result = (f"The area and perimeter of a circle whose Radius is {Radius} is {area} and {Perimeter} respectively")

print(Result)


# #                       challege timez
# # write a python program that prompts the user to enter there name and age the programm will than output the decades and the minutes the user has lived 
# # a decade is 10 yrs e.g if you are 22 yrs  you have lived 2 decades 

# Name = input("Enter you name: ")

# # Ask for user age 
# Age = int(input("Enter your age: "))

# # Calculate the age of the user in decades 
# Decades_lived = Age // 10

# # Calculate the age of the user in minutes 
# Minutes_lived = Age * 365 * 24 * 60

# print(f"Dear {Name} your have lived for {Decades_lived} decades and {Minutes_lived} Minute Hence you are {Age} years old")

# # create a python that captures the name and list of 5 subject scores and then stores that info to a dictionary.the program then outputs the average scores of the students .

# student_name = input("Enter your name: ")

# math = int(input("Enter your score: "))
# eng = int(input("Enter your score: "))
# kisw = int(input("Enter your score: "))
# science = int(input("Enter your score: "))
# ire = int(input("Enter your score: "))

# student = {
#     'name' : student_name,
#     'math' : math,
#     'eng': eng,
#     'kisw' : kisw,
#     'science' : science,
#     'ire' : ire
# }

# # output
# scores = list(student.values())
# scores_without_name = scores[1:]
# # Average
# Av = sum(scores_without_name) / len(scores_without_name)
# # Total marks is 
# Total = sum(scores_without_name)

# print(scores_without_name)
# print(Av)
# print(f"dear {student_name} your total marks is { Total} hence your average is {Av}")

# challenge time
# create a python programm using 5 or 4 functions that asks the user for their name and age. Then the programm should output the user info in a nice format displaying the name, age, decades lived, and age in second that the user has lived.



# a function to get the user name
# def user_name():
#     name = input("Eneter your name: ")
    

# # A function to get the user age 
def user_age():
    Age = int(input("Enter your age: "))
    
# A function to get user age in decades 
def decades_lived(Age):
    decades = Age // 10
    return decades
# calculate age in seconds
def age_in_seconds(Age):
    seconds = Age // 10 
    return seconds

def user_info():
    Name = user_name()
    Age = user_age()
    decades = decades_lived(Age)
    sconds = age_in_seconds(Age)
    print(f"dear {Name} you ahve lived for {decades} decades and {sconds} seconds, hence you are {Age} years old")
    
    
    
# user_info()


# A function to get user name 
def user_name():
    name = input("Enter your name: ")
    return name

# A function to get user age 
def user_age():    
    age = int(input("Enter your age: "))
    return age

# A fuction to get user age in decades
def user_decades(age):
    Age = age // 10
    return Age
# A function to get user age in minutes 
def Age_in_sec(age):
    seconds = age * 365.25 * 24 * 60 * 60
    return seconds
# a fuction to display them'

def user_info():
    name = user_name()
    age = user_age()
    Decades = user_decades(age)
    seconds_lived = Age_in_sec(age) 
    print(f"Dear {name} you have lived for {Decades} decades and {seconds_lived} seconds hence you are {age} years old." )
    
# call the user_info function 
user_info()