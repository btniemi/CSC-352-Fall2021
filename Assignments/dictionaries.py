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
print(West_team)

# 1 sorted
sorted_West_teams = sorted(West_team.items(), key=operator.itemgetter(0))
print('Sorted West Teams: ', sorted_West_teams)

# 2 add a team
West_team.update({'los angeles': 'Rams'})
print(West_team)


# 3 split (look up how to do this)
#can do something like is key present but need the dictionary to be based on sports not locations

# 4 concatenate them back together


# 5 check to see if specific teams ARE present
def is_key_present(x):
    if x in West_team:
        print(x, 'is present in the dictionary')
    else:
        print(x, 'is not present in the dictionary')
is_key_present('Las Vegas')
is_key_present('Yakima')

# 6 pull out teams by specific location????????????????????????????
for location_key, value in West_team.items():
    print(location_key, 'corresponds to ', West_team[location_key])
    # not sure how you wanted this one done actually...

# 7 remove the team that does not belong
if 'Miami' in West_team:
    del West_team['Miami']
print(West_team)
