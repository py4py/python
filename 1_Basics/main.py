""" This examples are based on various tutorials and books about python """

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

#################### DICTIONARIES ####################
empty_dict = {}
empty_dict2 = dict()
numbers = { "one": 1, "two": 2}
two = numbers['two']

there_is_one = "one" in numbers  # true
there_is_three = "three" in numbers  # false

one_value = numbers.get("one", 0)  # = 1
default_value = numbers.get("xxxxx")  # = None

numbers_keys = numbers.keys()
numbers_values = numbers.values()
numbers_items = numbers.items()

"one" in numbers_keys  # true but not good way in python to check
"one" in numbers  # python way of checking keys
1 in numbers_values  # true - but slow and only way to check it


#################### defaultdict ####################
"""Better dictionary management"""

from collections import defaultdict

words = ["one","someone", "anyone", "noone"]

word_count = defaultdict(int)  # int() generates value
for word in words:
    word_count[word] += 1
    
list_dict = defaultdict(list)  # function list() generates empty list
list_dict[2].append(1)  # now list contains {2: [1]}

dict_dict = defaultdict(dict)  # function dict() generates empty dictionary
dict_dict["one"]["first"] = "someone"   # { "one": { "first": "someone"}}

lambda_dict = defaultdict(lambda: [0, 0])
lambda_dict[2][1] = 1  # {2: [0,1]}

#################### Counter ####################
from collections import Counter
count = Counter([1,1,2,3,4,5,2])  # will count number of elements and return in form of dictionary
print(count)

word_count2 = Counter(words)
print(word_count2)

for word, count in word_count2.most_common(10):
    print(word, count)

#################### Set ####################
s = set()
s.add(1) # {1}
s.add(2) # {1,2}
s.add(2) # {1,2} only unique values - 2 is already there

stopword = ["asd","zxc","qwe","rty","fgh"]
"iop" in stopword  # returns false, but operation requires to check every element

stopword_set = set(stopword)
"iop" in stopword_set  # checking operation is very fast.

numbers2 = [1,1,2,3,4,3,3,2,2,2]
number2_set = set(numbers2)  # gets unique values from number2 list
print(numbers2)
print(number2_set)

#################### CONTROL FLOW ####################
if 1>2:
    msg = "no"
elif 1>3:
    msg = "no"
else:
    msg = "yes"
    
quick_if = "one" if x == 1 else "not one"

i = 0
while i<10:
    print(f"{i} is less than 10")
    i += 1
    
for i in range(10):  # range(10) means numbers 0,1,...,9
    print(f"{i} is less than 10")
    
for i in range(10):
    if i == 3:
        continue  # move immediately to next iteration
    if i == 5:
        break     # stop loop
    print(i)


#################### LOGIC VALUES ####################
""" This elements are false: False, None, [], {}, "", set(), 0, 0.0. Nearly every other element is true """
x = None
x == None  # BAD PRACTICE this is NOT python way of checking if variable is None
x is None  # this is python way of checking if variable is None

first_char = 1 and 2 # command and returns second value if first is true

safe_x = x or 0

safe_x = x if x is not None else 0

all([True, 1, {3}])  # True, all values are true
all([True, 1, {}])   # False, {} is false
any([True, 1, {}])   # True, first value is true
all([])              # True, no elements that are false
any([])              # False, no elements that are true


#################### SORTING ####################
num = [4,1,-2,3]
num_copy_sort = sorted(num) # copy and sorts list
num.sort() # sorts num list

num_copy_sort_reverse = sorted(num, key=abs, reverse=True) # sorts value from higher to lower
print(num_copy_sort_reverse)


#################### FOLDING LISTS ####################
""" How to write lists in one line - the fastest lists """

even_numbers = [x for x in range(5) if x % 2 == 0]  # [0,2,4]
squares      = [x * x for x in range(5)]            # [0,1,4,9,16]
even_squares = [x * x for x in even_numbers]        # [0,4,16]

square_dict = {x: x * x for x in range(5)}  #{0:0, 1:1, 2:4, 3:9, 4:16}
square_set = {x * x for x in [1,-1]} # {1}

zeros = [0 for _ in even_numbers]

