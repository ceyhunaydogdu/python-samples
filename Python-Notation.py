"""This is a 
multiline docstring/comment."""

"""
if 5 > 2:
 #This is the comment
print("Five is greater than two!")#This will raise an error, identation needed.
#"""

"""
x=5
y="ceyhun"
print(x)
print(y)
#"""

"""
x = 4 # x is of type int
x = "Sally" # x is now of type str
print(x)
#"""

"""
x = "awesome"
print("Python is " + x)
#"""

"""
x = "Python is "
y = "awesome"
z =  x + y
print(z)
#"""

"""
x = 5
y = 10
print(x + y)
#"""


"""
x = "Python is "
y = 5
#print(x+y)#This will raise an error. can not concat different int and string
print (x,y,"years old")# This will work
#"""

"""
x = 1    # int
y = 2.8  # float
z = 3+5j   # complex
print(x,y,z)
print(type(x), type(y),type(z))
#"""

"""
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
print(x,y,z)
print(type(x), type(y),type(z))
#"""

"""
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
print(x,y,z,w)
print(type(x), type(y),type(z), type(w))
#"""

"""
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
print(x,y,z)
print(type(x), type(y),type(z))
#"""

"""
a = "Hello, World!"
print(a[0])
print(a[1:5])
b = " Nello, World! "
print(b.strip()) # returns "Hello, World!" like trim() in java and js
print(len(a))# length
print(a.lower())#lowercase
print(a.upper())#uppercase
print(a.replace("H", "J"))
print(a.split(",")) # returns ['Hello', ' World!']
#"""

"""
print("Enter your name:")
x = input()
print("Hello, " + x)
#"""
"""
print("See u tomorrow, "+ input("Your last name ? : "))# shorter version
#"""

#A list is a collection which is ordered and changeable.
#In Python lists are written with square brackets.
"""
#Create a List:
thislist = ["apple", "banana", "cherry"]
print(thislist)
#"""

"""
#Print the second item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
#"""

"""
#Change the second item:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
#"""
"""
#Print all items in the list, one by one:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
#"""
"""
#Check if "apple" is present in the list:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
#"""
"""
#Print the number of items in the list:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
#"""
"""
#Using the append() method to append an item:
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist.append("orange")
print(thislist)
#"""
"""
#Insert an item as the second position:
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist.insert(1, "orange")
print(thislist)
#"""
"""
#The remove() method removes the specified item:
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist.remove("banana")
print(thislist)
#"""
"""
#The pop() method removes the specified index,
#(or the last item if index is not specified):
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist.pop()
print(thislist)
#"""
"""
#The del keyword removes the specified index:
#The del keyword can also delete the list completely:
thislist = ["apple", "banana", "cherry"]
print(thislist)
del thislist[0]
print(thislist)
#"""
"""
#The clear() method empties the list:
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
#"""
"""
#Using the list() constructor to make a List:
# note the double round-brackets
thislist = list(("apple", "banana", "cherry")) 
print(thislist)
#"""

#A tuple is a collection which is ordered and unchangeable.
#In Python tuples are written with round brackets.
"""
#Create a Tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple)
#"""
"""
#Return the item in position 1:
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
#"""
"""
#Once a tuple is created, you cannot change its values.
thistuple = ("apple", "banana", "cherry")
thistuple[1] = "blackcurrant"
print(thistuple)# The values will remain the same:
#"""
"""
#Iterate through the items and print the value
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
#"""
"""
#Check if "apple" is present in the tuple
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
#"""
"""
#Print the number of items in the tuple:
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
#"""
"""
#You cannot add items to a tuple:
thistuple = ("apple", "banana", "cherry")
thistuple[3] = "orange" # This will raise an error
print(thistuple)
#"""
"""
#You cannot remove items in a tuple.
#But del keyword can delete the tuple completely:
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists
#"""
"""
#It is also possible to use the tuple() constructor to make a tuple.
# note the double round-brackets
thistuple = tuple(("apple", "banana", "cherry")) 
print(thistuple)
#"""

