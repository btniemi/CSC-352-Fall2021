#write program that prints out all the elements of the list that are less than 34
#write one that prints out all elements above 41
#do it in one line of code ???
#ask user for the nuumber of elements

a = [1,1,2,3,4,5,8,13,21,25,27,31,34,35,37,41,44,55,89,91,95,101,122,155]

lessThanThirtyFour = []
greaterThanFortyOne = []
lessThanFifty = []
greaterThanFifty = []

for i in a:
    if i < 34:
        lessThanThirtyFour.append(i)
    elif i > 41:
        greaterThanFortyOne.append(i)

print("The numbers less than 34 are " + str(lessThanThirtyFour))
print("The numbers greater than 41 are " + str(greaterThanFortyOne))

print("The number of elements that are less then 34 is " + str(len(lessThanThirtyFour)))
print("The number of elements that are greater than 41 is " + str(len(greaterThanFortyOne)))
print("\n-----Extra Credit-----")

#extra credit
lst = []
numElements = int(input("Enter number of elements you want to add to list: "))

for i in range(0, numElements):
    element = int(input())
    lst.append(element)

lst.sort()

print("Your generated list is: " + str(lst))

for i in lst:
    if i < 50:
        lessThanFifty.append(i)
    elif i > 50:
        greaterThanFifty.append(i)

print("The numbers less than 50 are " + str(lessThanFifty))
print("The numbers greater than 50 are " + str(greaterThanFifty))

print("The number of elements that are less then 50 is " + str(len(lessThanFifty)))
print("The number of elements that are greater than 50 is " + str(len(greaterThanFifty)))
print("\n-----In One Line-----")

#one line of code
#not sure how to do this honestly


