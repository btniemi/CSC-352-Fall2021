# dict = {'a': 1}
# print(dict)
#
# dict.update(a='hello')
# print(dict)
#
# person_dict = {
#     'fName': "Braedon",
#     'lName': "Niemi",
#     'age': 27,
#     'grade': ['A', 'B', 'C', 'A']
# }

# was trying to test changes in grade list but realiezed that easier to create class and each grade for a class should be seperate that you can change not one list

# languages = ['Java', 'Python', 'JavaScript']
# versions = [14, 3, 6]
#
# result = zip(languages, versions)
# print(list(result))

# import csv
# import collections
#
# with open('test.csv', mode='r') as csvfile:
#     reader = csv.reader(csvfile, delimiter=',')
#
#     dict1 = collections.defaultdict(dict)
#     for row in reader:
#         dict1[row[0]][row[1]] = row[2:7]
#         dict1[row[0]][row[7]] = row[8:11]
#         dict1[row[0]][row[11]] = row[12:]
#
# print(dict1)

#weighted average
assAvg = 0.68
tstAvg = 0.66
labAvg = 0.45
assW = 0.10
tstW = 0.70
labW = 0.20

weightAvg = (assAvg*assW + tstAvg*tstW + labAvg*labW) / (assW+tstW+labW)

print(weightAvg)