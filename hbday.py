# An interactive fiction based on 'Happy Birthday' from Resident Evil 7.
# Author: Sævar Ingi Sigurðsson

from sys import exit

# Global variables for items collected.
candle = False
key = False
telescope = False
finger = False
balloon = False
quill = False
crank_wheel = False

# Global variables for environment status.
candle_lit = True
water_on = True
oil_floor = False
stove_on = False
rope_on = True
lock1_open = False
lock2_open = False
finger_on = False
quill_in = False


# Prints out helpful information about the game.
def rules():
    print "-" * 60
    print "This is a text-based escape game."
    print "To play, simply type what you want to do when asked to."
    print "You are more likely to hit the correct keywords by being concise."
    print "For example: \"eat fish\" is better than \"eat the little fish\"."
    print "To move between rooms, type then name of the room."
    print "You can only move to adjacent rooms."
    print "For example: \"go to kitchen\" works \"go left\" does not."
    print "\n"
    print "Commands:"
    print "\"rules\": Show this text again."
    print "\"look around\": Get room description again."
    print "-" * 60


# Starts the game.
def start():
    print "-" * 60
    print "Type \"rules\" for game information."
    print "-" * 60
    print "You wake up in a darkened room."
    print "An animatronic clown is sitting by the wall, holding a lit candle."
    print "The bathroom is in front of you and the kitchen to your left."

    global candle

    while True:
        print "What do you do?"
        print "-" * 60

        choice = raw_input('> ')

        if "pick up candle" in choice and candle == False:
            print "-" * 60
            print "You pick up the lit candle."
            print "A speaker voice tells you to put the lit candle on the birthday cake in the dining room."
            candle = True
        elif "pick up candle" in choice and candle == True:
            print "-" * 60
            print "You already have the damn candle!"
        elif "bathroom" in choice and candle == True:
            print "-" * 60
            print "There is nothing for you there at the moment."
        elif "kitchen" in choice and candle == True:
            kitchen_1()
        elif choice == "rules":
            rules()
        elif choice == "look around":
            print "-" * 60
            print "You wake up in a darkened room."
            print "An animatronic clown is sitting by the wall, holding a lit candle."
            print "The bathroom is in front of you and the kitchen to your left."
        elif candle == True:
            print "-" * 60
            print "Try exploring the rooms."
        else:
            print "-" * 60
            print "You should really pick the candle up."


# First time you enter the kitchen.
def kitchen_1():
    print "-" * 60
    print "You enter the kitchen."
    print "There's a stove here and an open gas main on the wall."
    print "In front of you is the parlor and to your right is the dining room."
    print "You can see a big birthday cake on the table in there."

    while True:
        print "What do you do?"
        print "-" * 60

        choice = raw_input('> ')

        if "dining room" in choice:
            dining_room()
        elif choice == "rules":
            rules()
        elif choice == "look around":
            print "-" * 60
            print "The kitchen."
            print "There's a stove here and an open gas main on the wall."
            print "In front of you is the parlor and to your right is the dining room."
            print "You can see a big birthday cake on the table in there."
        else:
            print "-" * 60
            print "The cake is right there! Go into the dining room and light it!"


# Contains what happens when you interact with stuff in the dining room.
def dining_room():
    global water_on
    global candle_lit
    global oil_floor
    global key
    global finger
    global lock1_open

    print "-" * 60
    print "As you enter the dining room you are met with a spray of water!"
    print "Your candle goes out."
    print "The voice reminds you that the candle has to be lit."
    print "On your right is an oil barrel with a key in it."
    print "On your left is a water main, it's crank wheel is missing."
    if lock1_open == False:
        print "There is a locked box on the wall. The lock needs 3 symbols to open."
    else:
        pass
    print "On the table is a huge birthday cake."

    candle_lit = False


    while True:
        print "What do you do?"
        print "-" * 60

        choice = raw_input('> ')

        if "take key" in choice and key == False:
            print "-" * 60
            print "You take the key from the barrel. Oil starts spilling everywhere!"
            key = True
            oil_floor = True
        elif "open lock" in choice and finger == False and lock1_open == False:
            print "#" * 60
            print "What is the passcode? (seperate by commas)"
            print "#" * 60

            passcode  = raw_input('> ')

            if passcode == "crow, bell tower, willow":
                print "-" * 60
                print "You open the box, inside is an animatronic finger. You take it."
                lock1_open = True
                finger = True
            else:
                print "-" * 60
                print "The box is locked. You step back."
        elif "open lock" in choice and lock1_open == True:
            print "-" * 60
            print "The box is unlocked and empty."
        elif "candle on the cake" in choice and candle_lit == False:
            print "-" * 60
            print "We've been over this. The candle must be lit."
        elif "kitchen" in choice and water_on == True:
            print "-" * 60
            print "You get sprayed again as you leave the dining room."
            candle_lit = False
            kitchen_2()
        elif "kitchen" in choice and water_on == False:
            kitchen_2()
        elif "turn off water" and crank_wheel == True and water_on == True:
            print "-" * 60
            print "You use the crank wheel to turn off the water!"
            water_on = False
        elif choice == "rules":
            rules()
        elif choice == "look around":
            print "-" * 60
            print "The dining room"
            print "On your right is an oil barrel with a key in it."
            print "On your left is a water main, it's crank wheel is missing."
            if lock1_open == False:
                print "There is a locked box on the wall. The lock needs 3 symbols to open."
            else:
                pass
            print "On the table is a huge birthday cake."
        else:
            print "-" * 60
            print "Do something intelligent, please."


