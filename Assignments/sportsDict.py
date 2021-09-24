import csv

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
# cant do zip need 2 list or iterables to tuple together
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
# list_values_to_check = {'Anaheim', 'Arlington', 'Atlanta', 'Austin', 'Baltimore', 'Boston', 'Buffalo', 'Calgary', 'Carson', 'Charlotte', 'Chester', 'Chicago', 'Cincinnati', 'Cheveland', 'Columbus', 'Commerce City', 'Dallas', 'Denver', 'Detroit', 'East Rutherford', 'Edmonton', 'Fort Lauderdale', 'Foxborough', 'Frisco', 'Green Bay', 'Hamilton', 'Harrison', 'Houston', 'Indianapolis', 'Inglewood', 'Jacksonville', 'Kansas City', 'Landover', 'Las Vegas', 'Los Angeles', 'Memphis', 'Miami', 'Milwaukee', 'Minneapolis', 'Montreal', 'Nashville', 'New Orleans', 'New York', 'Newark', 'Oakland', 'Oklahoma City', 'Orlando', 'Ottawa', 'Philadelphia', 'Phoenix', 'Pittsburgh', 'Portland', 'Raleigh', 'Regina', 'Sacramento', 'Salt Lake City', 'San Antonio', 'San Diego', 'San Francisco', 'San Jose', 'Sandy', 'Santa Clara', 'Seattle', 'St. Louis', 'St. Paul', 'St. Petersburg', 'Sunrise', 'Tampa', 'Toronto', 'Uniondale', 'Vancouver', 'Washington', 'Winnipeg'}

# search for particular value
value = input("Name a city (case sensitive): ")
# get the list that contains the given value
list_of_keys = [key for key, list_of_values in my_dict.items() if value in list_of_values]
if list_of_keys:
    print('value', value, 'exists in the dictionary at these keys', list_of_keys)
    # you can print the values if you print(my_dict['key_desired']) see if you can get that to work
    # you could loop this to append to a new dictionary as well most likely
    # also can loop this till done searching
else:
    print("City requested does not exist in the dictionary")

#create seperate dict for city
# search for particular value
value = input("Name a State (case sensitive): ")
# get the list that contains the given value
list_of_keys = [key for key, list_of_values in my_dict.items() if value in list_of_values]
if list_of_keys:
    print('value', value, 'exists in the dictionary at these keys', list_of_keys)
    # you can print the values if you print(my_dict['key_desired']) see if you can get that to work
    # you could loop this to append to a new dictionary as well most likely
    # also can loop this till done searching
else:
    print("State requested does not exist in the dictionary")