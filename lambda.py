'''
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.'''

'''
Syntax:
lambda arguments : expression
The expression is executed and the result is returned:'''

'''ExampleGet your own Python Server
Add 10 to argument a, and return the result:

x = lambda a : a + 10
print(x(5))#in the terminal prints 15'''

'''Example
Multiply argument a with argument b and return the result:

x = lambda a, b : a * b
print(x(5, 6))#in the terminal a = 5 and 5 = 6 and it is multiply by 30'''

'''Example
Summarize argument a, b, and c and return the result:

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))'''

'''Why Use Lambda Functions?
The power of lambda is better shown when you use them as an anonymous function inside another function.

Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

def myfunc(n):
  return lambda a : a * n
Use that function definition to make a function that always doubles the number you send in:

Example
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))
#in the terminal it prints 22 it shows that n is 2 and its doubler it 11

Or, use the same function definition to make a function that always triples the number you send in:

Example
def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))#in the terminal it prints 33
Or, use the same function definition to make both functions, in the same program:

Example
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))'''

def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))