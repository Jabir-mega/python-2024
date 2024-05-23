# Python 3 - Conversions btwn Data Types 

# The last thing we should cover on the data types topic is -> conversion btwn data types 

# This means that i learn how to convert from one data type, a numberfor example, to another data type, like string.

# There are specific function that accomplish this tasks,lets see them in action .

# Firstly, lets try to convert an int erger or floating-point number to a string.THis can be achieved by using the str() function.

num  = 2
f = 2.5

# /check the type of the variable 
print(type(num)) #<class 'int'>
print(type(f)) #<class 'float'>

# Now, converting number to a string 
num2 = str(num)
print(num2, type(num2))

f2 = str(f)
print(f2, type(f2))

# now, lets try backwards and convert a string to an interger, using int()

str1 = "5"
print(str1, type(str1))

int1 = int(str1)
print(type(int1), int1)

# You can also convert intergers to floating-point numbers, using the float() function, and viceversa, using the same int() function

num2 = 2

f = float(num2)
print(type(f), f)

# Not, the other way round, from float to interger using int()
f = 2.9999
int1= int(f)
print(type(int1), int1)

# Now, moving to sequences, lets convert a tuple into a list, using the list() function.

tuple1 = (1, 2, 3)
print(type(tuple1), tuple1)

# convert the tuple to alist
list1 = list(tuple1)
print(type(list1),list1)

# We have also seen how the set() function works for turning a list into set.

list = [1, 2, 3]
set1 = set(list)
print(type(set))
print(set1)

# The last thing i'll show you here is how to convert btwn diff numerical rep of numbers -> decimals, binary, and hex notation.So, base-10, base-2, and base-16 numbers.
# For this, we'll need the bin(). hex(),and int() functions.

num = 10
print(type(num))
# Convert to binary (o, 1)
num_bin = bin(num)
print(f"10 in binary is =  {num_bin}")

# Convert to hex
num_hex = hex(num)
print(f"10 in hex-decimal =  {num_hex}")

# Now to convert from binary and hex format to decimal notation, we will use the int() function 
bin_to_num = int(num_bin, base = 2 )
print(type(bin_to_num), bin_to_num)

hex_to_num = float(int(num_hex,16))
print(type(hex_to_num), hex_to_num)

# Next -> conditionals 