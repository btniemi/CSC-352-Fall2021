# methods are the verbs or programing

# abs()
print('this is abs()')
print("Absolute value of -10 is", abs(-10))
print("Absolute value of +10 is", abs(10))
print("Absolute value of -10.33 is", abs(-10.33))
print("Absolute value of 4 - 3j is", abs(4 - 3j))

print("Absolute value of -ob10011 is", abs(-0b10011))  # binary
print("Absolute value of -0o23 is", abs(-0o13))  # octal
print("Absolute value of -0x42 is", abs(-0x42))  # hex

# all(iterable)
print('\nthis is all()')
lst = []
print(all(lst))  # returns True for empty list
nums = [1, 2, 3, -4, -5]
print(all(nums))  # returns true
nums2 = [0, 1, 2, 3]
print(all(nums2))  # returns false because of 0
data = [1, 'phone', 12.5, 5, False]
print(all(data))  # returns false because of false
# demonstrates all() with strings
print(all('python'))
print(all(''))
print(all('False'))
# demonstrates all() with dictionaries
numsdict = {1: 'one', 2: 'two', 3: 'three'}
print(all(numsdict))  # returns true
numsdict2 = {0: 'zero', 1: 'one', 2: 'two', 3: 'three'}
print(all(numsdict2))  # returns false for 0

# any(iterable)
print('\nthis is any()')
list = []
print(any(list))  # returns false
nums = [0]
print(any(nums))  # returns false
nums2 = [0, 1, 2, 3, 4, 5]
print(any(nums2))  # returns true
nums3 = [0, False]
print(any(nums))  # returns false
nums4 = [0, 1, False]
print(any(nums4))  # returns True

# bool(any types) returns true or false for this
print('\nthis is bool()')
value = [0]
print("Boolean of [0] is: ", bool(value))
value = 0
print("Boolean of 0 is: ", bool(value))
value = 1
print("Boolean of 1 is: ", bool(value))
value = -1
print("Boolean of -1 is: ", bool(value))
value = None
print("Boolean of None is: ", bool(value))
value = True
print("Boolean of True is: ", bool(value))
value = False
print("Boolean of False is: ", bool(value))
value = 'a string'
print("Boolean of 'a string' is: ", bool(value))

# zip(*iterables)
#https://www.programiz.com/python-programming/methods/built-in/zip
# print('\nthis is zip()')
# numbers = [1, 2, 3]
# str_numbers = ['one', 'two', 'three']
# res = zip(numbers, str_numbers)
# print(list(res))
# print(list(res1)) #how to print a zip as a list

# numbers = [1, 2, 3]
# str_numbers = ['one', 'two', 'three']
# roman_numbers = ['I', 'II', 'III']
# result = zip(numbers, str_numbers, roman_numbers)
# res = list(result)
# print(result)
# print(res)
#
# teams = ["India", "England", "NZ", "Aus"]
# capital = ["Kohli", "Root", "Williamson", "Smith"]
# zipped = zip(teams, capital)
# zipList = list(zipped)
# print(zipList)

# bin()
print('\nthis is bin()')
print("binary equivalent of 5 is: ", bin(5))
print("binary equivalent of 5 is: ", bin(10))
# print("binary equivalent or A is: ", bin('A')) #wont work


# vars(object)
print('\nthis is vars()')


class student:
    def __init__(self):
        self.name = ''
        self.age = 0


std = student()
print(vars(std))
std.name = "Bill"
std.age = 18
print(vars(std))

# print(vars('Hello World')) #raises typeerror
# print(vars(10))# raises typeerror

# type() just returns the type
print('\nthis is type()')
lang = 'python'
nums = [1, 2, 3, 4]
nums_dict = {"one": 1, "two": 2, "three": 3}
print(type(lang))
print(type(nums))
print(type(nums_dict))
