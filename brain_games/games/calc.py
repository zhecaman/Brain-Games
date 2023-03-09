import random
from operator import add, sub, mul


RULES = 'What is the result of the expression?'


def get_question_and_correct_answer():
    '''
    Returns a tuple of question and correct answer
    '''

    numbers = random.randint(1, 21), random.randint(1, 21)
    operator = random.choice(['+', '-', '*'])
    question = f'{numbers[0]} {operator} {numbers[1]}'
    match operator:
        case '+':
            correct_answer = add(*numbers)
        case '-':
            correct_answer = sub(*numbers)
        case '*':
            correct_answer = mul(*numbers)
    return question, str(correct_answer)
