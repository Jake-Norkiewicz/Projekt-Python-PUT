import matplotlib.pyplot as plt
import numpy as np
import random
import math


def Fib_number(n = 0):

    if n == 0:
        return 0    #STOP condition of our recursive function
    elif n == 1:
        return 1

    return Fib_number(n-1) + Fib_number(n-2)


def mean_value(numbers):

    sum = 0
    num_of_elements = len(numbers)

    for i in range(0, num_of_elements):
        sum += numbers[i]

    mean = sum / num_of_elements

    return float(mean)

def standard_deviation(numbers):

    mean = mean_value(numbers)
    sum_of_squares_of_differences = 0

    for i in range(0, len(numbers)):
        diff = numbers[i] - mean
        sum_of_squares_of_differences += math.pow(diff, 2)

    stan_dev = math.sqrt(sum_of_squares_of_differences/len(numbers))

    return float(stan_dev)


def max_value(numbers):

    max_element = numbers[0]    #we're assuming that the first element is the greatest one. We have to do this assumption because we are going to compare this value with the rest and overwrite it if needed

    for i in range(0, len(numbers)):
        if max_element < numbers[i]:    #if there's a greater element in the list - overwrite the maximum element value
            max_element = numbers[i]

    return max_element


def min_value(numbers):

    min_element = numbers[0]    #same assumption as in the max_value() function

    for i in range(0, len(numbers)):
        if min_element > numbers[i]:
            min_element = numbers[i]

    return min_element


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

    print("Enter how many random numbers to save in the file:")
    n = int(input())
    numbers = []

    for i in range(n):
        random_number = random.randint(0, 99)
        numbers.append(random_number)

    path = "ex_2_file.txt"
    with open(path, 'w') as file:
        for i in range(0, n):
            file.write(str(numbers[i]))
            file.write('\n')

    print("Generated random number list:", numbers, "has been saved in the file", path, "successfully")

def ex_3():

    numbers = []

    path = "ex_2_file.txt"
    with open(path, 'r') as file:
        all_lines = file.readlines()

        for line in all_lines:
            x = int(line.strip())
            numbers.append(x)

    print("Numbers from the file", path, ":", numbers)

    print("Mean:", format(mean_value(numbers), ".2f") )
    print("Standard deviation:", format(standard_deviation(numbers), ".2f") )   #displaying up to 2 decimal places
    print("Maximum value:", max_value(numbers))
    print("Minimum value:", min_value(numbers))

def ex_4():

    print("Input a positive integer n:")
    n = int(input())

    result = Fib_number(n)
    print("n-th term of Fibonacci sequence is: ", result)

def ex_5():

    print("Enter how many Fibonacci numbers to generate:")
    n = int(input())

    fib_numbers = []

    for i in range(0, n):
        fib_numbers.append(Fib_number(i))

    print("Numbers generated:", fib_numbers)


def ex_6():

    print("Enter how many values to generate in the dictionary:")
    n = int(input())

    dict = {}
    keys = []
    values = []

    for i in range(0, n):
        keys.append(i + 1)

    for i in range(0, n):
        values.append(keys[i] * keys[i])

    for i in range(0, n):
        dict[keys[i]] = values[i]

    print("Generated dictionary:", dict)

    return dict


def ex_7(dict):

    sum = 0
    values = list(dict.values())    #dict_values() returns weird string representation so I convert it into a list type variable

    for i in values:
        sum += i

    print("Values from the dictionary from the previous task:", values)
    print("Sum of values:", sum)


def ex_8():

    










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
    dict_from_ex_6 = ex_6()
    print('\n')

    print("Ex.7:", '\n')
    ex_7(dict_from_ex_6)
    print('\n')

    print("Ex.8:", '\n')
    ex_8()
    print('\n')

    print("Ex.9:", '\n')
    ex_9()
    print('\n')

if __name__ == '__main__':
    main()