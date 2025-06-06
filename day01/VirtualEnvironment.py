'''A virtual environment in Python is an isolated environment on your computer, where you can run and test your Python projects.

It allows you to manage project-specific dependencies without interfering with other projects or the original Python installation.

Think of a virtual environment as a separate container for each Python project. Each container:

Has its own Python interpreter
Has its own set of installed packages
Is isolated from other virtual environments
Can have different versions of the same package
Using virtual environments is important because:

It prevents package version conflicts between projects
Makes projects more portable and reproducible
Keeps your system Python installation clean
Allows testing with different Python versions
ADVERTISEMENT

Recommended videosPowered by Snigel
JavaScript - Introduction

Unmute
Duration 
2:49
/
Current Time 
0:00

Advanced Settings

Fullscreen

Play

Rewind 10 Seconds

Up Next
Brand logo


Creating a Virtual Environment
Python has the built-in venv module for creating virtual environments.

To create a virtual environment on your computer, open the command prompt, and navigate to the folder where you want to create your project, then type this command:

ExampleGet your own Python Server
Run this command to create a virtual environment named myfirstproject:

WindowsmacOS/Linux
C:\Users\Your Name> python -m venv myfirstproject
This will set up a virtual environment, and create a folder named "myfirstproject" with subfolders and files, like this:

Result
The file/folder structure will look like this:

myfirstproject
  Include
  Lib
  Scripts
  .gitignore
  pyvenv.cfg
ADVERTISEMENT

Activate Virtual Environment
To use the virtual environment, you have to activate it with this command:

Example
Activate the virtual environment:

WindowsmacOS/Linux
C:\Users\Your Name> myfirstproject\Scripts\activate
After activation, your prompt will change to show that you are now working in the active environment:

Result
The command line will look like this when the virtual environment is active:

WindowsmacOS/Linux
(myfirstproject) C:\Users\Your Name>
ADVERTISEMENT

Install Packages
Once your virtual environment is activated, you can install packages in it, using pip.

We will install a package called 'cowsay':

Example
Install 'cowsay' in the virtual environment:

WindowsmacOS/Linux
(myfirstproject) C:\Users\Your Name> pip install cowsay
Result
'cowsay' is installed only in the virtual environment:

Collecting cowsay
  Downloading cowsay-6.1-py3-none-any.whl.metadata (5.6 kB)
Downloading cowsay-6.1-py3-none-any.whl (25 kB)
Installing collected packages: cowsay
Successfully installed cowsay-6.1

[notice] A new release of pip is available: 25.0.1 -> 25.1.1
[notice] To update, run: python.exe -m pip install --upgrade pip
ADVERTISEMENT

Using Package
Now that the 'cowsay' module is installed in your virtual environment, lets use it to display a talking cow.

Create a file called test.py on your computer. You can place it wherever you want, but I will place it in the same location as the myfirstproject folder -not in the folder, but in the same location.

Open the file and insert these three lines in it:

Example
Insert two lines in test.py:

test.py
import cowsay

cowsay.cow("Good Mooooorning!")
Then, try to execute the file while you are in the virtual environment:

Example
Execute test.py in the virtual environment:

WindowsmacOS/Linux
(myfirstproject) C:\Users\Your Name> python test.py
As a result a cow will appear in you terminal:

Result
The purpose of the 'cowsay' module is to draw a cow that says whatever input you give it:

  _________________
| Good Mooooorning! |
  =================
                 \
                  \
                    ^__^
                    (oo)\_______
                    (__)\       )\/\
                        ||----w |
                        ||     ||

ADVERTISEMENT

Deactivate Virtual Environment
To deactivate the virtual environment use this command:

Example
Deactivate the virtual environment:

WindowsmacOS/Linux
(myfirstproject) C:\Users\Your Name> deactivate
As a result, you are now back in the normal command line interface:

Result
Normal command line interface:

WindowsmacOS/Linux
C:\Users\Your Name>
If you try to execute the test.py file outside of the virtual environment, you will get an error because 'cowsay' is missing. It was only installed in the virtual environment:

Example
Execute test.py outside of the virtual environment:

WindowsmacOS/Linux
C:\Users\Your Name> python test.py
Result
Error because 'cowsay' is missing:

Traceback (most recent call last):
  File "C:\Users\Your Name\test.py", line 1, in <module>
    import cowsay
ModuleNotFoundError: No module named 'cowsay'
Note: The virtual environment myfirstproject still exists, it is just not activated. If you activate the virtual environment again, you can execute the test.py file, and the diagram will be displayed.

ADVERTISEMENT

Delete Virtual Environment
Another nice thing about working with a virtual environment is that when you, for some reason want to delete it, there are no other projects depend on it, and only the modules and files in the specified virtual environment are deleted.

To delete a virtual environment, you can simply delete its folder with all its content. Either directly in the file system, or use the command line interface like this:

Example
Delete myfirstproject from the command line interface:

WindowsmacOS/Linux
C:\Users\Your Name> rmdir /s /q myfirstproject'''