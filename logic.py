
import word_bank as w
import random

def game(user):
    print(f"Hello {user}! Welcome to Dict-ective🕵🏻🧐")
    print("Simple rule of the game! 50 points if you guess the charecter right and -10 for wrong guess. Enjoy😁✌🏻")
    score = 0
    word = random.choice(w.words)
    answers = list(word)
    for i in range(4):
        for j in range(i+1):
            print(answers[j])
        