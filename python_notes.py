'''
MULTILINE COMMMENTS
'''
#COMMMENT LINE
'''
TO RUN PYTHON SCRIPT/FILE IN TERMINAL:
    1. Navigate to the current directory or folder
    2. ENTER the following command in your terminal
       python ./file.py (if earlier than python3)
       python3 file.py  (python3)
'''

'''
VARIABLES: place to store data
    initialization: create and name variable and set to some value
        name_of_variable = VALUE
    global: outside of a function in the main body of code, accessible everywhere
    local: inside of funcitions, only accessible within the function
'''

'''
DATA TYPES:
    numbers
    "strings" or 'strings'
    [l,i,s,t,s]
    (t,u,p,l,e,s)
    dictionary = {key : value,      #also known as maps
                 key2 : value2}
'''
print("Hello, world!")
print("Here are some python basics!\n")

'''
NUMBERS:
    follows order of operations
    Integer (int): positive and negative whole numbers
        signed int  %d
    Float: a number with a decimal
        float       %f
            x decimals %.xf
'''
x = 5       #integer
y = 2       #integer
z = 12.4    #float

# x OPERATOR y
x + y       #plus        +
x - y       #minus       -
x * y       #multiply    *
x / y       #divide      /
x % y       #mod         %
x ** y      #exponet     **
x // y      #floor       //

x += 1      #increment by 1
x = x + 1

x -= 1      #decrement by 1
x = x - 1

'''
STRINGS: the characters between "" or ''
    string      %s
    char        %c
    concat      +
    from end    -x

    print
        change end parameter    end (default = '\n')
'''
#number as string
five = "5"  #5 as a string
int-five = int(string-five) #number 5

#substrings
string = "sub-string"
substrxy = string[0:3]      #chars x to y    string[x:y]
substrlastx = string[-6:]   #last x chars    string[-x:]
substruptox = string[:-3]   #chars up to x   string[:-x]

length = len(string)        #length
string.capitalize()         #capitalize first
string.find(substrxy)       #get index of substring       string.find(substring)
string.isalpha()            #contains all letters?
string.isdigit()            #contains all numbers?
string.replace("sub","str") #replace old with new         string.replace(old,new)
string.strip()              #remove whitespace
string.split("-")           #parse into list with token   string.split(token)

#format print            print("stuff %s" % (input))
print("string of length %d: %s" % (length,string))
print("substring 0-3: %s\nsubstring last 6: %s\nsubstring minus last 3: %s\n"
    % (substrxy,substrlastx,substruptox))
print(VARIABLE, "rest of text")

'''
LISTS:
    can have multiple data types in one list
    mutable (can be changed)
    indexed 0
    concat  +

    print(*list, sep=",")   print entire list (' ' default sep)
    'sep'.join(list)        condense into string separated by sep
'''
#string to list
# to get some value from a list at index i
value = list[i]

some_list = ['l','i','s','t']

print(*some_list)           #print entire lists default sep=" "

len(some_list)               #length
max(some_list)               #max element
min(some_list)               #min element
'l' in some_list             #checks if item is in list     item in list
some_list[0] = 'l'           #replaces at index             list[index] = new_element
some_list[0:3]               #subset from x to y            list[x:y]
some_list.append('s')        #append                        list.append(element)
some_list.insert(0,'a')      #insert                        list.insert(index, element)
some_list.remove('a')        #remove                        list.remove(element)
some_list.sort()             #sort
some_list.reverse()          #reverse sort or               some_list.sort(reverse=True)
index = some_list.index("l") #returns index of item in list
del some_list[3]             #delete at index
tuple(some_list)             #convert into tuple

'''
TUPLES:
    immutable lists
    print(*tuple)   print tuple
'''
some_tuple = ('t','u','p','l','e')
print(*some_tuple, sep="")

length = len(some_tuple)     #length
max_val = max(some_tuple)     #max
min_val = min(some_tuple)     #min
list(some_tuple)    #convert tuple into list

