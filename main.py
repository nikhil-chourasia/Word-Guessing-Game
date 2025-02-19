from art import *
import logic

def showResult(score):
    print("Congratulations! You are at the end of the game! 🎉")
    print("Here is your score!")
    str(score)
    Art = text2art(score, font = 'block', chr_ignore=True)
    print(Art)
    print("Thanks for playing😊")

def quit(user):
    print("Oh! you want to quit? 😢: ")
    response = input("You sure???🧐 (yes/no): ")
    if(response.lower() == "yes"):
        print(f"Ok.. fine😕 Have a great day! {user}😊")
        exit()
    elif (response.lower() == "no"):
        print("See! Now that's a Good Idea😁!")
        return
    else:
        print("Huh? What do you mean? I don't get it? Try again please😅")
        quit(user)

print("Hello user welcome to Dict-ective🕵🏻🧐")
user = input("What is your name?: ")
while True:
    response = input("Write anything and press enter to start the game or write \"quit\" to quit the game.")
    if (response.lower() == "quit"):
        quit(user)
    else:
        score = logic.game(user)
        showResult(score)