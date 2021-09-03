word = "python"
guess = ""
guesses = 5

print("Hey! Guess my secret word:")

while guess != word:
    if guesses == 0:
        print("\nYou're out of guesses!")
        break
    elif guesses < 5:
        print("Wrong! Try again (" + str(guesses) + "):")

    guess = input("> ")

    guesses -= 1

if guess == word:
    print("\nWow, you guessed it!")

print("\nThanks for playing!")
