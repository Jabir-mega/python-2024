# python 3 - user input 
# ctrl+/ -> shortcut for inserting a  comment
#  throughtout the course we are going to learn howtoinsert some input intp a python programme 
#  we are going to usea specific function to askthe user for some input, store the info he/she is entering at the prompt and then use that info futher into the programme 
#  this is especially usefull when you need to build an interactive application usually having some sort of menu that the user needs to interact with

#  examples of such menus are "pls enter your user name username:" or "choose an option from the following list:" and so on ...

#  the function we are talking about is called input()

# lets prompt the user to enter a string that he/she want to be printed out on the screen 

# lets me write the code and then anylize it inch by inch 

user_says = input("please enter the string you wish to print: ")

# looking at the above line of code you may ask yourself what is this "user_says" thing?
# well, thats a python variable .
#  for now just keep in mind that by using a variable you can store or save the value entered by the user for later use 

#  the so called storage or saving of the user's input is accomplished using the equal sign "=", which is called an assignment operater
#  folling the = sign we have the input() function 
# next, inside input()'s pair of parenthesis , you have to type in a description, a phrase, which is actually a string asking the user for input. This is completely upto you with an appropriate sentence.

# /A good practice here is to also enter a colon and a space after the text, so when the user inputs some data it will be clearly separeted from the sentence -> just to make everything pretty and easy to read 

# Finally, do not forget to close everything you write in btwn paranthesis , also using either double or single quotes.

#  last but not least, inorder to have out text printed on the screen and visible to the user, we should use the print() function inpython , to print out the content of the user_says variable 
print(user_says) 

#  shortcut for opening the terminal -> ctrl + j

#  Next - variables