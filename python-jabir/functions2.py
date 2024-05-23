#  create a function that takes in a list of intergers and then returns the smallest odd interger in that list
# solution
def smallest_interger(number_list):
    odd = []
    for number in number_list:
        if number % 2 == 1:
            odd.append(number)
    # return min(odd) 
    odd.sort() # sorts the lists in an ascending order 
    return odd[0] # selects the first element/interger


print(smallest_interger([12, 40, 45, 30, 20, 23, 40, 37, 37, 7, 17]))