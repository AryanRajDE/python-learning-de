"""
Task
The aim of this challenge is, given a dictionary of people's online status, to count the number of people who are online.
Given Dictionary is :
    statuses = {
        "Alice": "online",
        "Bob": "offline",
        "Eve": "online",
    }
Write a function named online_count that takes one parameter.
The parameter is a dictionary that maps from strings of names to the string "online" or "offline", as seen above.
Your function should return the number of people who are online.
"""


def online_count(statuses):
    print(statuses)
    count = 0
    
    for k,v in statuses.items():
        if v == 'online':
            count = count+1
    print("online_count : ", count)
    return count


# calling the function
statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

online_count(statuses)