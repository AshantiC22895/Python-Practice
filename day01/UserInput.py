'''Python allows for user input.

That means we are able to ask the user for input.

The following example asks for your name, and when you enter a name, it gets printed on the screen:

ExampleGet your own Python Server
Ask for user input:

print("Enter your name:")
name = input()
print(f"Hello {name}")
Python stops executing when it comes to the input() function, and continues when the user has given some input.

ADVERTISEMENT

Recommended videosPowered by Snigel
JavaScript - Introduction
Video Player is loading.

Unmute
Duration 
2:49
/
Current Time 
0:00

Playback Speed Settings
1x

Fullscreen

Play

Rewind 10 Seconds

Up Next
Brand logo

Using prompt
In the example above, the user had to input their name on a new line. The Python input() function has a prompt parameter, which acts as a message you can put in front of the user input, on the same line:

Example
Add a message in front of the user input:

name = input("Enter your name:")
print(f"Hello {name})
Multiple Inputs
You can add as many inputs as you want, Python will stop executing at each of them, waiting for user input:

Example
Multiple inputs:

name = input("Enter your name:")
print(f"Hello {name}")
fav1 = input("What is your favorite animal:")
fav2 = input("What is your favorite color:")
fav3 = input("What is your favorite number:")
print(f"Do you want a {fav2} {fav1} with {fav3} legs?")
ADVERTISEMENT

Input Number
The input from the user is treated as a string. Even if, in the example above, you can input a number, the Python interpreter will still treat it as a string.

You can convert the input into a number with the float() function:

Example
To find the square root, the input has to be converted into a number:

x = input("Enter a number:")

#find the square root of the number:
y = math.sqrt(float(x))

print(f"The square root of {x} is {y}")
Validate Input
It is a good practice to validate any input from the user. In the example above, an error will occur if the user inputs something other than a number.

To avoid getting an error, we can test the input, and if it is not a number, the user could get a message like "Wrong input, please try again", and allowed to make a new input:

Example
Keep asking until you get a number:

y = True
while y == True:
  x = input("Enter a number:")
  try:
    x = float(x);
    y = False
  except:
    print("Wrong input, please try again.")

print("Thank you!"'''