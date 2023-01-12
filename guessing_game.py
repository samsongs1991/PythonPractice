import random
import time

def start_game():
    print_title()
    user = get_user_name()
    (low, high) = get_guessing_range()
    random_num = select_random_int(low, high)
    attempts = start_guessing_loop(random_num)
    print_ending(user, attempts)

def get_input():
    return int(input())

def print_title():
    print('THE GUESSING GAME!')

def get_user_name():
    print('Type your name')
    return input()

def get_guessing_range():
    print('What should the LOWEST guess be?')
    low = get_input()
    print('The HIGHEST?')
    high = get_input()
    return (low, high)

def select_random_int(low, high):
    print(f'Selecting a random number between {low} and {high} inclusive')
    for i in range(6):
        print('.', end=' ', flush=True)
        time.sleep(0.5)
    print('Number selected!')
    return random.randint(low, high)

def start_guessing_loop(target):
    guessing = True
    attempts = 0
    while guessing:
        attempts += 1
        result = get_guess(target)
        if result == 0:
            print('YOU GOT IT!')
            guessing = False
        elif result == -1:
            print('Your guess was too low. Try again.')
        elif result == 1:
            print('Your guess was too high. Try again.')
    return attempts

def get_guess(target):
    print(f'Enter a number: ', end='')
    guess = get_input()
    if guess is target:
        return 0
    elif guess < target:
        return -1
    elif guess > target:
        return 1

def print_ending(user, attempts):
    print(f'Congrats {user}!')
    print(f'It took {attempts} attempts to get the correct answer.')
    print('EXITING PROGRAM')

start_game()
