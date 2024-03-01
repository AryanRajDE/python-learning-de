"""
Task
Write a function named capital_indexes. The function takes a single parameter, which is a string.
Your function should return a list of all the indexes in the string that have capital letters.
For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].
"""

def capital_indexes(string_arg):
    print("Given String : ", string_arg)
    lst = []
    num = 0
    for letter in string_arg:
        if letter.isupper():
            lst.append(num)
        num = num+1
    
    print("list of capital indexes : ", lst)    
    return lst 
            
# calling function
string_argument = input('Give String : ') 
capital_indexes(string_argument)
    