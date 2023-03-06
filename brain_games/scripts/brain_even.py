#!/usr/bin/env python3

import prompt
import random


def correct_answer(number):
    return 'yes' if number % 2 == 0 else 'no'


desk = list(range(1, 21))


def main():
    ATTEMPTS = 3
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while ATTEMPTS > 0:
        number = random.choice(desk)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')

        if answer != correct_answer(number):
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer(number)}'.\n"
                  f"Let's try again, {name}!")
            break
        print('Correct!')
        ATTEMPTS -= 1
        if ATTEMPTS == 0:
            print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
