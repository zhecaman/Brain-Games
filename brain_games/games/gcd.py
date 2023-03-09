from math import gcd
from sympy import isprime
import random


RULES = 'Find the greatest common divisor of given numbers.'


def get_question_and_correct_answer():
    '''
    Returns a tuple of question and correct answer
    '''
    desk = [x for x in range(100) if not isprime(x)]
    numbers = random.choice(desk), random.choice(desk)
    question = f'{numbers[0]} {numbers[1]}'
    correct_answer = gcd(*numbers)
    return question, str(correct_answer)
