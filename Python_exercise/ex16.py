# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them

#Ask user to input the number of Fibonacci series to be generate?

def get_integer():
    num = int(input("Enter how many Fibonnaci numbers to generate:\n"))
    return num

#Generate Febonacci series as per user required

def fibonacci():
    x = 0
    y = 1
    list=[]
    num = get_integer()
    for seq in range(1, num-1):
        y, x = y + x, y
        list.append(y)

    addition = 1 + sum([num1 for num1 in list])                     # add all the numbers generated in fibonacci series
    print('Addition of sequence of fibonacci Numbers:', addition)

fibonacci()