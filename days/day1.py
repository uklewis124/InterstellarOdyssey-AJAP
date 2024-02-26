import os
import colorama
from colorama import Fore, Back, Style
import time
import sys
import time
import sys
# from .. import main

colorama.init(autoreset=True)
# main.test()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def wait(length=2.7):
    time.sleep(length)

def prin(arg):
    print(arg)
    wait()

def speak(char, text, delay=0.05):
    characters = {
        "You": {"Color": Fore.CYAN, "Type": False},
        "??": {"Color": Fore.RED, "Type": False},
        "A group of people": {"Color": Fore.RED, "Type": False},
        
        "Ana": {"Color": Fore.BLUE, "Type": False},
        "1": {"Color": Fore.GREEN, "Type": False},
        "2": {"Color": Fore.YELLOW, "Type": False},
        
        "Stg": {"Color": Fore.RED, "Type": True},
        "Think": {"Color": Fore.GREEN, "Type": True},
        "White": {"Color": Fore.WHITE, "Type": True}
    }
    
    complete = False
    
    if not characters[char]["Type"]:
        if char in characters:
            print(f"{characters[char]['Color']}{char} | ", end="")
            for letter in text:
                sys.stdout.write(letter)
                sys.stdout.flush()
                time.sleep(delay)
            print()
            complete = True
            
    if characters[char]["Color"] == Fore.WHITE and not complete:
        for letter in text:
            sys.stdout.write(f"{characters[char]['Color']}{letter}")
            sys.stdout.flush()
            time.sleep(delay)
        print()
        complete = True
    else:
        if not complete:
            print(f"{characters[char]['Color']}")
            for letter in text:
                sys.stdout.write(f"{characters[char]['Color']}{letter}")
                sys.stdout.flush()
                time.sleep(delay)
            print()

def proceed():
    input(f"{Fore.RED}Press Enter to continue...")
    clear()

class Player:
    def __init__(self):
        self.name = ""

player = Player()
## START OF DAY 1 ##

print("")
speak("Stg", "Day ?? - Where am I?")
print(f"{Fore.RED}=====================")
print("")

time.sleep(2)

speak("Think", "Huh?   Where am I?")
wait()
speak("Think", "I don't remember a th-")
time.sleep(5)
clear()
print(f"{Fore.RED}You awake to a loud thud.  A figure stands over you, a mug in hand.")
print()
time.sleep(3)
speak("??", "You're finally awake.. I was beginning to think you'd never wake up.")
wait()
speak("You", "Where am I?")
wait()
speak("??", "You're not sure? Well, I suppose that's to be expected.")
wait()
speak("??", "I saw you in the wilderness of Charterland. You were unconscious, so I brought you here.")
wait()
speak("You", "Charterland? I've never heard of it.")
wait()
speak("??", "That's because it's a secret.  You're not from around here, are you?")
wait()
speak("You", "I don't think so.")
wait()
speak("You", "I don't remember anything.")
wait()
speak("??", "I see.  Well, I'm sure you'll remember soon enough.")
wait()
speak("??", "I've made you some breakfast. You must be hungry.")
wait()
speak("Stg", "The figure hands you a plate of eggs and bacon.")
wait()
speak("??", "I'm sure you have a lot of questions.  I'll answer what I can.")
wait()
speak("??", "But first, eat up.  You'll need your strength.")
wait(5)
proceed()

# Eating Breakfast
speak("Stg", "You eat the eggs and bacon.  They're delicious.")
wait()
speak("Think", "I don't remember the last time I had a meal this good!")
wait()
speak("Think", "I should probably get changed.")
wait()
speak("Stg", "You notice a set of clothes on the bed.")
wait()
speak("Stg", "You change into the clothes, They fit perfectly.")
proceed()

# Searching the room
speak("Stg", "You look around the room.")
wait()
speak("Stg", "It's a small room, with a bed, a table, and a chair.")
wait()
speak("Stg", "There's a window, but it's too high to see out of.")
wait()
speak("Stg", "There's a wooden splinted door at the end of the room.")
wait()
speak("Stg", "You notice a small keyhole in the door.")
wait()
## ASK IF TRY DOOR
speak("Stg", "Do you try the door?")
wait()
speak("Stg", "1. Yes")
speak("Stg", "2. No")
wait()
speak("Stg", "What do you do?")

complete = False
while not complete:
    openthedoor = input(">> ")
    if openthedoor == "1":
        speak("Stg", "You try the door, but it's locked.")
        wait()
        speak("Stg", "You'll need a key to open it.")
        wait()
        speak("Stg", "You decide to look around the room.")
        wait()
    elif openthedoor == "2":
        speak("Stg", "You decide to look around the room.")
        wait()
    else:
        speak("Stg", "You might want to try that again.")
    
# Continuing searching the room
speak("Stg", "You notice a sleek wardrobe hidden in the corner of the room.")
wait()
speak("Stg", "You open the wardrobe.")
wait()
speak("Stg", "Inside, you find a set of keys.")
wait()
speak("Stg", "You take the keys.")
wait(4)  # Dramatic Effect

speak("??", "Huh!?  Leaving so soon?")
wait()
speak("Stg", "The figure from earlier stands in the doorway.")
wait()
speak("??", "I realised I never introduced myself.")
wait()
speak("??", "How rude of me.   My name is Ana.")
wait()
speak("Stg", "Ana smiles warmly.")
wait()
speak("Ana", "What's your name?")
wait()

# Getting players name
speak("You", "My mame is...")
player.name = input(">> ")
speak("You", f"{player.name}.")
proceed()

speak("Ana", f"Well, {player.name}, it's a pleasure to meet you.")
wait()
speak("Ana", "I hope you're feeling better.")
wait()
speak("Ana", "I'm sure you have a lot of questions.")
wait()
speak("Ana", "I'll answer what I can.")
wait()
speak("Ana", "But first, I have something to show you.")
wait()
speak("Ana", "Come with me.")
wait(5)
proceed()

speak("Stg", "Ana leads you out of the room.")
wait()
speak("Stg", "You follow her out of the room, and into a long hallway.")
wait()
speak("Stg", "The hallway is lined with doors,   at least a dozen on each side.")
wait()
speak("Stg", "No two doors are the same,   and they all have weird symbols on them.")
wait()
speak("??", "No way.. It's the lo-")
wait()
speak("??", "-st one!")
