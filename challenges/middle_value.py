"""
Task
Write a function named mid that takes a string as its parameter.
Your function should extract and return the middle letter.
If there is no middle letter, your function should return the empty string.
For example, mid("abc") should return "b" and mid("aaaa") should return "".
"""

def mid(string):
    print("Given String : ", string)
    # finding he middle position of the string 
    mid_pos = int(len(string)/2)

    if len(string)%2 != 0 :
        print("Odd length string, it will have mid value...")
        middle_char = string[mid_pos]
        print(mid_pos, middle_char)
        return middle_char
    
    else:
        print("Even length string, it will have no mid value or two mid value...")
        middle_char = string[mid_pos-1:mid_pos+1]
        print(mid_pos-1, middle_char, mid_pos+1)
        return ""


# calling the function  
string_argument = input('Give String : ')         
mid(string_argument)       
        