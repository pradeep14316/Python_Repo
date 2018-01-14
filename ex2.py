'''Ask the user for a number.
Depending on whether the number is even or odd,
print out an appropriate message to the user. '''

def odd_even():
    number=int(input('Enter the number:\n'))
    if number % 4== 0:
        print("Given number is even and multiple of 4")
    elif number % 2 == 0:
        print("Given number is even")
    else:
        print("Given number is odd")
        
odd_even()