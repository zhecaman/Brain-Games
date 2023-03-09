import random
from sympy import isprime

RULES = 'Answer "yes" if given number is prime, otherwise answer "no".'


def get_question_and_correct_answer():
    '''
    Returns a tuple of question and correct answer
    '''
    question = random.randint(1, 20)
    correct_answer = 'yes' if isprime(question) else 'no'
    return question, correct_answer
