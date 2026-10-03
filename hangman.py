import random

words = ["python", "apple", "tiger", "computer", "school"]

word = "python"

guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

print("===== HANGMAN GAME =====")
print("Guess the word one letter at a time.")

while wrong_guesses < max_wrong_guesses:

    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)

    if "_" not in display_word:
        print("\nCongratulations!")
        print("You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        print("Wrong guess!")
        wrong_guesses += 1

else:
    print("\nGame Over!")
    print("The correct word was:", word)