def wordle_solver():
    guess_list = []
    file_in = open('possible_wordle_words.txt', 'r')
    for line in file_in:
        guess_list.append(line.upper().strip())
    file_in.close()
    for guesses in range(6):
        guess = input('What was your guess: ').upper()
        print('g - green, y - yellow, r - red')
        feedback = input('Feedback: ').lower()
        if feedback == 'ggggg':
            print('The word you guessed is correct!')
            break
        
        guess_list_tuple = tuple(guess_list)
        for word in guess_list_tuple:
            for pos in range(5):
                if feedback[pos] == 'r' and guess[pos] in word: ## Letter is not in answer but is in word
                    guess_list.remove(word)
                    break
                elif feedback[pos] == 'g' and guess[pos] != word[pos]: ## Letter in the right place in answer but not in the same place in word
                    guess_list.remove(word)
                    break
                elif feedback[pos] == 'y' and guess[pos] not in word: ## Letter is in answer but not in the right place and not in word
                    guess_list.remove(word)
                    break
                elif feedback[pos] == 'y' and guess[pos] == word[pos]: ## Letter is in answer but not in the right place and is in same place in word
                    guess_list.remove(word)
                    break
        print(guess_list)

wordle_solver()