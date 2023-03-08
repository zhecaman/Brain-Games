import random

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_correct_answer():
    '''
    Returns a tuple of question and correct answer
    '''
    question = random.randint(1, 21)
    correct_answer = 'yes' if question % 2 == 0 else 'no'
    return question, correct_answer
