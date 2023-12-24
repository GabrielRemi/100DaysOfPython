import random
from english_words import get_english_words_set
lives: int = 6
word: str
guessed_letters: list[str] = []
display: list[str] = []
end_of_game: bool = False


def generate_word():
    global word
    global display

    words: list[str] = list(get_english_words_set(["web2"], lower=True))

    word = random.choice(words)
    display = ["_"] * len(word)


def display_word() -> str:
    "display the word to guess with blanks in the unknown places"
    word: str = ""
    for c in display:
        word += c

    return word

def print_used_letters() -> str:
    global guessed_letters

    text = ""
    for c in guessed_letters:
        text += c

    return text


def win():
    global end_of_game
    print("You won!")
    end_of_game = True


def loose():
    global end_of_game
    global word

    print(f"You lost! the word was {word}")
    end_of_game = True

def guess_letter() -> bool:
    """User inputs a letter and return boolean if it is in the word. it true then
    fill in the blanks of the guessed_word list"""
    global lives
    global guessed_letters

    letter = input("Guess a letter: ")
    try:
        if len(letter) != 1:
            raise Exception("Letter must be a single letter")
        if not letter.isalpha():
            raise Exception("input must be a letter")
        if letter in guessed_letters:
            raise Exception("already guessed")
    except:
        print("something went wrong, try again.")
        return guess_letter()

    letter = letter.lower()
    guessed_letters.append(letter)

    if letter in word:
        for i in range(len(word)):
            if letter == word[i]:
                display[i] = letter
        return True
    else:
        lives -= 1
        return False


def run():
    global word
    global lives
    global guessed_letters
    global display
    global end_of_game

    generate_word()

    while lives > 0 and not end_of_game:
        print(f"used letters: {print_used_letters()}")
        guess_letter()
        print(lives)
        print(display_word())
        if "_" not in display:
            win()

    if lives == 0:
        loose()


if __name__ == "__main__":
    run()
