import operator

# the original list had dulicated and the key value pairs cant be the same key need unique ones so changed to this for the list
West_team = {
    'Las Vegas': 'Raiders',
    'San Francisco': 'Giants',
    'Denver': 'Broncos',
    'Arizona': 'Cardinals',
    'Colorado': 'Rockies',
    'Los Angeles': 'Dodgers',
    'SanFrancisco': '49ers',
    'Colorado.': 'Avalanche',
    'LasVegas': 'Aviators',
    'Seattle': 'Seahawks',
    'Seattle.': 'Mariners',
    'LosAngeles': 'Lakers',
    'Phoenix': 'Suns',
    'Phoenix.': 'Coyotes',
    'Oakland': 'Athletics',
    'San Diego': 'Padres',
    'Los angeles': 'Kings',
    'Portland': 'Trailblazers',
    'Miami': 'Heat'
}

# 1 sorted
print('#1')
sorted_West_teams = sorted(West_team.items(), key=operator.itemgetter(0))
print('Sorted West Teams: ', sorted_West_teams)

# 2 add a team
print('\n#2')
West_team.update({'los angeles': 'Rams'})
print(West_team)

# 3 split (look up how to do this)
print('\n#3')
sport_teams = {
    'football': ['Raiders', 'Giants', 'Broncos', '49ers', 'Seahawks'],
    'baseball': ['Cardinals', 'Rockies', 'Dodgers', 'Aviators', 'Mariners', 'Athletics', 'Padres'],
    'hockey': ['Avalanche', 'Coyotes', 'Kings'],
    'basketball': ['Lakers', 'Suns', 'Trailblazers', 'Heat'],
}
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

# 4 concatenate them back together
print('\n#4')
concatenate_sports = {}
for d in (football, baseball, hockey, basketball) : concatenate_sports.update(d)
print(concatenate_sports)

# 5 check to see if specific teams ARE present
print('\n#5')
def is_key_present(x):
    if x in West_team:
        print(x, 'is present in the dictionary')
    else:
        print(x, 'is not present in the dictionary')
is_key_present('Las Vegas')
is_key_present('Yakima')

# 6 pull out teams by specific location????????????????????????????
print('\n#6')
for location_key, value in West_team.items():
    print(location_key, 'corresponds to ', West_team[location_key])
    # not sure how you wanted this one done actually...

# 7 remove the team that does not belong
print('\n#7')
if 'Miami' in West_team:
    del West_team['Miami']
print(West_team)