print("length = %d\nmax_val = %c\nmin_val = %c\n"
    % (length,max_val,min_val))

'''
MAPS/DICTIONARIES:
    list of key value pairs of any data types
    cannot concat with +
'''
map = {"key" : "value1",
       "key2" : "value2"}

length = len(map)        #length
val1 = map.get("key")    #get value or map[key]
val1 = map["key"]

print("Map of length %d with value at key = %s" % (length,val1))

all_keys = map.keys()      #get all keys
all_values = map.values()    #get all values

print("all keys: ", all_keys)
print("all values: ", all_values, "\n")

del map["key"]  #delete key and value at key


'''
BOOLEANS: holds values of only True or False, often written as a conditional
'''
true-variable = True
false-boolean = False

'''
CONDITIONALS:
    ==, !=, >, >=, <, <=
    and, or, not

    BOOLEAN EXPRESSIONS
      AND (and) both expressions must be true
      OR (or) at least one expression must be true
      NOT (not) the opposite true/flips boolean

    Truth Table
       AND         |   OR          |   NOT
     T and T = T   | T or T = T    | not(T) = F
     T and F = F   | T or F = T    | not(F) = T
     F and T = F   | F or T = T    |
     F and F = F   | F or F = F    |

    if-then statements:
        if BOOLEAN CONDITION is met:
            then do this <- indent all the things you want to do
        elif BOOLEAN CONDITION: #if the previous condition(s) were not met, check this one
            then do this
        else:
            # otherwise do this
'''
BOOLEAN_CONDITION = True #set boolean variable to true
ANOTHER_BOOLEAN_CONDITION = True and False
if BOOLEAN_CONDITION:       #if true
    print("DO THE THING THAT METS THE CONDITION")#do this
elif ANOTHER_BOOLEAN_CONDITION:     #else if true
    print("DO THE OTHER THING THAT MEETS THIS CONDITION INSTEAD")#do this
else:       #else
    print("OTHERWISE DO THIS")  #otherwise do this


'''
LOOPS:
    range
        from 0 to x-1         range(x)
        from begin to end-1   range(begin,end)
        increment by step     range(begin,end,step)

    continue    skip to next iteration
    break       exit loop immediately
'''
xs = ['e','l','e','m','e','n','t','s']
for x in xs:
    #do stuff for every element in a list
    print(x, end="")

print('\n')

# repeat-times: repeats code some number of times
# This will print 0 1 2 3 4 5 6 7 8 9
for x in range(10): # <- don't forget this colon
    #below is the code that will be repeat <- remember to indent
    print(x, ' ', end="")


# This will print 0 1 2 3 4
counter = 0
while counter < 5:
    #below is the code that will be repeat <- remember to indent
    print(counter)
    #increment counter by 1
    counter = counter + 1

# repeat-until: repeats code until a CONDITION is met (meaning it is True)
done = False
while not(done):
    response = input("Keep going?")
    if response == 'yes':
        print("KEEP GOING")
    else:
        print("DONE")
        done = True

print("\n" * 2)

'''
FUNCTIONS:

DEFINE (def) - make a function
CALL - use the function you created or defined earlier

parameter: info you can pass or give to a function
return: output of a function
                   ________
        x         |        |        y
    parameter ->  |    f   | ->   return
     (input)      |________|     (output)
                   function
        x             x+5     =     y
        3             3+5     =     8

Examples:
    input()
    print()
    range()

'''
#function definition
def function_name(parameters):
    local = "this is a local string variable"
    print("This is where you do some fun stuff!")
    print("This code must be indented")
    ret = parameters
    return ret

global_variable = "this is a global string variable"
#function call
output = function_name()

'''
ANONYMOUS FUNCTIONS
    lambda arguments: expression
'''
#MAP,FILTER,REDUCE
int_list = [-3,-2,-1,0,1,2,3]
print(int_list)

