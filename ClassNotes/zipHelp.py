numbers = [1, 2, 3, 4, 5]
words = ['one', 'two', 'three', 'four', 'five']

res = zip(numbers, words)
print(list(res))

res1 = zip(numbers, words)  # has to be its own variable created to work in calling it to print
res_set = set(res1)
print(res_set)

number_list = [1, 2, 3]
str_list = ['one', 'two', 'three']

# No iterables are passed
result = zip()

# Converting iterator to list
result_list = list(result)
print(result_list)

# Two iterables are passed
result = zip(number_list, str_list)

# Converting iterator to set
result_set = set(result)
print(result_set)

# unzipping
coordinate = ['x', 'y', 'z']
value = [3, 4, 5]

result = zip(coordinate, value)
result_list = list(result)
print(result_list)

c, v = zip(*result_list)
print('c =', c)
print('v =', v)
