import random


RULES = 'Answer "yes" if given number is prime, otherwise answer "no".'

def isprime(number):
    for i in range(2, (number//2) + 1):
        if number % i == 0:
            return False
    return True



def get_question_and_correct_answer():
    '''
    Returns a tuple of question and correct answer
    '''
    question = random.randint(1, 20)
    correct_answer = 'yes' if isprime(question) else 'no'
    return question, correct_answer
