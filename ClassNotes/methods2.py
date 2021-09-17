# 9/17/21 you gotta read over these slides and do your own research

std = type('student', (object,), dict(name='John', age=12))
print('type = ', type(std))
print('__name__ = ', std.__name__)
print('__bases__ = ', std.__bases__)
print('__dict__ = ', std.__dict__)

#dir() function will return the following attributes of the dynamic class created using the type() function
print('\n----dir()----')
a = dir(std)
print(a)

#tuple(iterable)
print('\n----tuple()----')
tpl = tuple()
print('empty tuple: ', tpl)
numbers_list = [1,2,3,4,5]
print('converting list into tuple: ', tuple(numbers_list))
numbers_tuple = {1,2,3,4,5}
print('converting set into tuple: ', tuple(numbers_tuple))
numbers_dict = {1:'one', 2:'two', 3:'three'}
print('converting dictionary into tuple: ', tuple(numbers_dict))
greet = 'Hello'
print('converting string into tuple: ', tuple(greet))

#setattr(object, name, value)
print('\n----setattr()----')
class student:
    firstName = 'James'
    lastName = 'Bong'

std1 = student()
print('First Name:', std1.firstName)
print('Last Name:', std1.lastName)
setattr(std1, 'firstName', 'Bill')
setattr(std1, 'lastName', 'Gates')
print("after setting attributes")
print('First Name:', std1.firstName)
print('Last Name:', std1.lastName)
#assigns a new attribute
setattr(student, 'age', 25)
print("after setting attributes")
print('student.age =', student.age)
s = student()
print('s.age = ', s.age)

#went to fast missed notes here

#repr() what is this???
print('\n----repr()----')
print(repr(10))
print(repr(10.5))
print(repr(True))
print(repr(4+2))

#range()
print('\n----range()----')
num_range = range(5)
print(type(num_range))
print(num_range)
print("values = ", num_range[0], num_range[1], num_range[2], num_range[3], num_range[4])
#better way to print this with a list or compression one by one maybe
print(0 in num_range)
print(4 in num_range)
print(5 in num_range)
print(6 in num_range)
print(list(range(5)))
print(tuple(range(5)))
print(set(range(5)))

num_range1 = range(1,5)
print('range(1,5) = ', list(num_range1))
num_range2 = range(1,10,2)
print('range(1,10,2) = ', list(num_range2))
num_range3 = range(0,20,5)
print('range(0,20,5) = ', list(num_range3))
num_range4 = range(-5,-1)
print('range(-5,-1) = ', list(num_range4))
num_range5 = range(-5)
print('range(-5) = ', list(num_range5))

num_range1 = range(1,5)
num_range2 = range(1,10,2)
num_range3 = range(1,5)
print(num_range1 == num_range2)
print(num_range1 == num_range3)

for i in range(5):
    print(i)