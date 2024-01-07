<<<<<<< HEAD
from functions import processWord, get_random_word,game_over

word = get_random_word()

ok = False
for guess_num in range(1, 7):
        guess = input(f"\nGuess {guess_num}: ")
        while True:
            if processWord(guess,word):
                break
            else:
                guess = input(f"\nGuess {guess_num}: ")
        if guess == word:
            print("GOOD JOB!\n")
            ok = True
            break
if not ok:
    game_over(word)