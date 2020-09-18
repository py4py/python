# This is one line comment in python
''' This is multiline
    comment '''
""" And this is also multiline
    comment """

#################### MODULES/IMPORT ####################
""" How to import and use modules """

import os
sysinfo = os.getlogin()

import os as sysfunc
sysinfo = sysfunc.getlogin()

from os import getlogin, getpid
sysinfo = getlogin()
myuid = getpid()

getlogin = "mylogin"
from os import *  # VERY BAD PRACTICE - os has function 'getlogin'
print(getlogin)   # now this is function 


#################### FUNCTIONS ####################
""" How to declare functions and use them """

def double(x):
    return x * 2

def use_function(f):
    return f(1)  # calls function

double_of_2 = double(2)  # = 4
print(double_of_2)

function_f = double   # reference to function double
value = use_function(function_f)  # = 2
print(value)

x = lambda z: z * 2
print(x(2))  # = 4

y = use_function(lambda z: z * 2)
print(y)  # returns 2

def custom_message(msg = "default msg"):
    print(msg)
    
custom_message("custom msg")
custom_message()
custom_message(msg="custom2")


#################### STRINGS/CHAINS ####################
string = "Some text fo test"
len(string)  # returns length of string

tab_string = "\t"
len(tab_string)  # = 1

raw_string_no_tab = r"\t"
len(raw_string_no_tab)  # = 2

multi_line_string = """1 line
2 line
3 line"""

name = "John"
surname = "Mike"

fullname = name + " " + surname
fullname2 = "{0} {1}".format(name, surname)
fullname3 = f"{name} {surname}"  # the newest the best and the fastest way in python


#################### EXCEPTIONS ####################
try:
    print(0/0)
except ZeroDivisionError:
    print("Did you divided by zero?")
    
#################### LISTS ####################
int_list = [1,2,3,4]
dif_list = ["string", 0.1, False]
list_list = [int_list, dif_list, []]

int_len = len(int_list)  # = 4
int_sum = sum(int_list)  # = 10

zero =         int_list[0]  # = 1
one =          int_list[1]  # = 2
last =         int_list[-1]  # = 4
before_last =  int_list[-2]  # = 3

first_two =          int_list[:2]   # [1,2]
two_to_end =         int_list[1:]   # [2,3,4]
two_to_three =       int_list[1:3]  # [2,3]
last_two =           int_list[-2:]  # [3,4]
no_first_and_last =  int_list[1:-1] # [2,3]
copy_of_int_list =   int_list[:]    # [1,2,3,4]

every_second = int_list[::2]    # [1,3]
three_to_two = int_list[2:0:-1] # [3,2]

1 in int_list  # true
10 in int_list # false

int_list.extend([5,6])  # int_list is now [1,2,3,4,5,6]
int_list2 = int_list + [7,8]  # [1,2,3,4,5,6,7,8]

int_list2.append(9) # [1,2,3,4,5,6,7,8,9]

a, b = [10, 20]  # a = 10, b = 20
_, b = [10, 20]  # a has beeen omitted, b = 20


#################### TUPLES ####################
a_list = [1,2]
a_tuple = (1,2)
b_tuple = 5,6

try:
    a_tuple[1] = 3
except TypeError:
    print("We can't modify tuple in python")
    
def tuple_magic(x,y):
    return (x+y), (x*y)

test = tuple_magic(2,3)    # = (5,6)
t1, t2 = tuple_magic(5,10) # t1 == 15, t2 = 50

x, y = 1, 2
x, y = y, x  # python way of changing values of variables - now x == 2, y == 1

#################### defaultdict ####################

#################### Counter ####################

#################### Set ####################

#################### CONTROL FLOW ####################

#################### LOGIC VALUES ####################

#################### SORTING ####################

#################### FOLDING LISTS ####################

#################### AUTOMATIC TESTS AND ASSERT ####################

#################### CLASES ####################

#################### INTERABLE OBJECT AND GENERATORS ####################

#################### RANDOMNESS ####################

#################### REGULAR EXPRESSIONS ####################

#################### PACKING ARGUMENTS - ZIP ####################

#################### NAMED AND UNNAMED ARGUMENTS ####################

#################### TYPE ANNOTATIONS ####################

#################### HOW TO WRITE TYPE ANNOTATIONS ####################
