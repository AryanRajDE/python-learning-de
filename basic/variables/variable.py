# Local Variable 
def add():  
    # Defining local variables. They have scope only within a function  
    a = 20  
    b = 30  
    c = a + b  
    print("a, b, c are local variables as they have only scoped under the function.")
    print("The sum is:", c)    

# Calling the function  
add()  

# ---------------------

# Global Variable
# Declare a variable and initialize it  
x = 101  
  
# Global variable in function  
def mainFunction():  
    # printing a global variable  
    global x  
    print("Global Variable accessing from outside the function : ", x)  
    
    # modifying a global variable  
    print("After modifying the global variable inside function, the value will get changed afterwords.")
    x = 'Welcome To Javatpoint'  
    print(x)  

# calling the function 
mainFunction()  
print(x)
