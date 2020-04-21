#! python3
import random


def main():

    def update_hangman_string(original: str, underscored: str, char: str):
        first = original[0]
        last = original[-1]
        between = original[1:-1]
        underscored_between = underscored[1: -1]
        underscored_between = underscored_between.replace(" ", "")
        new_between = ""

        # iterate over all letters between the first and the last
        for idx in range(len(between)):
            # check if the letter is the same as the users's guess
            if between[idx] == char:
                # if it is, show it in the new underscored string
                new_between += f" {char} "
            else:
                # otherwise use the letter from the old underscored string
                new_between += f" {underscored_between[idx]} "
        return first + new_between + last

    words = ["pineapple", "soldier", "destruction", "asteroid", "mastery",
             "concatenate", "phoenix", "calculator", "president", "parachute"]
    word = str(random.choice(words))
    word_underscored = word[0] + len(word[1:-1]) * " _ " + word[-1]

    has_won = False
    current_try = 0
    number_of_tries = 5
    wrong_guesses = {}

    while current_try < number_of_tries:

        print(word_underscored)
        # get guess from user input
        guess = input("Enter a letter: ")

        if not guess.isalpha():
            print("You must enter a letter")
            continue

        if len(guess) > 1:
            print("You must enter only one letter!")
            continue

        guess = guess.lower()

        # check if the guess is correct
        if guess in word:
            word_underscored = update_hangman_string(word, word_underscored, guess)
            if word_underscored.replace(" ", "") == word:
                has_won = True
                break
        else:
            # keep track of all wrong guesses
            all_wrong_guess = list(wrong_guesses.keys()) + [guess]
            print(", ".join(all_wrong_guess))
            if guess in wrong_guesses:
                print("You have already guessed this and it was incorrect!")
                continue

            wrong_guesses[guess] = True
            current_try = current_try + 1
            print(f"You have {number_of_tries - current_try} tries left!")

    if has_won:
        print("You won! " + f"The word was: {word.upper()}.")
    else:
        print(f"The word was: {word}. You lost!")
    while True:
        restart = input("Do you want to play again? Type 'y' or 'n'.")
        if restart.lower() == "y":
            main()
        elif restart.lower() == "n":
            print("Bye, bye. :)")
            exit()
        else:
            continue


main()