#A set is a collection which is unordered and unindexed.
#In Python sets are written with curly brackets.
"""
#Create a Set:
#Sets are unordered, so the items will appear in a random order.
thisset = {"apple", "banana", "cherry"}
print(thisset)
#"""
"""
#You cannot access items in a set by referring to an index,
#since sets are unordered the items has no index.
#But you can loop through the set items using a for loop,
#Loop through the set, and print the values:
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
#"""
"""
#You can ask if a specified value is present in a set, by using the in keyword.
#Check if "banana" is present in the set:
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)
if 'cherry' in thisset:
    print('yes, cherry exits.')
#"""
"""
#Once a set is created, you cannot change its items,
#but you can add new items.
#Add an item to a set, using the add() method:
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
#Add multiple items to a set, using the update() method:
thisset = {"apple", "banana", "cherry"}
thisset.update(["orange", "mango", "grapes"])
print(thisset)
#"""
"""
#Get the number of items in a set:
thisset = {"apple", "banana", "cherry"}
print(len(thisset))
#"""
"""
#Remove "banana" by using the remove() method:
#If the item to remove does not exist, remove() will raise an error.
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
#"""
"""
#Remove "banana" by using the discard() method:
#If the item to remove does not exist, discard() will NOT raise an error.
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
#"""
"""
#You can also use the pop(), method to remove an item,
#but this method will remove the last item.
thisset = {"apple", "banana", "cherry"}
print(thisset)
x = thisset.pop()
print(x)
print(thisset)
#"""
"""
#The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)
#"""
"""
#The del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)
#"""
"""
#Using the set() constructor to make a set:
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
#"""

