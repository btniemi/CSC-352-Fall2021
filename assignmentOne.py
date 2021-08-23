#write program that prints out all the elements of the list that are less than 34
#write one that prints out all elements above 41
#do it in one line of code
#ask user for the nuumber of elements (length of list)

a = [1,1,2,3,4,5,8,13,21,25,27,31,34,35,37,41,44,55,89,91,95,101,122,155]

lessThanThirtyFour = []
greaterThanFortyOne = []

for i in a:
    if i < 34:
        lessThanThirtyFour.append(i)
    elif i > 41:
        greaterThanFortyOne.append(i)

print(lessThanThirtyFour)
print(greaterThanFortyOne)

#need to pring the lenght of the lists???