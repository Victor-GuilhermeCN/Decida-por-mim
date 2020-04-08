from random import randint
answers = ['Yeah, go on', 'No, do not go', 'Maybe', 'Yes', 'No', 'Absolutely', 'Of course', 'Sure', 'Thinking about it',
           'That is your choice', 'Do what you want', 'You do not need ask to me, you know the answer.']

def line():
    print('-' * 50)

def title(msg):
    line()
    print(msg.center(50))
    line()

def possibleAnswer():
    # Receiving the value, capitalizing it, selecting the first letter, and removing the spaces
    question = input('Ask your question: ').upper().strip()[0]
    # Testing whether the values entered are letters and questions or numbers.
    try:
        while question not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            print('Not number, just questions.')
            line()
            return possibleAnswer()
    except:
        print('Not number, just questions.')
        line()
        return possibleAnswer()
    else:
        # Using the library Random, to draw a possible answer saved in the list.
        if question in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            result = answers[randint(0, 11)]
            print(result)
            line()
            return wannaContinue()

def wannaContinue():
    resp = str(input('Do you want to do more questions? [Y/N]: ')).upper().strip()[0]
    while resp not in 'YN':
        print('Wrong option, try again.')
        return wannaContinue()
    if resp == 'Y':
        return possibleAnswer()
    if resp == 'N':
        while True:
            print('Ok, see you soon!')
            break
