# divisables
divisorList = []
num = int(input("Give me a number: "))

for elm in range(1, num + 1):
    if num % elm == 0:
        divisorList.append(elm)
print("Numbers divisible by " + str(num) + " are: " + str(divisorList))


# functions
def my_function():
    print("Hello from a function")


my_function()


def my_function2(fname):
    print(fname + " Refsnes")


my_function2("Emil")
my_function2("Tobias")
my_function2("Linus")


def country_Function(country="Norway"):
    print('I am from ' + country)


country_Function("Sweden")
country_Function("India")
country_Function()
country_Function("Brazil")


def food_function(food):
    for x in food:
        print(x)


fruits = ['apple', 'banana', 'cherry']

food_function(fruits)
