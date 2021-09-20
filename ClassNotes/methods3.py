# 9/20/21

# callable(object)
print('----callable()----')
print("is str callable? ", callable(str))
print("is len callable? ", callable(len))
print("is list callable? ", callable(list))
num = 10
print("is variable callable? ", callable(num))


class student:
    def greet(self):
        print("Hello there")


std = student()
print("is student class callable? ", callable(student))
print("is student.greet() callable? ", callable(std.greet))
print("is student instance callable? ", callable(std))


class student:
    def greet(self):
        print("Hello there")

    def __call__(self):
        print("hello, i am a student")


std1 = student()
print("is student instance callable? ", callable(std1))
print(std1())

# chr(integer)
print('\n----chr()----')
print("the character value of 65 is: ", chr(65))
print("the character value of 90 is: ", chr(90))
print("the character value of 97 is: ", chr(97))
print("the character value of 122 is: ", chr(122))
print("the character value of 1220 is: ", chr(1220))
print("the character value of 1100 is: ", chr(1100))
# print(chr(-1)) does not work not in range

# classmethod(function)
print('\n----classmethod()----')


class student:
    name = "John"

    def show_name(self):
        print('The students name is ', self.name)


student.show_name = classmethod(student.show_name)
student.show_name()

# complex(real, imaginary)
# complex(string)
print('\n----complex()----')  # what would you ever use this for look up
cnum = complex()
print(cnum)
print(type(cnum))
cnum = complex(2, 5)
print(cnum)
cnum = complex(5)
print(cnum)
cnum = complex(-5)
print(cnum)
print('str into complex numbers')
cnum = complex('5-3j')
print(cnum)
cnum = complex('3+j')
print(cnum)
cnum = complex('3')
print(cnum)
cnum = complex('+j')
print(cnum)
cnum = complex('-j')
print(cnum)

# delattr()
print('\n----delattr()----')


class student:
    name = 'Braedon'
    age = 27


print(dir(student))
delattr(student, 'age')  # same thing is del(student.age)
print("after the delattr() method is called:")
print(dir(student))

# dict(**kwarg)
print('\n----dict()----')
emptydict = dict()
print(emptydict)
numdict = dict(I='one', II='two', III='three')
print(numdict)
# numdict1 = dict(1='one', 2='two', 3='three') #cant do this with integers to specify keys in dictionary wont run

numdict = dict([(1, 'one'), (2, 'two'), (3, 'three')])
print("dict1= ", numdict)
# missed stuff here for stuff in notes but know this stuff already


numdict = dict({'I': 'one', 'II': 'two', 'III': 'three'})  # passing mapping object
print(numdict)