#A dictionary is a collection which is unordered, changeable and indexed.
#In Python dictionaries are written with curly brackets,
#and they have keys and values.
"""
#Create and print a dictionary:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
#Get the value of the "model" key:
x = thisdict["model"]
print(x)
x = thisdict.get("year")
print(x)
#"""
"""
#Change the "year" to 2018:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict)
#Print all key names in the dictionary, one by one:
for x in thisdict:
    print(x)
    print(thisdict.get(x))
#You can also use the values() function to return values of a dictionary:
print("Only values....")
for x in thisdict.values():
    print(x)
#"""
"""
#Check if "model" is present in the dictionary:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
#Print the number of items in the dictionary:
print(len(thisdict))
#"""
"""
#Adding an item to the dictionary is done by using a new index key
#and assigning a value to it:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
#"""
"""
#The pop() method removes the item with the specified key name:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)
#"""
"""
#The popitem() method removes the last inserted item
#(in versions before 3.7, a random item is removed instead):
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)
#"""
"""
#The del keyword removes the item with the specified key name:
#The del keyword can also delete the dictionary completely: del thisdict
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
#"""
"""
#The clear() keyword empties the dictionary:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)
#"""
"""
#It is also possible to use the dict() constructor to make a dictionary:
thisdict = dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)
#"""
#An "if statement" is written by using the if keyword.
#If statement, without indentation (will raise an error):
"""
a = 33
b = 200
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
#"""
"""
#Short Hand If
a=34
b=22
if a > b: print("a is greater than b")
#"""
"""
#Short Hand If .. else
a=34
b=42
print(a) if a > b else print(b)
#"""
"""
#Short Hand If .. else with multiple statements.
a=34
b=42
print("A") if a > b else print("=") if a == b else print("B")
#"""
"""
#The and keyword is a logical operator,
#and is used to combine conditional statements:
a=52
b=42
c=54
if a > b and c > a:
  print("Both conditions are True")
#"""
"""
#The or keyword is a logical operator,
#and is used to combine conditional statements:
a=52
b=42
c=54
if a > b or c > a:
  print("At least one of the conditions are True")
#"""
#With the while loop we can execute a set of statements as long as a condition is true
"""
#Print i as long as i is less than 6:
i=1
while i< 6:
    print(i)
    i+=1
#"""
"""
#With the break statement we can stop the loop even if the while condition is true:
i=1
while i< 6:
    print(i)
    if i==3: break
    i+=1
#"""
"""
#With the continue  statement we can stop the current iteration, and continue with the next:
i=0
while i< 6:
    i+=1
    if i==3: continue
    print(i)    
#"""
#A for loop is used for iterating over a sequence
#(that is either a list, a tuple, a dictionary, a set, or a string).
#break and continue statement are as in above.
"""
#Print each fruit in a fruit list:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)    
#"""
"""
#Loop through the letters in the word "banana":
fruits = ["apple", "banana", "cherry"]
for x in "banana":
  print(x)   
#"""
"""
#The range() function returns a sequence of numbers, starting from 0 by default,
#and increments by 1 (by default), and ends at a specified number.
for x in range(6):
  print(x)  
#"""
"""
#The range() function with start parameter
for x in range(2,6):
  print(x)  
#"""
"""
#The range() function defaults to increment the sequence by 1, however
#it is possible to specify the increment value by adding a third parameter: 
for x in range(2, 30, 3):
  print(x)  
#"""
"""
#The else keyword in a for loop specifies a block of code
#to be executed when the loop is finished: 
for x in range(6):
  print(x)
else:
  print("Finally finished!")  
#"""
"""
#A nested loop is a loop inside a loop.
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
#"""
#A function is a block of code which only runs when it is called.
"""
#In Python a function is defined using the def keyword:.
def my_function():
  print("Hello from a function")
#To call a function, use the function name followed by parenthesis:
my_function()
#"""
"""
#Parameters are specified after the function name, inside the parentheses.
#You can add as many parameters as you want, just separate them with a comma.
def writeName(fname):
  print(fname + " Refsnes")

writeName("Emil")
writeName("Tobias")
writeName("Linus")
writeName()#Will raise an error..
#"""
"""
#The following example shows how to use a default parameter value.
#If we call the function without parameter, it uses the default value:
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()#This will NOT raise an error.
my_function("Brazil")
#"""
"""
#To let a function return a value, use the return statement:
def my_function(x):
  return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))
#"""
#A lambda function is a small anonymous function.
#A lambda function can take any number of arguments,
#but can only have one expression.
"""
#A lambda function that adds 10 to the number
#passed in as an argument, and print the result:
x = lambda a : a + 10
print(x(5))
#A lambda function that multiplies argument
#a with argument b and print the result:
x = lambda a, b : a * b
print(x(5, 6))
#"""
"""
#The power of lambda is better shown when you use them as
#an anonymous function inside another function.
def myfunc(n):
  return lambda a : a * n
#Use that function definition to make a function
#that always doubles the number you send in:
mydoubler = myfunc(2)
print(mydoubler(11))
#Or, use the same function definition to make a
#function that always triples the number you send in:
mytripler = myfunc(3)
print(mytripler(11))
#"""
#Python is an object oriented programming language.
#Almost everything in Python is an object, with its properties and methods.
#A Class is like an object constructor, or a "blueprint" for creating objects.
"""
#To create a class, use the keyword class:
#Create a class named MyClass, with a property named x:
class MyClass:
  x = 5
#Now we can use the class named myClass to create objects:
p1 = MyClass()
print(p1.x)
#"""
"""
#All classes have a function called __init__(), which is always
#executed when the class is being initiated.
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
#"""
"""
#Let us create a method in the Person class:
#Insert a function that prints a greeting, and execute it on the p1 object:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
#"""
"""
#Note:The self parameter is a reference to the class instance itself,
#and is used to access variables that belongs to the class.
#It does not have to be named self , you can call it whatever you like,
#but it has to be the first parameter of any function in the class:
#Use the words mysillyobject and abc instead of self:
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()
#"""
"""
#You can modify properties on objects like this:
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.age = 40
#You can delete properties on objects by using the del keyword:
del p1.name
#You can delete objects by using the del keyword:
del p1
#"""
#Python Iterators
#Lists, tuples, dictionaries, and sets are all iterable objects.
#They are iterable containers which you can get an iterator from.
#All these objects have a iter() method which is used to get an iterator:
"""
#Return a iterator from a tuple, and print each value:
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
#"""
"""
#Strings are also iterable objects, containing a sequence of characters:
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
#"""
"""
#We can also use a for loop to iterate through an iterable object:
#The for loop actually creates in iterator object
#and executes the next() method for each loop.
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)
#"""
"""
#To create an object/class as an iterator
#you have to implement the methods __iter__() and __next__() to your object.
#The __iter__() method acts similar, you can do operations
#(initializing etc.), but must always return the iterator object itself.
#The __next__() method also allows you to do operations,
#and must return the next item in the sequence.
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
#"""
"""
#The example above would continue forever
#if you had enough next() statements, or if it was used in a for loop.
#To prevent the iteration to go on forever,
#we can use the StopIteration statement.
#Stop after 20 iterations:
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)
#"""
#Python Modules
#Consider a module to be the same as a code library.
#A file containing a set of functions you want
#to include in your application.
"""
#To create a module just save the code
#you want in a file with the file extension .py:
#Save this code in a file named mymodule.py
def greeting(name):
  print("Hello, " + name)
#"""
"""
#Import the module named mymodule, and call the greeting function:
#When using a function from a module,
#use the syntax: module_name.function_name.
import mymodule
mymodule.greeting("Jonathan")
#"""
"""
#Import the module named mymodule, and access the person1 dictionary:
import mymodule
a = mymodule.person1["age"]
print(a)
#"""
"""
#You can name the module file whatever you like,
#but it must have the file extension .py
#You can create an alias when you import a module, by using the as keyword:
import mymodule as mx
a = mx.person1["age"]
print(a)
#"""
"""
#There are several built-in modules in Python,
#which you can import whenever you like.
import platform
x = platform.system()
print(x)
#"""
"""
#There is a built-in function to list all the function names
#(or variable names) in a module. The dir() function:
#List all the defined names belonging to the platform module:
import platform
x = dir(platform)
print(x)
#"""
"""
#You can choose to import only parts from a module,
# by using the from keyword.
#Import only the person1 dictionary from the mymodule:
import mymodule as my1 #all funciton and variables
x = dir(my1)
print(x)
#When importing using the from keyword,
#do not use the module name when referring to elements in the module
from mymodule import person1 #only person1 variable imported
print (person1["age"])
#"""
#Python Datetime
#A date in Python is not a data type of its own,
"""
#Import the datetime module and display the current date:
import datetime

x = datetime.datetime.now()
print(x)
#"""
"""
#Return the year and name of weekday:
import datetime
x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))
#"""
"""
#To create a date,
#we can use the datetime() class (constructor) of the datetime module.
#The datetime() class requires
#three parameters to create a date: year, month, day.
#The datetime() class also takes parameters for time and timezone
#(hour, minute, second, microsecond, tzone),
#but they are optional, and has a default value of 0, (None for timezone).
import datetime
x = datetime.datetime(2020, 5, 17)
print(x)
#"""
"""
#The datetime object has a method for formatting date objects
#into readable strings.
#The method is called strftime(), and takes one parameter, format,
#to specify the format of the returned string:
#Display the name of the month:
import datetime
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))
#"""
#Python JSON
#Python has a built-in package called json,
#which can be use to work with JSON data.
"""
#If you have a JSON string,
#you can parse it by using the json.loads() method.
#The result will be a Python dictionary.
#Convert from JSON to Python:
import json
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"])
#"""
"""
#If you have a Python object,
#you can convert it into a JSON string by using the json.dumps() method.
#Convert from Python to JSON:
import json
# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
# convert into JSON:
y = json.dumps(x)
# the result is a JSON string:
print(y)
#"""
"""
#You can convert Python objects of the following types, into JSON strings:
#Convert Python objects into JSON strings, and print the values:
import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
#"""
"""
#Convert a Python object containing all the legal data types:
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))
#"""
"""
#The json.dumps() method has parameters to make it easier to read the result:
#Use the indent parameter to define the numbers of indents:
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x, indent=4))
#"""
"""
#You can also define the separators, default value is (", ", ": "),
#which means using a comma and a space to separate each object,
#and a colon and a space to separate keys from values:
#Use the separators parameter change the default separator:
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x, indent=4, separators=(". ", " = ")))
#"""
"""
#The json.dumps() method has parameters to order the keys in the result:
#Use the sort_keys parameter to specify if the result should be sorted or not:

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x, indent=4, sort_keys=True))
#"""
#Python PIP
#PIP is a package manager for Python packages, or modules if you like.
#If you have Python version 3.4 or later, PIP is included by default.
#Check if PIP is Installed: on command line prompt type: "pip -V"
"""
#Download a package named "camelcase": "pip install camelcase"
#Using a package
#Import and use "camelcase":
import camelcase
c = camelcase.CamelCase()
txt = "hello world"
print(c.hump(txt))
#to uninstall the package named "camelcase" type: "pip uninstall camelcase"
#Use the list command to list all the packages: "pip list"
#"""
#Python Try Except
#The try block lets you test a block of code for errors.
#The except block lets you handle the error.
#The finally block lets you execute code,
#regardless of the result of the try- and except blocks.
"""
#The try block will generate an exception, because x is not defined:
try:
 print(x)
except:
 print("An exception occurred")
#""" 
"""
#Print one message if the try block raises a NameError
#and another for other errors:
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
#"""
"""
#You can use the else keyword to define a block of code
#to be executed if no errors were raised:
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
#""" 
"""
#The finally block, if specified, will be executed
#regardless if the try block raises an error or not.
#This can be useful to close objects and clean up resources:
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
#"""
"""
#The finally block can be useful to close objects and clean up resources:
#Try to open and write to a file that is not writable:
try:
  f = open("demofile.txt")
  f.write("Lorum Ipsum")
except:
  print("Something went wrong when writing to the file")
finally:
    f.close()
#"""
#Python File Handling
"""
#The key function for working with files in Python is the open() function.
#The open() function takes two parameters; filename, and mode. Modes are:
#"r"- Read(error if not exits),
#"a"-Append(creates if not exits),
#"w"-Write(overwrites)(creates if not exits),
#"x"-Create(returns if exits)
#"t"-Text-Default value. Text mode
#"b"-Binary-binary mode
f = open("demofile.txt", "r")
print(f.read())
f = open("demofile.txt", "rb")
print(f.read())
#"""
"""
#By default the read() method returns the whole text,
#but you can also specify how many character you want to return:
#Return the 5 first characters of the file:
f = open("demofile.txt", "r")
print(f.read(5))
#"""
"""
#You can return one line by using the readline() method:
#Read first line of the file:
f = open("demofile.txt", "r")
print(f.readline())
#"""
"""
#Loop through the file line by line:
f = open("demofile.txt", "r")
for x in f:
    print(x)
#"""
"""
#To write to an existing file,
#you must add a parameter to the open() function
#Open the file "demofile.txt" and append content to the file:
f = open("demofile.txt", "a")
f.write("\nNow the file has one more line!")
f = open("demofile.txt", "r")
print(f.read())
#"""
"""
#Create a New File
#Create a file called "myfile.txt":
f = open("myfile2.txt", "x")
f.write("New File in Create mode with Python code..!\n")
f = open("myfile2.txt", "r")
print(f.read())
#Create a file called "myfile1.txt":
f = open("myfile1.txt", "a")
f.write("New File in Append mode with Python code..!\n")
f = open("myfile1.txt", "r")
print(f.read())
#Create a file called "myfile.txt":
f = open("myfile.txt", "w")
f.write("New File in Write mode with Python code..!\n")
f = open("myfile.txt", "r")
print(f.read())
#Delete a File
#To delete a file, you must import the OS module,
#and run its os.remove() function
#remove a file called "myfile2.txt":
import os
os.remove("myfile2.txt")
#Check if file exist, then delete it:
if os.path.exists("myfile1.txt"):
  os.remove("myfile1.txt")
else:
  print("The file 'myfile1.txt' does not exist")
#To delete an entire folder, use the os.rmdir() method:
#Remove the folder "myfolder": "os.rmdir("myfolder")"
#Note: You can only remove empty folders.
#"""
#Python MySQL
"""
#Start by creating a connection to the database.
#Use the username and password from your MySQL database:
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="7075"
)

print(mydb)
#"""
"""
#You can check if a database exist
#by listing all databases in your system
#by using the "SHOW DATABASES" statement:
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="7075"
)

mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)
#"""
"""
#you can try to access the database when making the connection:
#Try connecting to the database "world" and show tables
#If the database does not exist, you will get an error.
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="7075",
  database="test"
)
mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")
for x in mycursor:
  print(x)
#"""
"""
#Create a table named "customers" in the db "test"
#if table already exits, error will be raised.
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="7075",
  database="test"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
mycursor.execute("SHOW TABLES")
for x in mycursor:
  print(x)
#"""
"""
#Create primary key when creating the table:
#If the table already exists, use the ALTER TABLE keyword:
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="7075",
  database="test"
)
mycursor = mydb.cursor()
mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
mycursor.execute("SHOW TABLES")
for x in mycursor:
  print(x)
#"""
"""
#Insert a record in the "customers" table:
#If the table already exists, use the ALTER TABLE keyword:
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="7075",
  database="test"
)
mycursor = mydb.cursor()
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")
#Important!: Notice the statement: mydb.commit(). It is required to make the changes,
#otherwise no changes are made to the table.
#"""
"""
#To insert multiple rows into a table, use the executemany() method.
#The second parameter of the executemany() method is a list of tuples,
#containing the data you want to insert:
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="7075",
  database="test"
)
mycursor = mydb.cursor()
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")
#"""
"""
#You can get the id of the row you just inserted by asking the cursor object.
#Note: If you insert more that one row, the id of the last inserted row is returned.
#Insert one row, and return the ID:
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="7075",
  database="test"
)
mycursor = mydb.cursor()
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Michelle", "Blue Village")
mycursor.execute(sql, val)
mydb.commit()
print("1 record inserted, ID:", mycursor.lastrowid)
#"""
"""
#To select from a table in MySQL, use the "SELECT" statement:
#Select all records from the "customers" table, and display the result:
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="7075",
  database="test"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
#"""
"""
#If you are only interested in one row, you can use the fetchone() method.
#The fetchone() method will return the first row of the result:
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="7075",
  database="test"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchone()
print(myresult)
#"""
"""
#When selecting records from a table, you can filter the selection
#by using the "WHERE" statement:
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="7075",
  database="test"
)
mycursor = mydb.cursor()
sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
#"""
"""
#Prevent SQL Injection
#When query values are provided by the user, you should escape the values.
#This is to prevent SQL injections, which is a common web hacking technique to destroy or misuse your database.
#The mysql.connector module has methods to escape query values:
#Escape query values by using the placholder %s method:
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="7075",
  database="test"
)
mycursor = mydb.cursor()
sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )
mycursor.execute(sql, adr)
myresult =mycursor.fetchall()
for x in myresult:
  print(x)
#"""
"""
#Update Table
#Overwrite the address column from "Valley 345" to "Canyoun 123":
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="7075",
  database="test"
)
mycursor = mydb.cursor()
sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")
#use sql statements below to prevent sql injection
#sql = "UPDATE customers SET address = %s WHERE address = %s"
#val = ("Valley 345", "Canyon 123")
#"""
"""
#Delete Record
#You can delete records from an existing table
#by using the "DELETE FROM" statement:
#Delete any record where the address is "Mountain 21":
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="7075",
  database="test"
)
mycursor = mydb.cursor()
sql = "DELETE FROM customers WHERE address = 'Mountain 21'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")
#"""
"""
#Delete a Table
#You can delete an existing table by using the "DROP TABLE" statement:
#Delete the table "customers":
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="7075",
  database="test"
)
mycursor = mydb.cursor()
sql = "DROP TABLE customers"
mycursor.execute(sql)
#sql = "DROP TABLE IF EXISTS customers" used to check if exits.
#"""
