#It starts from system and ends by exit.
from sys import exit
#Defining start
def start():
    print "You are trapped in a dark room. You have a candle and a raw meat in front of you."
    print "A voice came out from the ceiling."
    print "You weren't appreciating of your life. Let me teach you how marvelous a life is."
    print "<<<Instruction: You can move to the next room only with a candle. The candle lasts for 2 moves."
    print "The spare candle is in the room #3.>>>"
    room_1()
#Defining room_1
def room_1():
    print "You've entered the first room. Which direction would you go?"
    print "Type Left, Right, or Forward"

    choice = raw_input("> ")
    if choice == "Left":
        room_4()
    elif choice == "Right":
        dead_end()
    elif choice == "Forward":
        room_2()
    else:
        dead("You didn't follow my directions.")
#Defining room_2
def room_2():
    print "You've entered the second room. Which direction would you go?"
    print "Type Left, Right, or Forward"

    choice = raw_input("> ")
    if choice == "Left":
        room_5()
    elif choice == "Right":
        dead_end()
    elif choice == "Forward":
        room_3()
    else:
        dead()
#Defining room_3
def room_3():
    print "You've entered the third room."
    print "You've found a spare candle."
    print "Which direction would you go?"
    print "Type Left, Right, or Forward"

    choice = raw_input("> ")
    if choice == "Left":
        room_6()
    elif choice == "Right":
        dead_end()
    elif choice == "Forward":
        dead_end()
    else:
        dead("You didn't follow my directions.")
#Defining room_4
def room_4():
    print "You've entered the fourth room. Which direction would you go?"
    print "Type Left, Right, or Forward"

    choice = raw_input("> ")
    if choice == "Left":
        dead_end()
    elif choice == "Right":
        room_1()
    elif choice == "Forward":
        room_5()
    else:
        dead("You didn't follow my directions.")
#Defining room_5
def room_5():
    print "You've entered the fifth room."
    print "The light of the candle is very weak now. You need a spare candle to move."
    print "Which direction would you go?"
    print "Type Left, Right, or Forward"

    choice = raw_input("> ")
    if choice == "Left":
        darkness()
    elif choice == "Right":
        darkness()
    elif choice == "Forward":
        darkness()
    else:
        dead("You didn't follow my directions.")
#Defining room_6
def room_6():
    print "You've entered the sixth room. Which direction would you go?"
    print "Type Left, Right, or Forward"

    choice = raw_input("> ")
    if choice == "Left":
        dead_end()
    elif choice == "Right":
        room_3()
    elif choice == "Forward":
        clear()
    else:
        dead("You didn't follow my directions.")
#Defining dead_end
def dead_end():
    print "It is a dead end."
    print "Invisible wall snake swallowed your whole body."
    dead()
#Defining clear
def clear():
    print "Congratulations!"
    print "I hope you've understood how precious your life is.."
    exit(0)
#Defining dead by not following directions
def dead():
    print "You didn't follow my directions."
    exit(0)
#Defining running out of candle.
def darkness():
    print "Your candle ran out."
    print "You try to walk without a candle."
    print "."
    print "."
    print "."
    print "."
    print "."
    print "You've walked for an hour, but not even a single door appears."
    print "Something from the dark suddenly grabbed you and you are not there anymore."
    exit(0)
#starts start()
start()
