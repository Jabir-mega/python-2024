# python 3 - Strings

# A string is a sequence of characters meaning - letters, numbers and other characters like the dollar sign, spacees and punctuation marks enclosed by single quotes, double quotes oreven triple quotes when spanning multiple lines 

# lets use astring 

my_string = "This is my first string"
print(my_string)

# what do we need triple quotes for? we need them whenever to enter a string on multiple lines -> i.e when puting a comment 

my_string = """this is my first string wewe 

"""
print(my_string)

#                 ---------- Indexing ----------
#  Python uses indexing to mark the position of an element within a sequence of elements - a string is a sequence of elements and the elements of a string are the characters themselves. One character one element

# The first element of any sequence, when counting from left to rigth, has the index 0, the second has the index 1, the third of the sequence is positioned ata index 2

# when using indexes remember to start counting from 0 

# when counting backward from right to left, the first index will be -1 

# The last character in a string will have index -1, When looking from right to left. 

#  Indexes are closed by square brackets, when we want to access some letters of a string 

# lets see in practice 

string1 = "cisco Router "
print(string1)

print(string1[0])