import random

def greeting():
    print('-------------------------')
    print('Please enter your number:')
    print('-------------------------')

def guess_game():
        greeting()
        program_choice = random.randint(1, 10)
        while user_choice != program_choice:
            user_choice = int(input('>'))
            if user_choice > program_choice:
                print('Less')
            if user_choice < program_choice:
                print('More')
        print('You Guess')
guess_game()
