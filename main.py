import random
from hangmanArt import stages, logo
from hangmanWordList import word_list

chosenWord = random.choice(word_list)
wordLength = len(chosenWord)


endOfGame = False
lives = 6

print(logo)
print("")

display = []
for _ in range(wordLength):
    display += "_"
print(display)

while not endOfGame:
    guess = input("Guess a Letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(wordLength):
        letter = chosenWord[position]

        if letter == guess:
            display[position] = letter
            print(f"Guessed Letter: {guess}")

    if guess not in chosenWord:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            endOfGame= True
            print("You lose.")
    print(' '.join(display))

    if "_" not in display:
        endOfGame  = True
        print("You win.")

    print(stages[lives])
