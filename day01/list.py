'''List
Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets:

Example
Create a List:

thislist = ["apple", "banana", "cherry"]
print(thislist)
#in the terminal it prints the list which are apple, banana, cherry'''

'''List Items
List items are ordered, changeable, and allow duplicate values.

List items are indexed, the first item has index [0], the second item has index [1] etc.

Ordered
When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

If you add new items to a list, the new items will be placed at the end of the list.

Note: There are some list methods that will change the order, but in general: the order of the items will not change.

Changeable
The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

Allow Duplicates
Since lists are indexed, lists can have items with the same value:

Example
Lists allow duplicate values:

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)'''

'''List Length
To determine how many items a list has, use the len() function:

Example
Print the number of items in the list:

thislist = ["apple", "banana", "cherry"]
print(len(thislist))
#in the terminal it prints 3'''

'''List Items - Data Types
List items can be of any data type:

Example
String, int and boolean data types:

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]'''

'''A list can contain different data types:

Example
A list with strings, integers and boolean values:

list1 = ["abc", 34, True, 40, "male"]'''

'''Python - Access List Items
Access Items
List items are indexed and you can access them by referring to the index number:

ExampleGet your own Python Server
Print the second item of the list:

thislist = ["apple", "banana", "cherry"]
print(thislist[1])
#in the terminal it prints "banana" cause of 1 but if its 0 it will print apple and 2 for cherry'''

'''Negative Indexing
Negative indexing means start from the end

-1 refers to the last item, -2 refers to the second last item etc.

Example
Print the last item of the list:

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])#in the terminal it prints cherry and it goes backwards cause its negative'''

'''Range of Indexes
You can specify a range of indexes by specifying where to start and where to end the range.

When specifying a range, the return value will be a new list with the specified items.

Example
Return the third, fourth, and fifth item:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])#it prints cherry orange and kiwi'''

'''This example returns the items from the beginning to, but NOT including, "kiwi":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])#it the terminal it prints apple,banana,cherry,orange

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])#in the terminal it prints apple and banana

Check if Item Exists
To determine if a specified item is present in a list use the in keyword:

Example
Check if "apple" is present in the list:

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
  
  Change Item Value
To change the value of a specific item, refer to the index number:

ExampleGet your own Python Server
Change the second item:

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)# in the terminal it changes banana to blackcurrant'''

'''Insert Items
To insert a new list item, without replacing any of the existing values, we can use the insert() method.

The insert() method inserts an item at the specified index:

Example
Insert "watermelon" as the third item:

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)# in the terminal it adds watermelon after banana'''

'''Append Items
To add an item to the end of the list, use the append() method:

Example
Using the append() method to append an item:

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)'''

'''Extend List
To append elements from another list to the current list, use the extend() method.

Example
Add the elements of tropical to thislist:

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)#in the terminal it prints apple,banana,cherry,mango,pineapple,papaya'''

'''Remove Specified Item
The remove() method removes the specified item.

Example
Remove "banana":

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)#in the terminal it remove banana and says apple, cherry'''

'''Remove Specified Index
The pop() method removes the specified index.

Example
Remove the second item:

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
If you do not specify the index, the pop() method removes the last item.

Example
Remove the last item:

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)# in the terminal it removes cherry'''

'''The del keyword also removes the specified index:

Example
Remove the first item:

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)#in the terminal it prints banana, and cherry'''

'''Clear the List
The clear() method empties the list.

The list still remains, but it has no content.

Example
Clear the list content:

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)'''

'''Loop Through a List
You can loop through the list items by using a for loop:

ExampleGet your own Python Server
Print all items in the list, one by one:

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)#in the terminal it prints the list in a vertically way'''
  
'''Join Two Lists
There are several ways to join, or concatenate, two or more lists in Python.

One of the easiest ways are by using the + operator.

Example
Join two list:

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
Another way to join two lists is by appending all the items from list2 into list1, one by one:

Example
Append list2 into list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
Or you can use the extend() method, where the purpose is to add elements from one list to another list:

Example
Use the extend() method to add list2 at the end of list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)'''

'''List Methods
Python has a set of built-in methods that you can use on lists.

Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list'''