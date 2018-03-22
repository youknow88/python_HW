import random

def greeting():
    print('-------------------------')
    print('Please enter your number:')
    print('-------------------------')

def guess_game():
        greeting()
        user_choice = int(input('>'))
        program_choice = random.randint(1, 10)
        while user_choice != program_choice:
            print(user_choice)
            if user_choice > program_choice:
                print('More')
            if user_choice < program_choice:
                print('Less')
guess_game()






















