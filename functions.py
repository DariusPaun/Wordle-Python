import pathlib
import random
from string import ascii_letters


def getWords(leng):
    with open("words.txt", "r") as file:
        old_list = file.read().splitlines()
    new_list = [word.lower() for word in old_list if len(word) == leng]
    return new_list
def checkWord(word) -> bool:
    if len(word) != 5:
        print("YOUR WORD MUST HAVE 5 LETTERS")
        return False
    Letters=[let for let in word]
    ASCII_LETTERS = {chr(i): i for i in range(ord('A'), ord('Z')+1)}
    for let in Letters:
        if let not in ASCII_LETTERS:
            print(f"{let} IS NOT ALLOWED")
            return False
    return True
def get_random_word():
    wordlist = getWords(5)
    words = [
        word.upper()
        for word in wordlist
        if all(letter in ascii_letters for letter in word)
    ]
    return random.choice(words)

def processWord(word,randword) ->bool:
    word = word.upper()
    if checkWord(word):
        CorectLatters = []
        MisplacedLatters = []
        WrondLatters = []
        ListWord=list(word)
        ListRandword =list(randword)
        for i in range(5):
            if ListWord[i] == ListRandword[i] :
                CorectLatters.append(ListWord[i])
                ListRandword[i] = 0
            elif (ListWord[i] in ListRandword) and ListWord[i] not in MisplacedLatters:
                MisplacedLatters.append(ListWord[i])
            elif ListWord[i] not in ListRandword:
                WrondLatters.append(ListWord[i])
        print(f"Corect Letters: {CorectLatters}")
        print(f"Misplaced Letters: {MisplacedLatters}")
        print(f"Wrong Letters: {WrondLatters}")
        return True


    else:
        return False


def game_over(word):
    print(f"The word was {word}")