pairs = [(x,y)
         for x in range(10)
         for y in range(10)]  # 100 pairs (0,0) (0,1) .... (9,8), (9,9)

increasing_pairs = [(x,y)
                    for x in range(10)
                    for y in range(x+1, 10)]

#################### AUTOMATIC TESTS AND ASSERT ####################
assert 1 + 2 == 3
assert 1 + 1 == 2, "1+1 = 2"  # assert with alternate message

def min_item(x):
    return min(x)

assert min_item([1,-10,234,3]) == -10

def min_item(x):
    assert x, "List need to have values"
    return min(x)


#################### CLASSES ####################
class Block:
    """Class, should be described here"""
    
    def __init__(self, count = 0):
        self.count = count
        
    def __repr__(self):
        return f"Should return a printable representation of the object"

    def read(self):
        return self.count
    
    def reset(self):
        self.count = 0


# The derived class inherits all the features of the base class.
class NewerBlock(Block):
    #This class has the same functions as Block
    
    # except this - reset function does nothing
    def reset(self):
        pass


#################### INTERABLE OBJECT ####################
names = ["Jon", "Mark", "Bob", "Sara"]

# BAD PRACTICE
for i in range(len(names)):
    print(f"name {i} is {names[i]}")
    
# BAD PRACTICE
i = 0
for name in names:
    print(f"name {i} is {names[i]}")
    i += 1
    
# GOOD PRACTICE
for i, name in enumerate(names):
    print(f"name {i} is {name}")

#################### RANDOMNESS ####################
import random
random.seed(10) # thanks to this we receive alwayes the same results

four_uniform_randoms = [random.random() for _ in range(4)] # generates random numbers between 0 and 1

random.randrange(10) # will draw number between range(10)
random.randrange(3,6) # will draw number between range(3,6)

up_to_ten = [1,2,3,4,5,6,7,8,9,10] 
random.shuffle(up_to_ten) # shuffles list
print(up_to_ten)

my_best_friend = random.choice(["one", "two", "three"])  # draws from list

lottery_numbers = range(60)
winning_numbers = random.sample(lottery_numbers, 6)
print(winning_numbers)

four_with_replacemet = [random.choice(range(10)) for _ in range(4)]
print(four_with_replacemet)

#################### REGULAR EXPRESSIONS ####################
import re

re_examples = [                            # All examples generates logic true, because:
    not re.match("a", "cat"),                 # word cat doesn't start with a;
    re.search("a", "cat"),                    # word cat contains letter a;
    not re.search("c", "dog"),                # word dog doesn't contains letter c;
    3 == len(re.split("[ab]", "carbs")),      # word carbs after splitting on letters a or b gives list ['c','r','s'];
    "R-D-" == re.sub("[0-9]", "-", "R2D2")    # the numbers are replaced by dashes.
    ]

#################### PACKING ARGUMENTS - ZIP ####################
list1 = ['a','b','c']
list2 = [1,2,3]

# zip generates result only then, when is needed (lazy function). It can be used like that:
[pair for pair in zip(list1, list2)]  # A list is generated [('a', 1), ('b', 2), ('c', 3)]

assert [pair for pair in zip(list1, list2)]  == [('a', 1), ('b', 2), ('c', 3)]

pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs)

letters, numbers = zip(('a', 1), ('b', 2), ('c', 3))

def add(a,b): return a + b

add(1,2)  # returns 3
try:
    add([1,2])
except TypeError:
    print("function requires 2 arguments")
add(*[1,2]) # returns 3

#################### NAMED AND UNNAMED ARGUMENTS ####################
def magic(*args, **kwargs):
    print("unnamed arguments:", args)
    print("named arguments:", kwargs)
    
magic(1,2,key="word", key2="word2")

#################### TYPE ANNOTATIONS ####################
def add(a,b):
    return a + b

try:
    add(10, "five")
except TypeError:
    print("can't add number to string chain")
    
def add(a: int, b: int) -> int:  # type annotataions informs what type of data should be in input and output
    return a + b                 # makes code more readable but may also make code more uglier

# custom types
from typing import List
Vector = List[float]

def dot_product(x: Vector, y: Vector) -> float: ...  # 3 dots lets you omit function definition