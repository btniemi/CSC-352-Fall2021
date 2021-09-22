import csv

my_dict = {}
# open the file in read mode
with open('North_America_Sports_Teams.csv', mode='r') as infile:
    # open a reader to the csv, the delimiter is a single space
    reader = csv.reader(infile, delimiter=',', skipinitialspace=True)
    # read the dictionary using dictionary comprehension, key is the first column and row is the rest of the columns
    my_dict = {key: row for key, *row in reader}
print(my_dict)
# abs()
print('------abs()------')
# abs(my_dict) does not work as this is not a number or integer which is what abs() takes

# all(iterable)
print('------all()------')
print(all(my_dict))  # returns a bool of true or false if iterable has values in it

# any(iterable)
print('------any()------')
print(any(my_dict))  # returns a bool of true or false if there at least one element in itterable

# bool(any types) returns true or false
print('------bool()------')
print(bool(my_dict))
def check_Key(dict, key):
    if key in dict.keys():
        print("Present, value = ", dict[key])
    else:
        print("Not present")
ans = check_Key(my_dict, '4')
ans2 = check_Key(my_dict, '200')

# zip(*iterables)
print('------zip()------')
# cant do zip need 2 list or iterables to tupel together
# bin()
print('------bin()------')
# cant do this either with list as it needs an integer to make it binary
# vars(object)
print('------vars()------')
# cant do needs an object that has a __dict__ attribute
# type() just returns the type
print('------type()------')
print(type(my_dict))  # returns the type of the param you give to it
# dir()
print('------dir()------')
print(dir(my_dict))  # returns valid attributes of the param given
# tuple(iterable)
print('------tuple()------')
a = tuple(my_dict)
print(a) # gives us the number of elements or keys of the dictionary as a tuple list
# setattr(object, name, value)
print('------setattr()------')
# cant do on a none object
# repr()
print('------repr()------')
# cant do on a none object
# range()
print('------range()------')
#cant do this with a dictionary as your looking for keys and values based off keys
# callable(object)
print('------callable()------')
b = callable(my_dict)
print(b)  # a dict is not callable
# chr(integer)
print('------char()------')
# this will work but not really necessary for a dict in this case
# classmethod(function)
print('------classmethod()------')
# only works with objects
# complex(real, imaginary)
print('------complex()------')
# wont work in this assignement because no need for complex numbers
# delattr()
print('------delattr()------')
# will only work with objects



#create seperate dict for state

#create seperate dict for city