#map function onto list    map(func, list)
squared = list(map(lambda x: x**2,int_list))
print(squared)

#filter in                 filter(cond, list)
whole_nums = list(filter(lambda x: x > 0,int_list))
print(whole_nums)

#reduce into single computation     reduce((lambda tmp,ret: op(tmp,ret)),list)
from functools import reduce
sum = reduce(lambda x,y: x + y, int_list)
print("Sum = %d\n" % sum)

'''
LIBRARIES and MODULES

    Libraries are a collection of functions we can call.

    import LIBRARY
'''
#always import libraries up top
import math
import random

#MATH library
# calling a function in math, type library then function_name
#     so we know where to look for the function we want to use
x = math.sqrt(16) #square root, expected 4
y = math.floor(123.325) #round down, expected 123
print(x)
print(y)

#RANDOM library
some_list = ["Data", "Mining", "Privacy", "SQL"]
pick = random.choice(some_list) #pick an item at random
print(pick)

'''
GET INPUT FROM USER:
    input()

    or

    import sys
    input = sys.stdin.readline()
'''
reponse = input("Prompt to User")

'''
FILES:
    modes
        read all contents    r    (r+ create if file DNE)
        write                w    (w+ create if file DNE)
        append to file       a    (a+ create if file DNE)
        create new file      x    (fails if already exists)
        text                 t
        binary               b
        read and write       +
'''
test_file = open("test.txt", "wb")    #open file   open(name_of_file, mode)
test_file.write(bytes("write stuff to test_file\n", 'UTF-8'))    #write to file
test_file.close()                     #close

test_file = open("test.txt", "r+")    #reopen file with dif mode
file_mode = test_file.mode            #mode
file_name = test_file.name            #name
contents = test_file.read()           #read from file
print("File %s in mode %s contains: %s\n"
    % (file_name, file_mode,contents))
test_file.close()

#delete file
import os
os.remove("test.txt")

#JSON Files (import json)
jsonFile = open("file.json", "r")
fileData = json.load(jsonFile) #use fileData (list of dicionaryies)
jsonFile.close()

'''
OBJECTS:
    attributes
        private     __attribute
        no value    None or "" or 0
'''
class SuperClass:
    __supAttribs = None

    #constructor
    def __init__(self, supAttribs):
        self.__supAttribs = supAttribs

    def set_supAttribs(self, supAttribs):
        self.__supAttribs = supAttribs

    def get_supAttribs(self):
        return self.__supAttribs

    def get_type(self):
        print("SuperClass")

    def toString(self):
        return "SuperClass with attributes {}".format(self.__supAttribs)

super_object = SuperClass("attrib values")    #create object/call constructor
print(super_object.toString())               #call function declared in class

#inheritance
class InheritedClass(SuperClass):
    __moreAttribs = ""

    def __init__(self, supAttribs, moreAttribs):
        self.__moreAttribs = moreAttribs

        #super class constructor
        super(InheritedClass, self).__init__(supAttribs)

    def set_moreAttribs(self, moreAttribs):
        self.__moreAttribs = moreAttribs

    def get_moreAttribs(self):
        return self.__moreAttrib

    def get_type(self):
        print("InheritedClass")

    def toString(self):
        return "InheritedClass with attributes {} and more {}".format(self.get_supAttribs(),
                                                                      self.__moreAttribs)

    #method overloading -- perform diff tasks based on parameters
    def multiple_supAttribs(self, num=None): #num=None means don't have to specify
        if num is None:
            print(self.get_supAttribs() + '\n')
        else:
            print((self.get_supAttribs() + '\n') * num)

sub_object = InheritedClass("super value", "attribs")
print(sub_object.toString())

sub_object.multiple_supAttribs(3)

#polymorphism
class ClassTest:
    def get_type(self, superClassOb):
        superClassOb.get_type()

test_super = ClassTest()
test_super.get_type(super_object)
test_super.get_type(sub_object)
