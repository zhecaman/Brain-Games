import random


RULES = 'What number is missing in the progression?'


def get_question_and_correct_answer():
    '''
    Returns a tuple of question and correct answer
    '''
    start = random.randint(1, 20)
    step = random.randint(1, 10)
    hidden = random.randint(1, 9)
    progression = [str(x) for x in range(start, (step * 10 + start), step)]
    correct_answer = progression[hidden]
    progression[hidden] = '..'
    question = ' '.join(progression)
    return question, str(correct_answer)
