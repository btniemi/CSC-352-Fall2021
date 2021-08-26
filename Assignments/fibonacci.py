#write a program that ask the user for how many fibo numbers to generate and then generate them.
#if types 7 get the first 7 numbres of fibo

x = int(input("Enter how many fibonacci numbers you want to see in the amazing mathematical sequence: "))

ans = []

def fibo(num):
    a = 1
    b = 0
    if num < 0:
        print("Incorrect input~~~cant find sequence~~~(robotic voice line)")

    if num == 0:
        print("There is no 0 element in the fibonacci sequence(well there is but its just zero)")

    elif num == 1:
        ans.append(a)

    else:
        for i in range(0, num):
            c = a + b
            a = b
            b = c
            ans.append(c)
    return print(ans)

fibo(x)