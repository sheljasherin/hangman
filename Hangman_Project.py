import random

def choose_word():
    words = ["python", "programming", "hangman", "computer", "science", "coding", "compiler", "interpreter", "developer"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    max_attempts = 6  # Adjust as needed
    attempts = 0

    print("Welcome to Hangman!")
    
    while attempts < max_attempts:
        guess = input("\nGuess a letter: ").lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
                continue

            guessed_letters.append(guess)

            if guess not in word_to_guess:
                attempts += 1
                print(f"Incorrect! Attempts left: {max_attempts - attempts}")
                print_hangman(attempts)

            display = display_word(word_to_guess, guessed_letters)
            print(display)

            if "_" not in display:
                print("\nCongratulations! You guessed the word.")
                break
        else:
            print("Invalid input. Please enter a single letter.")

    if "_" in display:
        print(f"\nSorry, you ran out of attempts. The word was: {word_to_guess}")

def print_hangman(attempts):
    hangman_parts = [
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

    print(hangman_parts[attempts])

if __name__ == "__main__":
    hangman()
