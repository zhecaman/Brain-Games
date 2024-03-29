import prompt


ATTEMPTS = 3


def play(game):
    '''
    The game engine.
    parametr = game module
    '''

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.RULES)

    counter = 0

    while counter < ATTEMPTS:
        question, correct_answer = game.get_question_and_correct_answer()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer != correct_answer:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {name}!")
            return
        counter += 1
        print('Correct!')
    print(f'Congratulations, {name}!')
