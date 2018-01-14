#Ask the user for a number and determine whether the number is prime or not.

def get_number():
    num = int(input("Enter a number:\n"))
    return num

def prime_check():
    'check whether number is a prime or not'
    num = get_number()
    if (num % 2 != 0) and (num / num == 1):
        print(num,"is a prime number")
    else:
        print(num,"is not a prime number")

prime_check()