# Contains what happens when you interact with stuff in the kitchen.
def kitchen_2():
    print "-" * 60
    print "You are in the kitchen."
    print "There's a stove here and an open gas main on the wall."
    print "You can enter the parlor, dining room or entrance from here."

    global stove_on
    global candle_lit
    global balloon
    global quill

    while True:
        print "What do you do?"
        print "-" * 60

        choice = raw_input('> ')

        if "dining room" in choice and candle_lit == True and water_on == False:
            endgame()
        elif "entrance" in choice:
            entrance()
        elif "parlor" in choice:
            parlor()
        elif "dining room" in choice:
            dining_room()
        elif "light stove" in choice and stove_on == False:
            print "-" * 60
            print "You turn on the stove."
            stove_on = True
        elif "light stove" in choice and stove_on == True:
            print "-" * 60
            print "The stove is clearly on...there's fire and everything!"
        elif "light candle" in choice and stove_on == False:
            print "-" * 60
            print "The stove is off, how are you going to light your candle with it?"
        elif "light candle" in choice and stove_on == True:
            print "-" * 60
            print "You light your candle!"
            candle_lit = True
        elif "inflate balloon" in choice and balloon == True:
            print "-" * 60
            print "You inflate the balloon until it pops!"
            print "You yell out in pain!"
            print "A feather quill is sticking out of your abdomen. You remove it."
            quill = True
            balloon = False
        elif "inflate balloon" in choice and balloon == False:
            print "-" * 60
            print "What balloon?"
        elif choice == "rules":
            rules()
        elif choice == "look around":
            print "-" * 60
            print "The kitchen."
            print "There's a stove here and an open gas main on the wall."
            print "You can enter the parlor, dining room or entrance from here."
        else:
            print "-" * 60
            print "Do something intelligent, please."


# Contains what happens when you interact with stuff in the entrance.
def entrance():
    print "-" * 60
    print "You are at the entrance."
    print "You can enter the kitchen or the bathroom from here."
    print "The creepy clown robot is still here, looking ominous."

    while True:
        print "What do you do?"
        print "-" * 60

        choice = raw_input('> ')

        if "bathroom" in choice:
            bathroom()
        elif "kitchen" in choice:
            kitchen_2()
        elif "clown" in choice:
            clown()
        elif choice == "rules":
            rules()
        elif choice == "look around":
            print "-" * 60
            print "The entrance."
            print "You can enter the kitchen or the bathroom from here."
            print "The creepy clown robot is still here, looking ominous."
        else:
            print "-" * 60
            print "Do something intelligent, please."


# Contains what happens when you interact with stuff in the bathroom.
def bathroom():
    print "-" * 60
    print "You enter the bathroom."
    print "It looks like it hasn't been cleaned in years. Ugh!"
    print "There is a toilet here and nothing more."

    global telescope

    while True:
        print "Do you want to flush it?"
        print "-" * 60

        choice = raw_input('> ')

        if "yes" in choice and telescope == False:
            print "-" * 60
            print "The toilet is clogged and fills with water."
            print "There is a metal object floating in the water!"
            print "You pick it up (disgusting...) and see that it's a telescope."
            print "You stash it for later, and leave the bathroom."
            telescope = True
            entrance()
        elif "no" in choice and telescope == False:
            print "-" * 60
            print "Oh come on. What's the worst that could happen?"
        elif "yes" in choice and telescope == True:
            print "-" * 60
            print "Why the hell would you flush it again, it's clogged!"
        elif "no" in choice and telescope == True:
            print "Smart man, it is clogged after all. You leave."
            entrance()
        elif choice == "rules":
            rules()
        elif choice == "look around":
            print "-" * 60
            print "The bathroom."
            print "It looks like it hasn't been cleaned in years. Ugh!"
            print "There is a toilet here and nothing more."
        else:
            print "-" * 60
            print "Fine. Be a wuss. You leave the bathroom."
            entrance()


