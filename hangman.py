import time

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    print("Welcome to Hangman! 🎉")
    time.sleep(1)
    start = input("Wanna play hangman with a friend? (y/n): ")

    if start.lower() == "n":
        print("😔 See you later!")
        quit()
    else:
        print("Come onn, lets play!")

    word_to_guess = input("Player 1, type in your secret word: ").lower()
    guessed_letters = []
    incorrect_attempts = 0
    max_attempts = 6

    while True:
        current_display = display_word(word_to_guess, guessed_letters)
        print("Current word:", current_display)
        guess = input("Player 2, guess a letter: ").lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("Oops, you already guessed that one. Try again!")
            elif guess in word_to_guess and guess not in guessed_letters:
                print("Nice one! You got it!")
                guessed_letters.append(guess)
            else:
                print("Nope, wrong guess. 😬")
                incorrect_attempts += 1
                print_hangman(incorrect_attempts)

            if set(guessed_letters) == set(word_to_guess):
                print("Yes! Player 2 had won. The word was:", word_to_guess)
                break

            if incorrect_attempts == max_attempts:
                print("Uh-oh, you're out of tries! Better luck next time. The word was:", word_to_guess)
                break
        else:
            print("Uh-oh! That's not a valid letter. Try again with just one letter.")

def print_hangman(incorrect_attempts):
    hangman_art = [
        """
         -----
         |   |
             |
             |
             |
             |
        """,
        """
         -----
         |   |
         O   |
             |
             |
             |
        """,
        """
         -----
         |   |
         O   |
         |   |
             |
             |
        """,
        """
         -----
         |   |
         O   |
        /|   |
             |
             |
        """,
        """
         -----
         |   |
         O   |
        /|\  |
             |
             |
        """,
        """
         -----
         |   |
         O   |
        /|\  |
        / \  |
             |
        """,
        """
         -----
         |   |
         O   |
        /|\  |
        / \  |
             |
        """
    ]
    print(hangman_art[incorrect_attempts])

if __name__ == "__main__":
    hangman()
