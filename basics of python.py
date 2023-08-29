 
         # BASICS OF PYTHON 

# Python is a programming language. It can quickly create and manage data structures, allowing you to analyze and manipulate complex data sets.

          # DATA TYPES
     # Mostly used datatypes are:

# integer
# float
# string
# boolean

# some examples of datatypes are:

print(56)  # integer

# Print is a keyword and used to get output and debug the code.
# we will not use the inverted commas in this datatype because any number or integer value is universal.
# If it is in quotes, it will be read as a piece of text, the symbol itself with no value, so no calculations can be carried out with it.

print("World is nothing, but an exam")  # string

# compiler can't read the inverted comas statements we can write any thing in coma's.

print(33.56)   # float

# float values are those which contain decimal point.

print("true")   # boolean

# boolean tell us about true or false conditions

          # ARITHEMETIC OPERATIONS
# + , - , * , / , %  these signs called arithemetic operations
# Some examples are:

print(45+78)   # Addition
print(107-67)   # Subtraction
print(34*7)   # Multiplication
print(35/5)   # Division
print(23%2)   # remainder or modulo

     # We can also use VARIABLES :-
# Some examples of arithmetic operations by using variables.
#  = this sign is known as assignment operation used to assign any value to variable

a=8
b=50
c=a+b   # Addition
print(c)
# we can also find the datatypes of variables
print(type(c))   # class int

c=a-b   # Subtraction
print(c)
print(type(c))   # class int

d=10.45
m=15.9
h=d*m   # Multiplication
print(h)
print(type(h))   # class float

l=70
r=50
s=l/r   # Division
print(s)
print(type(s))   # class float

s=l%r   # Remainder 
print(s)
print(type(s))   # class int

     # we can also use MULTIPLE ARITHEMETIC OPERATIONS in one line:

a=50
b=80
c=70
d=(b*c+a)   # multiple operations
print(d)
print(type(d))   # class int

          # TYPE CASTING
# It is the method to convert the variable datatype into a certain datatype in order to perform the required operation by user.
# examples for type casting are:

p=25.5
print("before type casting",type(p))
p=str(p)
print("after type casting", type(p))
# In this example, we did type casting, in which we converted float into integer datatype
# keep in mind that, string datatype will not change into int or float instead, int, flaot can change into string.

z=("I feel anxiety nowadays")
print("before TC", type(z))
z=bool(z)
print("after TC", type(z))
# In this example, we did change from string to boolean 

          # INDEXING
# indexing is a process of accessing a specific element in a sequence.For example sort numbers assigning to the table of content in a books
# indexing always start with 0 in python
# we will also use square bracket to represent the indexes
# some exampels are:

name="Daniya Saqib"
print(name[5])   # square bracket represent the index 

# for easy to understand   name[starting index : ending index : steps]

print(name[4: ])   # it tells that text start from 4 index to end
print(name[0:6])   # 0 index to 6 
print(name[0:11:4])   # it means from index 0 to 11 skip 3,3 values 
print(name[1: :2])   # from 1 index to end skip 1,1 values
print(name[::-1])   # To opposite the name

          # CONDITIONAL STATEMENTS
# conditional statements provide a way to make decesions in your program and execute different codes based on those decisions
# If condition will true then it will execute otherwise it will stops the execution
# Mostly used conditional statements are: if , elif , else
# some examples are:

num=5
if(num>0):
    print("Number is positive")
else:
    print("Number is negative")
# It is the example of if_else now we will see the use of elif

a=20
b=6
if(a<b):
    print("statement is false")
elif(a>b):
    print("statement is true")   # it will execute and execution will stop here
elif(a>3):
    print("statement is true but not execute")
else:
    print("if all fails")

          #LOOPS
# looping means repeating something over and over until a particular condition is satisfied.
# There are 3 loops for, while, do-while. mostly used loops are for and while.
# some examples are:

for i in range(101):
    print(i)
    i=i+1

i=0
while(i<=50):
    print(i)
    i=i+1

          # FUNCTIONS
# Function is a block of code which only runs when it is called.() these brackets are used for function .
# mostly used functions are of two types built in and user-defined function
# built in functions are those that are already defined in python libraries and we can call them directly.eg.print,input etc
# user defined are those that we define ourselves in our programm.
  
def addition(a,b):
    #a=56  
    #b=65
    return(a+b)
# function calling
print (addition(56,65))





    