# Contains what happens when you interact with the clown.
def clown():
    global finger
    global quill
    global finger_on
    global quill_in

    print "-" * 60
    print "You approach the clown."
    print "Now that you can see it properly you notice that it needs to be wound up."
    if finger_on == False:
        print "It also appears to be missing a finger."
    else:
        pass

    while True:
        print "What do you do?"
        print "-" * 60

        choice = raw_input('> ')

        if "wind up" in choice and key == True and finger_on == True and quill_in == True:
            print "-" * 60
            print "The clown grabs your arm and starts writing!"
            print "It's writing into your skin! You scream in pain!"
            print "L O S E R"
            print "Laughing, the clown releases you and shuts down. Your arm hurts like hell."
            print "-" * 60
            entrance()
        elif "wind up" in choice and key == True and finger_on == True:
            print "-" * 60
            print "You use the key to wind up the clown."
            print "It moves its hand and laughs like it is writing something funny."
            print "But nothing else happens."
        elif "wind up" in choice and key == True:
            print "-" * 60
            print "You use the key to wind up the clown."
            print "It moves its hand and laughs like it is writing something funny."
            print "But nothing else happens."
        elif "finger" in choice and finger == True and finger_on == False:
            print "-" * 60
            print "You place the animatronic finger on the clowns hand."
            print "It looks like it should be holding something."
            finger = False
            finger_on = True
        elif "quill" in choice and finger_on == False and quill == True and quill_in == False:
            print "-" * 60
            print "It won't fit, something is missing."
        elif "quill" in choice and finger_on == True and quill == True and quill_in == False:
            print "-" * 60
            print "You place the quill in the clowns hand."
            quill = False
            quill_in = True
        elif "leave" in choice:
            print "-" * 60
            print "You leave the clown alone for now."
            entrance()
        elif choice == "rules":
            rules()
        elif choice == "look around":
            print "-" * 60
            print "The clown."
            print "Now that you can see it properly you notice that it needs to be wound up."
            if finger_on == False:
                print "It also appears to be missing a finger."
            else:
                pass
        else:
            print "-" * 60
            print "Do something intelligent, please."


# Contains what happens when you interact with stuff in the parlor.
def parlor():
    global rope_on

    if rope_on == True and crank_wheel == False:
        print "-" * 60
        print "You are in the parlor."
        print "There are three monitors on the wall."
        print "There is a door tied shut with a rope. You can only enter the kitchen from here."
        print "Through a hole in the wall you see the crank wheel needed to turn off the water!"
    elif rope_on == False and crank_wheel == False:
        print "-" * 60
        print "You are in the parlor."
        print "There are three monitors on the wall."
        print "There is a door you can open here and you can enter the kitchen."
        print "Through a hole in the wall you see the crank wheel needed to turn off the water!"
    else:
        print "-" * 60
        print "You are in the parlor."
        print "There are three monitors on the wall."
        print "There is a door you can open here and you can enter the kitchen."

    while True:
        print "What do you do?"
        print "-" * 60

        choice = raw_input('> ')

        if "door" in choice and rope_on == False:
            print "-" * 60
            print "You go through the door."
            balloon_hall()
        elif "door" in choice and rope_on == True:
            print "-" * 60
            print "The rope is keeping the door shut. If only you could get rid of it."
        elif "burn rope" in choice and candle_lit == True and rope_on == True:
            print "-" * 60
            print "You use the candle to burn the rope! The door is now open."
            rope_on = False
        elif "burn rope" in  choice and candle_lit == False:
            print "-" * 60
            print "How are you going to burn it?"
        elif "cut rope" in choice and rope_on == True:
            print "-" * 60
            print "The rope is too strong for you to cut it or rip it."
        elif "monitors" in choice and "telescope" in choice and telescope == True:
            print "-" * 60
            print "Looking at the monitors through the telescope you see something!"
            print "On the left monitor there is a picture of a crow."
            print "On the middle monitor there is a picture of a bell tower."
            print "On the right monitor there is a picture of a willow."
        elif "monitors" in choice:
            print "-" * 60
            print "The monitors are just fuzzy."
        elif "hole" in choice:
            print "-" * 60
            print "You can't get through the hole. There must be anoter way."
        elif "kitchen" in choice:
            kitchen_2()
        elif choice == "rules":
            rules()
        elif choice == "look around":
            if rope_on == True:
                print "-" * 60
                print "The parlor."
                print "There are three monitors on the wall."
                print "There is a door tied shut with a rope. You can only enter the kitchen from here."
                print "Through a hole in the wall you see the crank wheel needed to turn off the water!"
            else:
                print "-" * 60
                print "The parlor."
                print "There are three monitors on the wall."
                print "There is an open door here and you can enter the kitchen."
                print "Through a hole in the wall you see the crank wheel needed to turn off the water!"
        else:
            print "-" * 60
            print "Do something intelligent, please."


