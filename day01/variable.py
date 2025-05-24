#python has no command for declaring a varibale.
# A variable is created the moment you first assign a value to it

""" 
x = 5 # x is of type of int(integer)
y = "John" # y is now of type of string(str)
print(x)
print(y) 

"""
# prints in terminal 5, john


"""x = 4 # x is of type int(integer)
x = "sally" #x is now of type string(str)
print(x)
"""
#prints the current updated X variable which is the string "sally" and print it in the terminal

#Casting is if you want to specify the data type of variable, this can be done with casting
#Example
"""
x = str(3) #x will be '3'
y = int(3) #y will be 3
z = float(3)#z will be 3.0
"""
# you can get the data type of a variable with the type() function
#Example
x = 5
y = "john"
print(type(x))
print(type(y))
# tells you wat type of there are if its a string,integer, or a float with the type function

#Rules for Python variables:
#A variable name must start with a letter or the underscore character
#A variable name cannot start with a number
#A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
"""myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
    """
#Python Variables -Assign Multiple Values
""""
x,y,z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
"""
#in the terminal it prints Orange, Banana, and Cherry in X,Y,Z order
# One Value to Multiple Variables
"""
x = y = z = "Orange"
print(x)
print(y)
print(z)
"""
#prints Orange for all varibles that are equal to each other
#unpack a Collection
#If you have a collection of values in a list,tuple etc. Python allows you to extract the values into variables.
"""
fruits = ["apple", "banana", "cherry"]
x,y,z = fruits
print(x)
print(y)
print(z)
"""
#in the terminal it prints fruits in x,y,z as it equals fruits
# Output Variables is often use with the print() function often used ot output variables
#Example
"""
x = "Python is awesome"
print(x)
"""
#will print Python i awsome in the terminal
#Global Variables are variabls that are created outside of a function
#they can be used by everyone, both inside of functions and outside
#Example
"""
x = "awesome"
def myfunc():
     print("Python is " + x)
myfunc()
"""
# prints Python is awesome in the terminal
#now if you create a varibale with the same name inside a funcion, this varibale will be local and can only be used inside the function
#Example 
'''
x = "awesome"
def myfunc():
    x = "fantastic"
    print("Python is " + x)
myfunc()

print("python is " + x)
'''
#it prints "Python is fantastic" and "Python is awesome"
# reason why fantastic is first is because it is the updated X variable and prints it first then prints awesome last
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)