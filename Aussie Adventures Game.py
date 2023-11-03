#Welcome player to game
print("G'day, welcome to Aussie Adventure!")

#verify player name and age
name = input("What's your name? ")
age = int(input("How old are you " + name + "? "))

#if old enough continue to play
if age >= 18:
    print("Bonza, you are old enough to play!")

#verify if player wants to play
    wants_to_play = input("Do you want to play? ").lower()
    if wants_to_play == "yes":
        print("Right on, lets play!")

#First scenario question
        answer = input("You are stood in your gumboots on a dusty road. It's getting hot so you'd better move - which way do you go? (Options: left/right) ").lower()

        if answer == "left":
            answer = input("You see a house at the side of the road as you walk. You are tired - what do you do? Enter the house, or continue? (Options: enter/continue) ").lower()
            if answer == "enter":
                answer = input()
            elif answer == "continue":
                print("You see Sydney up ahead, with the harbour and the Opera House - what a sight,", name + "!")
                answer = input("Where do you go? (Options: harbour/opera house) ").lower()
                if answer == "harbour":
                        print("Oh crikey, you fell in the harbour! You lose!")
                elif answer == "opera house":
                        answer = input()
            else: print("Please enter a valid answer.")

        elif answer == "right":
            answer = input()

#exit game if player does not choose to play
    else:
        print("Goodbye then", name + "!")

#exit game if player is under 18
else:
    print("Sorry, you are not old enough to play.")