from words import wordList
from random import randint


guesses = 0


def main():
    win = False
    word = chooseRandomWord()
    coveredWord = "_" * len(word)
    print(f"The word contains {len(word)} letters")
    while guesses <= 11:
        if win:
            print("\n You win")
            print(f"The word was {coveredWord}")
            break
        else:
            print(f"\n{coveredWord}")
            print(f"You have {guesses} guesses out of 11 left")
            letterGuess = input("Please input a letter: ")
            # this ensures the player does not use a guess if they enter more
            # than 1 character
            if len(letterGuess) == 1:
                coveredWord = guessCheck(letterGuess, word, coveredWord)
                if word == coveredWord:
                    win = True

        if guesses == 11:
            print("\n You lose")
            print(f"The word was {word}")
            break


def chooseRandomWord():
    # take away 1 from the len of the list or else we'll get an index out of
    # range error
    wordListLen = len(wordList) - 1
    randomIndex = randint(0, wordListLen)
    return wordList[randomIndex]


def guessCheck(letterGuess, word, coveredWord):
    global guesses

    newCover = ""
    # first check if the letter guess is in the current word
    if letterGuess in word:
        for i in range(len(word)):
            if letterGuess == word[i]:
                newCover += word[i]
            else:
                newCover += coveredWord[i]
        return newCover
    else:
        guesses += 1
        return coveredWord


if __name__ == "__main__":
    main()
