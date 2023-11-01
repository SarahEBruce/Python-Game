print("G'day, welcome to Aussie Adventure!")

name = input("What's your name? ")
age = int(input("How old are you " + name + "? "))

health = 10

if age >= 18:
    print("Bonza, you are old enough to play!")

    wants_to_play = input("Do you want to play? ").lower()
    if wants_to_play == "yes":
        print("Right on, lets play! You are starting at", health, "health.")

        direction = input("Which way would you like to go, right or left? (right/left) ").lower()
        if direction == "left":
            ans = input("You head along the road toward the city and see a house to your left. Do you go in, or continue past (enter/pass)? ").lower()

            if ans == "enter"
                print("Bad move! The house has a Huntsman the other side of the door. The fright lost you 5 health.")
                health -= 5

            else:
                ans = input("Nice! You see Sydney Opera house to your right, and the harbour to your left, where do you go? (left/right? "))

                if ans == "left"
                    print("You fell in the harbour and lost 5 health.")

        else:
            print("Dang, you went into the bush and got bitten by a deadly snake. You lost...")

    else:
        print("Goodbye then", name + "!")

else:
    print("Sorry, you are not old enough to play.")