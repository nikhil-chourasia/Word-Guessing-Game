
import word_bank as w
import random

def game(user):
    print(f"Hello {user}! Welcome to Dict-ective🕵🏻🧐")
    print("Simple rule of the game! 50 points if you guess the charecter right and -10 for wrong guess. Enjoy😁✌🏻")
    score = 0
    word = random.choice(w.words)
    answers = list(word)
    answersRevealed = ["-"] * len(answers)
    answersRevealed[0] = answers[0]
    index = 1
    attempt = 0
    incorrectAttempt = 0
    while index < len(answers):
        print("Word:", " ".join(answersRevealed))
        response = input("Guess the next letter: ").strip().lower()
        if response == answers[index]:
            print("Great Job!🎉 That's correct.. moving on to next one...")
            score += 50
            answersRevealed[index] = answers[index]
            index += 1
            attempt += 1
        else:
            print("Uh Oh!❌ Wrong guess.. Try again!")
            score -= 10
            attempt += 1
            incorrectAttempt += 1
    print("Congractulations! You guessed the word🎉")
    print(f"It took you {attempt} attempts out of which {incorrectAttempt} were incorrect.")
    return score