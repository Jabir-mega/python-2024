# Python 3 Booleans- Logical Operators

# as a short definition we can say the booleans defines only two values -> true or false 
# Booleans comes from George Boolean a 19TH century math philosopher 
#  these two values can be equal to 1 and 0 
#  in python true is written with a capital T-> True and false with a capital F-> False. 

# Basically they are used to evaluate wether an expression is true or false  and can be futher used in conditional  or loop structures 

#  for now lets evaluate some basic expression and see how python evaluates each of them 

print(1 == 1)# returns True

print(1 == 2)#  returns False

print("python" != "Python") # returns True (This is due to difference in casesensitivty in the letter 'p')

print(3 <= 4) # returns True 

# The above are some basic evaluation 

#  There are three main boolean operation,,each of them having a specific operations namely  "and", "or", and "not"

# 1 -> "and" means both the operands/expression should be True, in order to have the entire expresion evaluated as True
        # Both must be true 
print((1 == 1) and (2 == 2)) # returns True 

print((1 == 1) and (2 == 3)) # returns False 

# the conclusion here is that when using AND  operand, if both expression are true, then the result will also be True. On the otherhand if at least one expression is evaluated as false then the result will be false as well. 

# 2 -> "OR " -> if atleast one of the expressions evaluates to be true then the final result is True. if they are both false, then the final result willbe false as well
# So when using OR it is enough if only one expression is True, in order to have True as the final result 
print((1 == 1) or (2 == 2)) # returns True
print((1 == 1) or (2 != 3)) # returns True 
print((1 == 1) or (2 != 3) and ("jave" == "java")) # returns True

# 3 -> Finally, using NOT means simply denying an expression. If that expression is True, then denying it will lead to false and vise-versa 
print(not(1 == 1))# returns False 
print(not(1 == 2))# returns True

# One more thing to keep in mind here: some python values always evaluate to false. Ther are:-
"""
None
0
0.0
empty string ""
empty list []
empty set()
empty tuple ()
empty dictionaries {}
"""

# Python provides the bool() function to help us evaluate values and expression  as true or false. so lets use this function to check the always false value 
print(bool(None))# returns False 
print(bool(0))# returns False 
print(bool(0.0))# returns False 
print(bool(""))# returns False  

# All other values in python are considered to be true 

print(bool(0.1))# returns True
print(bool(" "))# returns True (due to space in btwn the '""')

# Real World eExample -> Login system...
# User credential in the DB database
user_name_in_db = "Dennis"
password_in_db = "p@$$w0rd"

# user credentials provided during login attempt 
user_name = "Dennis"
password = "p@$$w0rd"

# check if the user credentials are correct
if (user_name_in_db == user_name ) and (password_in_db == password ):
    print("login successful!!!")
else:
    print("wrong username or password, Please try again!!!")

# Next -> Lists 