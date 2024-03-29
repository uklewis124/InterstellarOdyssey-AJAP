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

def wait(length=2.6):
    time.sleep(length)

def speak(char, text, delay=0.05, wait_tog=True):    
    # DEBUG:
    debug = False
    if debug:
        print(Fore.MAGENTA, char, " | ", "Character")
        print(Fore.MAGENTA, text, " | ", "Text")
        print(Fore.MAGENTA, delay, " | ", "Delay")
    
    # TYPE TRUE = NOT A CHARACTER
    characters = {
        "You": {"Color": Fore.CYAN, "Type": False},
        player.name: {"Color": Fore.CYAN, "Type": False},
        "??": {"Color": Fore.RED, "Type": False},
        "A group of people": {"Color": Fore.RED, "Type": False},
        
        "Ana": {"Color": Fore.BLUE, "Type": False},
        "1": {"Color": Fore.GREEN, "Type": False},
        "2": {"Color": Fore.YELLOW, "Type": False},
        
        "Stg": {"Color": Fore.RED, "Type": True},
        "Think": {"Color": f"{Fore.GREEN}{Style.BRIGHT}", "Type": True},
        "White": {"Color": Fore.WHITE, "Type": True}
    }
    complete = False
    # If a character
    if not characters[char]["Type"]:
        if char in characters:
            print(f"{characters[char]['Color']}{char} | ", end="")
            for letter in text:
                sys.stdout.write(letter)
                sys.stdout.flush()
                time.sleep(delay)
            print()
            complete = True
    # If not a character and white      
    if char == "White" and not complete:
        for letter in text:
            sys.stdout.write(f"{characters[char]['Color']}{letter}")
            sys.stdout.flush()
            time.sleep(delay)
        print()
        complete = True
    # If not a character and not white ("Think")
    if char == "Think" and not complete:
        if not complete:
            print(f"{characters[char]['Color']}" + '"', end="")
            for letter in text:
                sys.stdout.write(characters[char]['Color'] + letter)
                sys.stdout.flush()
                time.sleep(delay)
            sys.stdout.write(characters[char]['Color'] + '"')
            sys.stdout.flush()
            time.sleep(delay)
            print()
            complete = True
    # If stage
    elif char == "Stg":
        if not complete:
            print("", end="")
            for letter in text:
                sys.stdout.write(characters[char]['Color'] + letter)
                sys.stdout.flush()
                time.sleep(delay)
            print()
            complete = True


    
    if complete:
        # WAITING
        if wait_tog == True:
            wait()
        elif wait_tog != False:
            wait(wait_tog)
        # If specifically told not to wait
        else:
            pass
            
        

def proceed():
    input(f"{Fore.RED}Press Enter to continue...")
    clear()

class Player:
    def __init__(self):
        self.name = ""

player = Player()
## START OF DAY 1 ##

print("")
speak("Stg", "Day ?? - Where am I?", wait_tog = False)
speak("Stg", "=====================", wait_tog = False)
print("")

wait(2)

speak("Think", "Huh?   Where am I?")
speak("Think", "I don't remember a th-", wait_tog = 3)
clear()
speak("Stg", "You awake to a loud thud.  A figure stands over you, a mug in hand.", wait_tog = 3)
print()
speak("??", "You're finally awake.. I was beginning to think you'd never wake up.")
speak("You", "Where am I?")
speak("??", "You're not sure? Well, I suppose that's to be expected.")
speak("??", "I saw you in the wilderness of Charterland. You were unconscious, so I brought you here.")
speak("You", "Charterland? I've never heard of it.")
speak("??", "That's because it's a secret.  You're not from around here, are you?")
speak("You", "I don't think so.")
speak("You", "I don't remember anything.")
speak("??", "I see.  Well, I'm sure you'll remember soon enough.")
speak("??", "I've made you some breakfast. You must be hungry.")
speak("Stg", "The figure hands you a plate of eggs and bacon.")
speak("??", "I'm sure you have a lot of questions.  I'll answer what I can.")
speak("??", "But first, eat up.  You'll need your strength.", wait_tog = 5)
proceed()

speak("Stg", """
You eagerly dig into the breakfast, your stomach grumbling as you realize just how hungry you are. The eggs are
perfectly scrambled, and the bacon is crispy and delicious.

As you eat, you can't help but steal glances at the mysterious figure who rescued you. As you steal glances at the
figure while devouring the delicious breakfast, you can't help but admire their apperance. They exude an air of
mystery, their features both caprivating and enigmatic. They have piercing eyes, the color of stormy seas,
which seem to hold untold depths of wisdom and experience. Their hair, a tousled mane of midnight black, frames
their face in a way that accentuates their sharp cheekbones and stong jawline. 

Despite the seriousness of the situation, there's a warmth to their smile that puts you at ease. Their presence is
reassuring, like a steady beacon in the midst of uncertainty. Clad in simple yet elegant attire that hints
at a life spent traversing both worlds mundane and magical, their exudes a sense of confidence and strength.

As you continue to eat, you find yourself drawn to their mannerisms—the way they speak with a quiet authority, the way they
move with a grace that belies their apparent strength. There something undeniably intriguing about them, something that
makes you want to unravel the mysteries they hold within.

Lost in your thoughts, you almost forget the gravity of your situation. But as you meet their gaze once more, you're 
reminded that there are still unanswered questions looming overhead, waiting to be unraveled in this strange and
mysterious land.
""")
proceed()