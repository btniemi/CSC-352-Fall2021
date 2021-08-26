def recur_fibo(num):
    if num <=1:
        return num
    else:
        return(recur_fibo(num-1) + recur_fibo(num-2))

nterms = int(input("How many terms of the fibonacci sequence do you wanna see? : "))

if nterms <=0:
    print("not valid input")
else:
    print("Fibonacci sequence is: ")
    for i in range(nterms):
        print(recur_fibo(i))