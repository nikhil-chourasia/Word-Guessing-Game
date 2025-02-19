from art import *
import logic
from rich.progress import Progress
import time

def showResult(score):
    print("Congratulations! You are at the end of the game! 🎉")
    with Progress() as progress:
        task = progress.add_task("[orange]Loading Scores...", total = 100)
        while not progress.finished:
            progress.update(task, advance = 7)
            time.sleep(0.2)
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
        with Progress() as progress:
            task = progress.add_task("[cyan]Quiting...", total = 100)
            while not progress.finished:
                progress.update(task, advance = 7)
                time.sleep(0.2)
        exit()
    elif (response.lower() == "no"):
        with Progress() as progress:
            task = progress.add_task("[cyan]Returning...", total = 100)
            while not progress.finished:
                progress.update(task, advance = 7)
                time.sleep(0.2)
        print("See! Now that's a Good Idea😁!")
        return
    else:
        print("Huh? What do you mean? I don't get it? Try again please😅")
        quit(user)

print("Hello user welcome to Dict-ective🕵🏻🧐")
user = input("What is your name?: ")
with Progress() as progress:
    task = progress.add_task("[red]Loading...", total = 100)
    while not progress.finished:
        progress.update(task, advance = 7)
        time.sleep(0.2)
while True:
    response = input("Write anything and press enter to start the game or write \"quit\" to quit the game.")
    with Progress() as progress:
        task = progress.add_task("[yellow]Starting...", total = 100)
        while not progress.finished:
            progress.update(task, advance = 7)
        time.sleep(0.2)
    if (response.lower() == "quit"):
        quit(user)
    else:
        score = logic.game(user)
        showResult(score)