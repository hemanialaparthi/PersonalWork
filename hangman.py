"""A simple Hangman Game"""

import random


def choose_word():
    " A function which contains list of words and chooses one on random using the random function"
    words = [
        "apple", "banana", "orange", "grape", "kiwi", "melon", "strawberry", "pineapple",
        "hate", "laptop", "computer", "love", "giraffe", "elephant", "zebra",
        "sunflower", "butterfly", "watermelon", "keyboard", "lamp", "internet", "lion",
        "developer", "astronaut", "universe", "galaxy", "moon", "spaceship", "planet"
        ]
    return random.choice(words)


def display_word(word, guessed_letters):
    "Displays the word"
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display


def display_hangman(attempts):
    "Shows the number of attempts left using hangman"
    stages = [
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
          /|\\  |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        """
    ]
    return stages[attempts]


def hangman():
    "Checks to see if user can get the word in the number of attempts provided"
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("Guess the word!")

    while attempts > 0:
        print(display_hangman(attempts))
        print(display_word(word, guessed_letters))
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print("Incorrect guess! You have", attempts, "attempts left.")
            if attempts == 0:
                print(display_hangman(attempts))
                print("Sorry, you ran out of attempts. The word was:", word)
                break
        else:
            print("Correct guess!")

        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You guessed the word:", word)
            break

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        hangman()
    else:
        print("Thanks for playing!")


if __name__ == "__main__":
    hangman()