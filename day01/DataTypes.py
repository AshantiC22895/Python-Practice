'''
Built-in Data Types
In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
'''
'''
Setting the Data Type
In Python, the data type is set when you assign a value to a variable:

Example	Data Type	Try it
x = str("Hello World")	str	
x = int(20)	int	
x = float(20.5)	float	
x = complex(1j)	complex	
x = list(("apple", "banana", "cherry"))	list	
x = tuple(("apple", "banana", "cherry"))	tuple	
x = range(6)	range	
x = dict(name="John", age=36)	dict	
x = set(("apple", "banana", "cherry"))	set	
x = frozenset(("apple", "banana", "cherry"))	frozenset	
x = bool(5)	bool	
x = bytes(5)	bytes	
x = bytearray(5)	bytearray	
x = memoryview(bytes(5))	memoryview	

'''
#there are three numeric types in python
#int
#float
#complex
#Example
'''
x = 1    # int
y = 2.8  # float
z = 1j   # complex
To verify the type of any object in Python, use the type() function:
Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length
Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
Float can also be scientific numbers with an "e" to indicate the power of 10.
Complex numbers are written with a "j" as the imaginary part:
'''

'''
Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:
Example
Import the random module, and display a random number from 1 to 9:

import random

print(random.randrange(1, 10))
spits a random number rangeing form (1,10)
'''