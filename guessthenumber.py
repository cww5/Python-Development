import random


def ask_user_for_boundary_numbers(user_name):
    while True:
        low_num = ask_user_for_number_of('low number', user_name)
        high_num = ask_user_for_number_of('high number', user_name)
        if low_num >= high_num:
            print('Please ensure low number is less than high number.')
        else:
            break
    return low_num, high_num


def ask_user_for_number_of(prompt, user_name):
    while True:
        try:
            number = int(input('Please enter a number for: {} '.format(prompt)))
            break
        except TypeError:
            print('You entered an invalid number, please enter a positive integer.')
    return number


def ask_user_name():
    user_name = input('What is your name? ')
    return user_name


def generate_number(low=0, high=20):
    random_num = random.randint(low, high)
    return random_num


def play_game(player_name, num_guesses, ai_number):
    for i in range(num_guesses):
        user_guess = ask_user_for_number_of('your guess', player_name)
        dist = abs(abs(user_guess) - abs(ai_number))
        if 6 > dist > 0:
            print('You are getting closer...')
        if user_guess > ai_number:
            print('You are too high! Try again.')
        elif user_guess < ai_number:
            print('You are too low! Try again.')
        else:
            print('You got it correct!')
            break


def main():
    user_name = ask_user_name()
    user_guesses = ask_user_for_number_of('number of guesses', user_name)
    low_num, high_num = ask_user_for_boundary_numbers(user_name)
    ai_number = generate_number(low_num, high_num)
    play_game(user_name, user_guesses, ai_number)


if __name__ == '__main__':
    main()