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

languages = ['Java', 'Python', 'JavaScript']
versions = [14, 3, 6]

result = zip(languages, versions)
print(list(result))