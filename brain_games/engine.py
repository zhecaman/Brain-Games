import prompt


def play(game):
    ATTEMPTS = 3
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.RULES)

    while ATTEMPTS > 0:
        question, correct_answer = game.get_question_and_correct_answer()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer != correct_answer:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {name}!")
            break
        print('Correct!')
        ATTEMPTS -= 1
        if ATTEMPTS == 0:
            print(f'Congratulations, {name}!')
