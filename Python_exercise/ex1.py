"""Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that
they will turn 100 years old."""

def userinfo():
    current_year=int(input('Enter the current year:\n'))
    name=input('Enter your name:\n')
    age=int(input('Enter your age:\n'))
    if age>=0:
        result=(current_year-age)+100
        print('{0}! you  will be 100 years old in  {1} '.format(name.capitalize(),result))
    else:
        print('Check your input values String:Name,int:Age')
userinfo()
