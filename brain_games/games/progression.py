import random


RULES = 'What number is missing in the progression?'


def get_question_and_correct_answer():
    '''
    Returns a tuple of question and correct answer
    '''
    start = random.randint(1, 20)
    step = random.randint(1, 10)
    hidden = random.randint(1, 9)
    progression = [x for x in range(start, (step * 10 + start), step)]
    numbers = progression.copy()
    numbers[hidden] = '..'
    question = '{0} {1} {2} {3} {4} {5} {6} {7} {8} {9}'.format(*numbers)
    correct_answer = progression[hidden]
    return question, str(correct_answer)
