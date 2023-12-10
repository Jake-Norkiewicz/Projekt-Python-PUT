import matplotlib.pyplot as plt
import numpy as np

def Fib_number(n = 0):

    if n == 0:
        return 0    #STOP condition of our recursive function
    elif n == 1:
        return 1

    return Fib_number(n-1) + Fib_number(n-2)

def ex_1():

    numbers = []
    for i in range(0, 100):
        numbers.append(i + 1)

    print("Number list", '\n', numbers)

    for i in range(0, 100):
        if numbers[i]%3 == 0 and numbers[i]%5 == 0:
            numbers[i] = "FizzBuzz"
        elif numbers[i]%3 == 0:
            numbers[i] = "Fizz"
        elif numbers[i]%5 == 0:
            numbers[i] = "Buzz"

    #The order of if's matters here. if's executed in reverse would result in for example: the number 15 being replaced only by "Buzz". Elif instruction would
    #prevent checking the next possible condition if the first one were true

    print("After replacing:", '\n', numbers)


def ex_2():
    pass

def ex_3():
    pass

def ex_4():

    print("Input a positive integer n: ")
    n = int(input())

    result = Fib_number(n)
    print(result)

def ex_5():
    pass

def ex_6():
    pass

def ex_7():
    pass

def ex_8():
    pass

def ex_9():
    pass

def main():

    print("Ex.1:", '\n')
    ex_1()
    print('\n')

    print("Ex.2:", '\n')
    ex_2()
    print('\n')

    print("Ex.3:", '\n')
    ex_3()
    print('\n')

    print("Ex.4:", '\n')
    ex_4()
    print('\n')

    print("Ex.5:", '\n')
    ex_5()
    print('\n')

    print("Ex.6:", '\n')
    ex_6()
    print('\n')

    print("Ex.7:", '\n')
    ex_7()
    print('\n')

    print("Ex.8:", '\n')
    ex_8()
    print('\n')

    print("Ex.9:", '\n')
    ex_9()
    print('\n')

if __name__ == '__main__':
    main()