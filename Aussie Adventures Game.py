print("G'day, welcome to Aussie Adventure!")

name = input("What's your name? ")
age = int(input("How old are you " + name + "? "))

def introScene():
    directions = ["left", "right"]
    print("You are stood in your gumboots on a dusty road. It's getting hot so you'd better move - which way do you go?")
    playerinput = ""
    while playerinput not in directions:
        print("Options: left/right")
        playerinput = input()
        if playerinput == "left":
            houseScene()
        elif playerinput == "right":
            bushScene()
        else:
            print("Please enter a valid direction.")

def houseScene():
    directions = ["left", "right"]
    print("You see a house at the side of the road as you walk. You are tired - what do you do? Enter the house, or continue?")
    playerinput = ""
    while playerinput not in directions:
        print("Options: enter/continue")
        playerinput = input()
        if playerinput == "enter":
            hallScene()
        elif playerinput == "continue":
            operahouseScene()
        else:
            print("Please enter a valid choice.")

def operahouseScene():
    directions = ["left", "right"]
    print("You see a house at the side of the road as you walk. You are tired - what do you do? Enter the house, or continue?")
    playerinput = ""
    while playerinput not in directions:
        print("Options: harbour/enter")
        playerinput = input()
        if playerinput == "enter":
            fostersScene()
        elif playerinput == "harbour":
            print("Oh crikey, you fell in the harbour! You lose!")
        else:
            print("Please enter a valid choice.")

if age >= 18:
    print("Bonza, you are old enough to play!")

    wants_to_play = input("Do you want to play? ").lower()
    if wants_to_play == "yes":
        print("Right on, lets play!")

        introScene()

    else:
        print("Goodbye then", name + "!")

else:
    print("Sorry, you are not old enough to play.")