# Contains what happens when you interact with stuff in the balloon hallway.
def balloon_hall():
    print "-" * 60
    print "You find yourself in a hallway filled with gray balloons."
    print "You feel like they're here to hide something."
    print "At the far end is a locked door. Its lock needs a five letter code."

    global balloon
    global lock2_open

    while True:
        print "What do you do?"
        print "-" * 60

        choice = raw_input('> ')

        if "search" in choice:
            print "-" * 60
            print "Searching the sea of balloon reveals a yellow, uninflated balloon."
            print "You stash it for later."
            balloon = True
        elif "open lock" in choice and lock2_open == False:
            print "#" * 60
            print "What is the password? (5 letters, seperated by whitespace)"
            print "#" * 60
            password  = raw_input('> ')
            if password == "L O S E R":
                print "-" * 60
                print "The lock opens. You can open the door."
                lock2_open = True
            else:
                print "-" * 60
                print "The door is locked. You step back."
        elif "parlor" in choice:
            parlor()
        elif "open door" in choice and lock2_open == True:
            crank_room()
        elif choice == "rules":
            rules()
        elif choice == "look around":
            print "-" * 60
            print "The balloon hallway."
            print "At the far end is a locked door. Its lock needs a five letter code."
        else:
            print "-" * 60
            print "Do something intelligent, please."


# Contains what happens when you interact with stuff in the crank room.
def crank_room():
    print "-" * 60
    print "You have found the entrance to the room with the crank wheel!"
    print "Do you want to take it?"
    print "-" * 60

    global crank_wheel

    while True:
        choice = raw_input('> ')

        if "yes" in choice:
            print "-" * 60
            print "You take the crank wheel and leave the room."
            print "-" * 60
            crank_wheel = True
            balloon_hall()
        elif choice == "rules":
            rules()
        elif choice == "look around":
            print "-" * 60
            print "You have found the entrance to the room with the crank wheel!"
            print "Do you want to take it?"
            print "-" * 60
        else:
            print "-" * 60
            dead("You really should have taken that crank wheel...idiot.")


# Contains what happens when you interact with stuff in the endgame.
def endgame():
    print "-" * 60
    print "As you enter the dining room the door slams shut behind you!"
    print "On the table is a huge birthday cake."
    print "Put the candle on the cake. What could possibly go wrong..."

    while True:
        print "What do you do?"
        print "-" * 60

        choice = raw_input('> ')

        if "candle on the cake" in choice and oil_floor == True:
            print "-" * 60
            print "The cake starts ticking ominously."
            print "You can hear the clown lauging outside."
            print "The cake explodes and the oil catches fire!"
            print "You are burned alive."
            print "-" * 60
            dead("No one escapes this place. Or do they?")
        elif "candle on the cake" in choice and oil_floor == False:
            print "-" * 60
            print "The cake starts ticking ominously."
            print "You can hear the clown lauging outside."
            print "The cake explodes!"
            print "Your ears hurt but otherwise you are fine."
            print "The explosion has blown a hole in the wall for you to pass through."
            win()
        elif choice == "rules":
            rules()
        elif choice == "look around":
            print "-" * 60
            print "The dining room (with your precious lit candle)."
            print "The door has shut behind you!"
            print "On the table is a huge birthday cake."
            print "Put the candle on the cake. What could possibly go wrong..."
        else:
            print "-" * 60
            print "Put the candle on the cake!"


# Tells you when you die, and why (usually). Allows you to try again.
def dead(why):
    print "You are dead."
    print why
    print "-" * 60
    print "Do you want to try again? y/n"

    while True:
        choice = raw_input('> ')

        if choice == "y":
            reset_globals()
            start()
        elif choice == "n":
            exit(0)
        else:
            print "You must answer with \"y\" or \"n\"."


# Tells you if you win the game. Yes you can win!
def win():
    print "-" * 60
    print "You make your way outside and feel the sun on your face."
    print "Congratulations, you are free!"
    print "Ears still hurt tho...stupid exploding cake."
    print "-" * 60
    exit(0)


# Resets all global variables to their original state.
def reset_globals():

    global candle
    global key
    global telescope
    global finger
    global balloon
    global quill
    global crank_wheel

    global candle_lit
    global water_on
    global oil_floor
    global stove_on
    global rope_on
    global lock1_open
    global lock2_open
    global finger_on
    global quill_in

    # Reset item status
    candle = False
    key = False
    telescope = False
    finger = False
    balloon = False
    quill = False
    crank_wheel = False

    # Reset environment status
    candle_lit = True
    water_on = True
    oil_floor = False
    stove_on = False
    rope_on = True
    lock1_open = False
    lock2_open = False
    finger_on = False
    quill_in = False


# Starts the game automatically when script is run.
start()
