import random
from termcolor import colored, cprint

def wordle():
    word_list = []
    file_in = open('possible_wordle_words.txt', 'r')
    for line in file_in:
        word_list.append(line.upper().strip())
    file_in.close()
    word = word_list[random.randrange(12948)].strip().upper()
    attempts = 0
    while attempts < 7:
        guess = input('Guess a 5 letter word: ').upper()
        if len(guess) != 5:
            print('Invalid Guess')
        elif guess == word:
            print('Your Guess Was Correct!')
            break
        else:
            output = ''
            for pos in range(5):
                if guess[pos] == word[pos]:
                    output = output + colored(guess[pos], 'green') + ' '
                elif guess[pos] in word:
                    output = output + colored(guess[pos], 'yellow') + ' '
                else:
                    output = output + colored(guess[pos], 'red') + ' '
            print(output.strip())
            attempts += 1
    if attempts == 7:
        print('The correct word was ' + word)

wordle()