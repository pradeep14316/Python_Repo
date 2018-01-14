#Guess the number
from random import randint
def guess():
    num=False
    while not num:
        num = input("Guess the number or 'q' to quit?\n")
        machine = randint(1,9)
        try:
            if num=='q':
                break

            elif machine == int(num):
                print("Your'e exactly correct!")

            elif abs(machine - int(num)) >= 4:
                print('Too High !')

            elif abs(machine - int(num)) <4 and abs(machine - int(num)) >=1:
                print('too Low!')

            num=False
        except ValueError as e:
            print('Check your input:\n',e)


guess()