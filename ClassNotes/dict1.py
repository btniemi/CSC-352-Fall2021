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

dict = {'a': 1}
print(dict)

dict.update(a='hello')
print(dict)

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



#multiple values for each key
sport_teams = {
    'football': ['Raiders', 'Giants', 'Broncos', '49ers', 'Seahawks'],
    'baseball': ['Cardinals', 'Rockies', 'Dodgers', 'Aviators', 'Mariners', 'Athletics', 'Padres'],
    'hockey': ['Avalanche', 'Coyotes', 'Kings'],
    'basketball': ['Lakers', 'Suns', 'Trailblazers', 'Heat'],
}
print(sport_teams)

#add values key present
def add_values_to_key(temp_dict, key, list_of_values):
    if key not in temp_dict: #creates a bool for true or false https://www.askpython.com/python/examples/in-and-not-in-operators-in-python
        temp_dict[key] = list() #if true do this to create key value pairs for new stuff
    temp_dict[key].extend(list_of_values) #if false skip creation and do this
    return temp_dict
sport_teams = add_values_to_key(sport_teams, 'football', [1,2,3,4])
print("after add to existing: ", sport_teams)
sport_teams = add_values_to_key(sport_teams, 'temp', [1,2,3,4])
print("after add new key: ", sport_teams)

#seperate into different dictionaries
football = {}
baseball = {}
hockey = {}
basketball = {}

list_values_to_check = {'football', 'baseball', 'hockey', 'basketball'}
for keys in sport_teams:
    if keys in list_values_to_check:
        if keys == 'football':
            football[keys] = sport_teams[keys]
        elif keys == 'baseball':
            baseball[keys] = sport_teams[keys]
        elif keys == 'hockey':
            hockey[keys] = sport_teams[keys]
        elif keys == 'basketball':
            basketball[keys] = sport_teams[keys]
        else:
            break
print(football)
print(baseball)
print(hockey)
print(basketball)

concatenate_sports = {}
for d in (football, baseball, hockey, basketball) : concatenate_sports.update(d)
print(concatenate_sports)

#Search for value in the dictionary with multiple values for a key
word_freq = {'is': [1, 3, 4, 8, 10],
             'at': [3, 10, 15, 7, 9],
             'test': [5, 3, 7, 8, 1],
             'this': [2, 3, 5, 6, 11],
             'why': [10, 3, 9, 8, 12]}
# Check if a value exist in dictionary with multiple value
value = 10
# Get list of keys that contains the given value
list_of_keys = [key
                for key, list_of_values in word_freq.items()
                if value in list_of_values]
if list_of_keys:
    print(list_of_keys)
else:
    print('Value does not exist in the dictionary')