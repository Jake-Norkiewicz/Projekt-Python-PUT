import matplotlib.pyplot as plt
import numpy as np
import random
import math
import time
import csv
from datetime import datetime


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


def generate_random_content():

    numbers = []

    for i in range(0, 10):
        base = random.randint(1, 10)
        exponent = random.uniform(1, 2)
        exponent = round(exponent, 2)
        number = pow(base, exponent)

        number = int(number)
        numbers.append(number)

    return numbers


def print_graph_ex_9(timestamp, pos_x, pos_y, pos_z):

    fig, (ax1, ax2, ax3) = plt.subplots(3, sharex = True)

    fig.suptitle("Position vs Time Graph", size = 15, fontweight = "bold")
    ax1.plot(timestamp, pos_x, color = "red")
    ax2.plot(timestamp, pos_y, color = "blue")
    ax3.plot(timestamp, pos_z, color = "green")

    plt.xlabel("Timestamps in seconds", fontsize = 12, fontweight = "bold")
    plt.xlim(None, 8)  # None guarantees that the X axis beginning remains shifted a little to the right

    ax1.set_title("x-position")
    ax2.set_title("y-position")
    ax3.set_title("z-position")

    ax1.set_ylabel("x-pos", fontsize = 12, fontweight = "bold")
    ax2.set_ylabel("y-pos", fontsize = 12, fontweight = "bold")
    ax3.set_ylabel("z-pos", fontsize = 12, fontweight = "bold")

    ax1.set_ylim(-25, 35)
    ax2.set_ylim(19.95, 20.05)
    ax3.set_ylim(1.8, 2.0)

    fig.tight_layout()
    plt.show()


def print_graph_ex_5(fib_numbers, n):

    x_values = []
    y_values = fib_numbers

    for i in range(0, n):
        x_values.append(i+1)

    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.title("Fibonacci numbers", fontsize = 12, fontweight = "bold")

    for i in range(0, len(y_values)):
        plt.text(i+1, y_values[i], y_values[i], ha = "center", va = "bottom")   #exact values of Fibonacci numbers will appear above the bars

    plt.bar(x_values, y_values, width = 0.5, tick_label = x_values, color = ["blue", "cyan"], edgecolor = "black")
    plt.show()


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
    print("Mean:", round(mean_value(numbers), 2) )
    print("Standard deviation:", round(standard_deviation(numbers), 2) )   #rounding to 2 decimal places
    print("Maximum value:", max_value(numbers))
    print("Minimum value:", min_value(numbers))

def ex_4():

    print("Input a positive integer n:")
    n = int(input())

    result = Fib_number(n)
    print("Term number", n, "of Fibonacci sequence is: ", result)

def ex_5():

    print("Enter how many Fibonacci numbers to generate:")
    n = int(input())

    fib_numbers = []

    for i in range(0, n):
        fib_numbers.append(Fib_number(i))

    print("Numbers generated:", fib_numbers)
    print_graph_ex_5(fib_numbers,n)


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

    file_paths = []

    for i in range(0, 10):
        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y_%m_%d_%H_%M_%S_%f")
        path = formatted_time + ".bin"
        file_paths.append(path)
        time.sleep(0.1)

        #file names are generated so quickly that all values would have the same name without the command time.sleep()
        #We have to delay the loop a little. The value of 0.1 second is chosen totally arbitrarily

    for i in range(0, 10):
        current_file_path = file_paths[i]

        with open(current_file_path, "wb") as file:
            content = generate_random_content()         #Function that generates random content of one line to be saved in the file
            content_byte = bytearray(content)
            file.write(content_byte)

    print("Position vs Time graph has been displayed")


def ex_9():

    timestamp = []      #column number 1 in .csv file
    pos_x = []          #num. 2
    pos_y = []          #num. 3
    pos_z = []          #num 4.
    
    vel_x = []
    vel_y = []
    vel_z = []

    file_path = "ex_9_file.csv"

    with open(file_path, "r") as file:
        CSV_READER = csv.reader(file)

        next(CSV_READER, None)

        for row in CSV_READER:
            timestamp.append(float(row[0]))     #float() converts string type data from .csv file to a float type variable so we can perform calculations on it

            pos_x.append(float(row[1]))
            pos_y.append(float(row[2]))
            pos_z.append(float(row[3]))
            
            vel_x.append(float(row[4]))
            vel_y.append(float(row[5]))
            vel_z.append(float(row[6]))

    print("Average x-position:", np.mean(pos_x))
    print("Average y-position:", np.mean(pos_y))
    print("Average z-position:", np.mean(pos_z))

    velocity_file_path = "velocity.csv"

    with open(velocity_file_path, "w", newline = '') as file:
        CSV_WRITER = csv.writer(file)
        rows_number = len(timestamp)

        for i in range(0, rows_number):
            velocity = np.sqrt(pow(vel_x[i], 2) + pow(vel_y[i], 2) + pow(vel_z[i], 2))  #Pythagorean Theorem in 3D
            CSV_WRITER.writerow([velocity])    #writerow() needs a list as a parameter

    print_graph_ex_9(timestamp, pos_x, pos_y, pos_z)


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