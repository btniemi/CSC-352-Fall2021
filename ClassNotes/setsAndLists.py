names = set()
names.add("Michele")
names.add("Robin")
names.add("Michele")
print(names)

names2 = ["Michele", "Robin", "Sara", "Michele"]
print(names2)

names3 = ["Michele", "Robin", "Sara", "Michele"]
names3 = set(names3)
names3 = list(names3)
print(names3)

#next mission
names4 = ["Zavvh", "Rob", "Sarah", "Zavvh"]
names4 = set(names4)
names4 = list(names4)
print(names4)

g = []
if not g:
    print("List is empty")

#sum items in a list
def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers
print(sum_list([1,2,-8]))

#multiply
def multiply_list(items):
    tot = 1
    for x in items:
        tot *= x
    return tot
print(multiply_list([1,2,-8]))

#largest number in the list
def max_num_in_list(list):
    max = list[0]
    for a in list:
        if a > max:
            max = a
    return max
print(max_num_in_list([1,2,-8,0]))

#smallest number in list
def min_num_in_list(list):
    min = list[0]
    for a in list:
        if a < min:
            min = a
    return min
print(min_num_in_list([1,2,-8,0]))

#words longer than n
def long_words(n, str):
    word_len = []
    txt = str.split(" ")
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len
print(long_words(3, "The quick brown fox jumps over the lazy dog"))

#remove even numbers
num = [7,8,120,25,44,20,27]
numOdd = [x for x in num if x%2 != 0]
numEven = [x for x in num if x%2 == 0]
print(numOdd)
print(numEven)
