# more dictionary exercises start of the slides

# matching key/values in two dictionaries
x = {'key1': 1, 'key2': 3, 'key3': 2}
y = {'key1': 1, 'key2': 2, 'key3': 2}
for (key, value) in set(x.items()) & set(y.items()):
    print('%s: %s is present in both x and y' % (key, value))

print('xyz')
x = {'key1': 1, 'key2': 3, 'key3': 2, 'key4': 4}
y = {'key1': 1, 'key2': 2, 'key3': 2, 'key4': 0}
z = {'key1': 1, 'key2': 2, 'key3': 0, 'key4': 4}
for (key, value) in set(x.items()) & set(y.items()) & set(z.items()):
    print('%s: %s is present in x, y, and z' % (key, value))

print('xyza')
x = {'key1': 0, 'key2': 3, 'key3': 2, 'key4': 4, 'key5': 6}
y = {'key1': 1, 'key2': 2, 'key3': 2, 'key4': 4, 'key5': 6}
z = {'key1': 1, 'key2': 2, 'key3': 2, 'key4': 0, 'key5': 6}
a = {'key1': 1, 'key2': 2, 'key3': 0, 'key4': 4, 'key5': 6}
for (key, value) in set(x.items()) & set(y.items()) & set(z.items()) & set(a.items()):
    print('%s: %s is present in x, y, z, and a' % (key, value))

print('xyzab')
x = {'key1': 1, 'key2': 3, 'key3': 2, 'key4': 4, 'key5': 0, 'key6': 8}
y = {'key1': 1, 'key2': 2, 'key3': 2, 'key4': 4, 'key5': 6, 'key6': 8}
z = {'key1': 0, 'key2': 2, 'key3': 0, 'key4': 4, 'key5': 6, 'key6': 8}
a = {'key1': 1, 'key2': 2, 'key3': 2, 'key4': 0, 'key5': 6, 'key6': 8}
b = {'key1': 1, 'key2': 2, 'key3': 2, 'key4': 4, 'key5': 6, 'key6': 8}
for (key, value) in set(x.items()) & set(y.items()) & set(z.items()) & set(a.items()) & set(b.items()):
    print('%s: %s is present in x, y, z, a, and b' % (key, value))

print('xyzabc')
x = {'key1': 1, 'key2': 3, 'key3': 2, 'key4': 4, 'key5': 6, 'key6': 8, 'key7': 69}
y = {'key1': 1, 'key2': 2, 'key3': 2, 'key4': 4, 'key5': 6, 'key6': 7, 'key7': 69}
z = {'key1': 1, 'key2': 2, 'key3': 2, 'key4': 4, 'key5': 5, 'key6': 9, 'key7': 69}
a = {'key1': 4, 'key2': 2, 'key3': 3, 'key4': 1, 'key5': 6, 'key6': 8, 'key7': 69}
b = {'key1': 1, 'key2': 2, 'key3': 2, 'key4': 4, 'key5': 6, 'key6': 0, 'key7': 69}
c = {'key1': 1, 'key2': 2, 'key3': 2, 'key4': 4, 'key5': 6, 'key6': 8, 'key7': 69}
for (key, value) in set(x.items()) & set(y.items()) & set(z.items()) & set(a.items()) & set(b.items()) & set(c.items()):
    print('%s: %s is present in x, y, z, a, b, and c' % (key, value))

# create dictionary using python

from pprint import pprint

dict_nums = dict(x=list(range(11, 20)), y=list(range(21, 30)), z=list(range(31, 40)))
pprint(dict_nums)
print(dict_nums["x"][4])  # accessing a specific element in that dictionary
print(dict_nums["y"][4])
print(dict_nums["z"][4])
for k, v in dict_nums.items():  # prints all numbers in that keys values from specific dictionary
    print(k, "has values", v)

dict_nums_4_7 = dict(x=list(range(11, 20)), y=list(range(21, 30)), z=list(range(31, 40)), a=list(range(41, 50)),
                     b=list(range(51, 60)))
pprint(dict_nums_4_7)
print(dict_nums_4_7['x'][4])
print(dict_nums_4_7['x'][6])
print(dict_nums_4_7['y'][4])
print(dict_nums_4_7['y'][6])
print(dict_nums_4_7['z'][4])
print(dict_nums_4_7['z'][6])
print(dict_nums_4_7['a'][4])
print(dict_nums_4_7['a'][6])
print(dict_nums_4_7['b'][4])
print(dict_nums_4_7['b'][6])

# filter a dictionary
marks = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
print("Original Dictionary:")
print(marks)
print("marks greater than 170:")
result = {key: value for (key, value) in marks.items() if value >= 170}
print(result)

# put it all together create a list of key value pairs where keys are from a list
# https://www.geeksforgeeks.org/python-program-to-create-a-list-using-custom-key-value-pair-of-a-dictionary/
