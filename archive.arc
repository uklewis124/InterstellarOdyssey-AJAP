# Eating Breakfast
speak("Stg", "You eat the eggs and bacon.  They're delicious.")
speak("Think", "I don't remember the last time I had a meal this good!")
speak("Think", "I should probably get changed.")
speak("Stg", "You notice a set of clothes on the bed.")
speak("Stg", "You change into the clothes, They fit perfectly.")
proceed()

# Searching the room
speak("Stg", "You look around the room.")
speak("Stg", "It's a small room, with a bed, a table, and a chair.")
speak("Stg", "There's a window, but it's too high to see out of.")
speak("Stg", "There's a wooden splinted door at the end of the room.")
speak("Stg", "You notice a small keyhole in the door.")
## ASK IF TRY DOOR
speak("Stg", "Do you try the door?")
speak("Stg", "1. Yes")
speak("Stg", "2. No")
speak("Stg", "What do you do?")

complete = False
while not complete:
    openthedoor = input(">> ")
    if openthedoor == "1":
        speak("Stg", "You try the door, but it's locked.")
        speak("Stg", "You'll need a key to open it.")
        speak("Stg", "You decide to look around the room.")
        complete = True
    elif openthedoor == "2":
        speak("Stg", "You decide to look around the room.")
        complete = True
    else:
        speak("Stg", "You might want to try that again.")
    
# Continuing searching the room
speak("Stg", "You notice a sleek wardrobe hidden in the corner of the room.")
speak("Stg", "You open the wardrobe.")
speak("Stg", "Inside, you find a set of keys.")
speak("Stg", "You take the keys.")
speak("Stg", "                                                                                                ")

speak("??", "Huh!?  Leaving so soon?")
speak("Stg", "The figure from earlier stands in the doorway.")
speak("??", "I realised I never introduced myself.")
speak("??", "How rude of me.   My name is Ana.")
speak("Stg", "Ana smiles warmly.")
speak("Ana", "What's your name?")


# Getting players name
speak("You", "My name is...")
player.name = input(">> ")
speak(player.name, f"{player.name}.", wait_tog = False)
proceed()

speak("Ana", f"Well, {player.name}, it's a pleasure to meet you.")
speak("Ana", "I hope you're feeling better.")
speak("Ana", "I'm sure you have a lot of questions.")
speak("Think", "You can say that again...")
speak("Ana", "I'll answer what I can.")
speak("Ana", "But first, I have something to show you.")
speak(player.name, "Huh?           ")
speak("Ana", "Come with me.", wait_tog = 3)
proceed()

speak("Stg", "Ana leads you out of the room.")
speak("Stg", "You follow her out of the room, and into a long hallway.")
speak("Stg", "The hallway is lined with doors,   at least a dozen on each side.")
speak("Stg", "No two doors are the same,   and they all have weird symbols on them.")
speak("??", "psswsspsss")
speak("Stg", "You hear a bunch of whispers coming from behind two large doors at the end of the hallway.")
speak("Stg", "As you approach, the whispers grow louder and louder")
speak("Stg", "Until...", wait_tog = 3)
speak("??", "")