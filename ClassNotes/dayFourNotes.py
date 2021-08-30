import operator
d = {1:2, 3:4, 4:3, 2:1, 0:0}
print('Original dictionary : ', d)
sorted_d = sorted(d.items(), key=operator.itemgetter(1))
print('Dictionary in ascending order by value : ', sorted_d)
sorted_d = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))
print('Dictionary in descending order by value : ', sorted_d)

#add a key
d = {0:10, 1:20}
print(d)
d.update({2:30})
print(d)

#concatenate dictionaries
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}
dic4={}
for d in (dic1, dic2, dic3) : dic4.update(d)
print(dic4)

d = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
def is_key_present(x):
    if x in d:
        print('key is present in the dictionary')
    else:
        print('key is not present in the dictionary')
is_key_present(5)
is_key_present(9)

#loops
d = {'Red':1, 'Green': 2, 'Blue': 3}
for color_key, value in d.items():
    print(color_key, 'corresponds to ', d[color_key])

#remove a key
myDict = {'a':1, 'b':2, 'c':3, 'd':4}
print(myDict)
if 'a' in myDict:
    del myDict['a']
print(myDict)

#derive dictionary from objects
class dictObj(object):
    def __init__(self):
        self.x = 'red'
        self.y = 'Yellow'
        self.z = 'Green'
    def do_nothing(self):
        pass
test = dictObj()
print(test.__dict__)