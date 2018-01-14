#Rock Paper Scissors game
#Rock beats scissors
#Scissors beats paper
#Paper beats rock

from random import randint

def Rock_Paper_Scissors():

    player=False

    while not player:

        a = ['Rock', 'Paper', 'Scissors']

        machine = a [randint(0, 2)]
        you = (input ("\n Rock,Paper,Scissors? \n ") ).capitalize()

        if machine == you:
            print("\n Its tie \n")

        elif machine == 'Rock':
            if you == 'Paper':
                print('\nYou win! {1} beats {0}\n'.format(machine,you))
            else:
                print('\nYou lose! {0} beats {1}\n'.format(machine, you))

        elif machine == 'Paper':
            if  you == 'Rock':
                print('\nYou lose! {0} beats {1}\n'.format(machine, you))
            else:
                print('\nYou win! {1} beats {0}\n'.format(machine, you))

        elif machine == 'Scissors':
            if you =='Paper':
                print('\nYou lose! {0} beats {1}\n'.format(machine, you))
            else:
                print('\nYou win! {1} beats {0}\n'.format(machine, you))

        player=False

Rock_Paper_Scissors()
