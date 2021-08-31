name = input("Give me you name: ")
age = input("Enter your age: ")
age = int(age)  # this will throw a type error if trying to print because cant type case int to a string

print("Your name is " + name + "\n")

# concatination
print("Were" + "wolf")
print("Door" + "man")
print("4" + "chan")
print(str(4) + "chan")
print(4 * "test" + "\n")  # can use math to contatinate things as well kinda cool here

# conditionals
if age > 17:
    print("you can see a R rated movie")
elif age < 17 and age > 12:
    print("you can see a PG-13 rated movie")
else:
    print("you can see a G rated movie")

grade = int(input("Enter your grade:"))
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 65:
    print("D")
else:
    print("F")

a = 6
if a == 3:
    print("The variable 'a' has the value 3")
elif a != 3:
    print("The variable 'a' does not have the value 3")

# lists
import random

my_list = [10, 20, 30, 40, 50]
u_list = random.sample(my_list, 3)
print(u_list)