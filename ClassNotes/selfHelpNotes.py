#think of example: anagram program *have to sort
s = 'hel'
s1 = 'harry'
for i, j in zip(s, s1):
    if i != j:
        print("False")
    else:
        print("True")

# zip(*iterables) –> A zip object yielding tuples until an input is exhausted.
x = list(zip('abcdefg', range(3), range(4)))
print(x)
# [('a', 0, 0), ('b', 1, 1), ('c', 2, 2)]
# The zip object yields n-length tuples, where n is the number of iterables passed as positional arguments to zip().
# The i-th element in every tuple comes from the i-th iterable argument to zip().
# This continues until the shortest argument is exhausted.
