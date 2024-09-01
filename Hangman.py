import random

# List of words to choose from
word_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']

def hangman():
    # Select a random word from the list
    word = random.choice(word_list)
    word_length = len(word)

    # Initialize the guessed word with underscores
    guessed_word = ['_'] * word_length

    # Initialize the number of incorrect guesses
    incorrect_guesses = 0
    max_incorrect_guesses = 10

    print("Welcome to Hangman!")
    print("You have", max_incorrect_guesses, "chances to guess the word.")

    while '_' in guessed_word and incorrect_guesses < max_incorrect_guesses:
        # Display the current state of the guessed word
        print(' '.join(guessed_word))

        # Ask the player for their guess
        guess = input("Guess a letter: ").lower()

        # Check if the guess is in the word
        if guess in word:
            # Reveal the correct letter in the guessed word
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            # Increment the number of incorrect guesses
            incorrect_guesses += 1
            print("Incorrect guess. You have", max_incorrect_guesses - incorrect_guesses, "chances left.")

    # Check if the player won or lost
    if '_' not in guessed_word:
        print(' '.join(guessed_word))
        print("Congratulations, you won!")
    else:
        print("Sorry, you lost. The word was:", word)

if __name__ == "__main__":
    hangman()