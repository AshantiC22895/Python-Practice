#Strings in python are surrounded by either single quotation marks, or double quotation marks.
#You can use quotes inside a string, as long as they don't match the quotes surrounding the string
'''
Example
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

Assigning a string to a variable is done with the variable name followed by an equal sign and the string:
Example:
a = "Hello"
print(a)
#will print Hello in the terminal

You can assign a multiline string to a variable by using three quotes:
You can use three double quotes:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.
Example
Get the character at position 1 (remember that the first character has the position 0):

a = "Hello, World!"
print(a[1])
#prints the letter e in the terminal and if you change 1 to 0 it will print H. the numbers are just the position of each letter in the string

Since strings are arrays, we can loop through the characters in a string, with a for loop.
Loop through the letters in the word "banana":

for x in "banana":
  print(x)
  # it prints banna vertically
  
To get the length of a string, use the len() function.
The len() function returns the length of a string:

a = "Hello, World!"
print(len(a))
# in the terminal it prints the number 13 cause thats how many letters in "Hello World"
'''
'''
To check if a certain phrase or character is present in a string, we can use the keyword in
Example
Check if "free" is present in the following text:

txt = "The best things in life are free!"
print("free" in txt)
#in the terminal it says true because it detects "free" in the string and if not it would be false
'''
'''
Use it in an if statement:

Example
Print only if "free" is present:

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
  #in the terminal it prints("Yes, 'free' is present cause its true)
'''
'''
Check if NOT
To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.

Example
Check if "expensive" is NOT present in the following text:

txt = "The best things in life are free!"
print("expensive" not in txt)
#in the terminal its says false cause 'expensive' is not in the text
# it can be use as the same as an if statement

'''
'''Slicing
You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string.

ExampleGet your own Python Server
Get the characters from position 2 to position 5 (not included):

b = "Hello, World!"
print(b[2:5])
#in the terminal it prints llo cause 2 got rid of He and 5 got rid of world
Example
Get the characters from the start to position 5 (not included):

b = "Hello, World!"
print(b[:5]) # in the terminal it only deletes world and keeps hello

ExampleGet your own Python Server
The upper() method returns the string in upper case:

a = "Hello, World!"
print(a.upper())

Example
The lower() method returns the string in lower case:

a = "Hello, World!"
print(a.lower())

Remove Whitespace
Whitespace is the space before and/or after the actual text, and very often you want to remove this space.

Example
The strip() method removes any whitespace from the beginning or the end:

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

Replace String
Example
The replace() method replaces a string with another string:

a = "Hello, World!"
print(a.replace("H", "J"))
#in the terminal it will replace h with j and instead of hello it will be jello

String Concatenation
To concatenate, or combine, two strings you can use the + operator.

ExampleGet your own Python Server
Merge variable a with variable b into variable c:

a = "Hello"
b = "World"
c = a + b
print(c)# in the terminal it prints Hello World

F-Strings
F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.

To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.

Example
Create an f-string:

age = 36
txt = f"My name is John, I am {age}"
print(txt)# in the terminal it will print My name is john, I am 36

Placeholders and Modifiers
A placeholder can contain variables, operations, functions, and modifiers to format the value.

Example
Add a placeholder for the price variable:

price = 59
txt = f"The price is {price} dollars"
print(txt)# in the terminal it will print the price is 59 dollars

A placeholder can include a modifier to format the value.

A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:

Example
Display the price with 2 decimals:

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)#in the terminal it will print 59.00 and .2f is the added zeros 

A placeholder can contain Python code, like math operations:

Example
Perform a math operation in the placeholder, and return the result:

txt = f"The price is {20 * 59} dollars"
print(txt)'''

'''String Methods
Python has a set of built-in methods that you can use on strings.

Note: All string methods return new values. They do not change the original string.

Method	Description
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning'''



