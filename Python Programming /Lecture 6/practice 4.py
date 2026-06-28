# WAP to find the factorial of n number using function

def fact(num):
    factorial=1
    for i in range(1, num + 1):
        factorial *= i
        print(factorial)

fact(10)