# Dungeon of Madness - Beta
# By Lukas Senkus P110112760

### PACKAGES ###
import os
import sys
import time

### GLOBAL VARIABLES ###
### Used to save information on what user did or collected ###
Locked_Door = []
Inventory = []
Coins = []
Key = []
Wall_Crack = []
Brick_Entrance = []

### ROOM LAYOUT & DECISIONS ###
### IN THIS SECTION THERE WILL DIFFEREMT ROOMS AND EACH OF THOSE ROOMS WILL HAVE DIFFERENT OPTIONS ###
### .lower ensures that the user input is being proccessed as lowercase incase of misspelling ###

def first_room():
    os.system("cls") # Used to clear the terminal (Only works for Windows)
    print("You are in an empty room. There is a door to the north, and a door to the west.\nBehind you to the south is the stairs that lead back to the entrance.")
    task_1 = input("What would you like to do? [Look], [Move], [Action] or [Collect].\n-> ")

### LOOK INPUT ####

    if task_1.lower() == "look":
        print("You look around the room...")
        time.sleep(2)
        print("You keep looking...")
        time.sleep(2)
        print("There was nothing of interest in this room.")
        time.sleep(3)
        first_room()
   
### ACTION INPUT ####

    elif task_1.lower() == "action":
        print("What would you like to do?")
        action_1 = input("[Shout] or [Punch]\n-> ")

        if action_1.lower() == "shout":
            print("You proceed to shout in this room...")
            time.sleep(2)
            print("Nothing happens")
            time.sleep(2)
            first_room()

        elif action_1.lower() == "punch": 
            print("You tried punching the brick wall...")
            time.sleep(2)
            print("Nothing happens")
            time.sleep(2)
            first_room()

        else: 
            print("Choose a correct option and try again...")
            time.sleep(2)
            first_room()

### MOVE INPUT ###

    elif task_1.lower() == "move":
        direction_1 = input("Which direction would you like to move? [North], [South] or [West]?\n-> ")
        if direction_1.lower() == "north":
            if "1" not in Key:
                print("You don't have the key for this door")
                time.sleep(3)
                print("HINT: Walk around the rooms use [Look] or [Action]")
                time.sleep(3)
                first_room()
            elif "1" in Key:
                print("You have a key for this door, would you like to unlock it?")
                decision_key = input("[Yes] or [No]\n-> ")
                if decision_key.lower() == "yes":
                    print("You unlocked the door and walked into the room...")
                    time.sleep(2)
                    treasure_room()
                elif decision_key.lower() == "no":
                    print("You choose to not unlock the door...")
                    time.sleep(2)
                    first_room()
            
        elif direction_1.lower() == "west":
            second_room()
        
        elif direction_1.lower() == "south":
            print("Would you like to exit a dungeon?")
            leave_choice = input("[Yes] or [No]\n-> ")

            if leave_choice.lower() == "yes":
                print("You choose to leave the dungeon without finding the treasure.")
                time.sleep(2)
                os.system("cls") # Used to clear the terminal (Only works for Windows)
                print("Thank you for playing!")
                print("--- Your Stats ---")
                Coinstotal = sum(Coins) 
                print(Inventory)
                print(Coinstotal)
                time.sleep(5)
                sys.exit()


            elif leave_choice.lower() == "no":
                print("You choose to not leave the dungeon and continue looking for the treasure")
                time.sleep(2)
                first_room()

            while leave_choice.lower() is not ["yes", "no"]:
                print("Please choose a valid option")
                print("Would you like to exit a dungeon?")
                leave_choice = input("[Yes] or [No]\n-> ")

                if leave_choice.lower() == "yes":
                    print("You choose to leave the dungeon without finding the treasure.")
                    time.sleep(3)
                    print("--- Your Stats ---")
                    Coinstotal = sum(Coins) 
                    print(Inventory)
                    print(Coinstotal)
                    

                elif leave_choice.lower() == "no":
                    print("You choose to not leave the dungeon and continue looking for the treasure")
                    time.sleep(3)
                    first_room()

        else:
            print("You cannot move there, as there is a brick wall in your way...")
            time.sleep(3)
            first_room()

### COLLECT INPUT ####

    elif task_1.lower() == "collect":
        print("You look around in this room...")
        time.sleep(2)
        print("There is nothing to collect")
        time.sleep(3)
        first_room()

### NO INPUT ###

    else:
        print("!!! Please choose a command from the list !!!")
        time.sleep(3)
        first_room()

def second_room():
    os.system("cls") # Used to clear the terminal (Only works for Windows)
    print("You are in a small room with a table. Upon the table are some letters and a key. There is a door to the East.")
    task_2 = input("What would you like to do? [Look], [Move], [Action] or [Collect].\n-> ")

### LOOK INPUT ###

    if task_2.lower() == "look":
        print("You look around the room...")
        time.sleep(2)
        print("You keep looking...")
        time.sleep(2)
        print("There seems to be a key and some coins on the table, and the brick wall to the north seems to be cracked.")
        time.sleep(4)
        second_room()

### ACTION INPUT ###

    elif task_2.lower() == "action":
        print("What would you like to do?")
        action_2 = input("[Shout] or [Punch]\n-> ")

        if action_2.lower() == "shout":
            print("You proceed to shout in this room...")
            time.sleep(2)
            print("The brick wall seemed to drop a piece which enabled you to see that there is a room behind the wall")
            time.sleep(2)
            print("It seems that you need a small push or punch to break it down.")
            time.sleep(4)
            Wall_Crack.append("1")
            second_room()


        elif action_2.lower() == "punch":
            print("You walk to brick wall to the north...")
            time.sleep(2)
            if "1" not in Wall_Crack:
                print("You're punching the brick wall...")
                time.sleep(2)
                print("Nothing happens")
                time.sleep(2)
                second_room()
            elif "1" in Wall_Crack:
                print("You're punching the brick wall...")
                time.sleep(2)
                print("The brick wall broke down...")
                time.sleep(3)
                Brick_Entrance.append("1")
                print("Would you like to enter the hole in the wall?")
                enter_secret = input("[Yes] or [No]\n-> ")

                if enter_secret.lower() == "yes":
                    print("You're walking into the secret room...")
                    time.sleep(3)
                    secret_room()
                elif enter_secret.lower() == "no":
                    print("You're walking back to the center of the room...")
                    time.sleep(3)  
                    second_room()    
                else:
                    print("Choose a correct option and try again...")
                    time.sleep(2)
                    second_room()
        else:
            print("Choose a correct option and try again...")
            time.sleep(2)
            second_room()

### MOVE INPUT ###

    if task_2.lower() == "move":
        direction_2 = input("Which direction would you like to move? [North] or [East]?\n-> ")
  

        if direction_2.lower() == "east":
            first_room()

        elif "1" in Brick_Entrance:
            secret_room()

        elif direction_2.lower() == "north":
            print("You walk up to the north brick wall...")
            time.sleep(2)
            print("You have a feeling that there is something behind that wall...")
            time.sleep(2)
            print("HINT: Use [Action] or [Look] to figure out your surroundings")
            time.sleep(3)
            second_room()

        else:
            print("You cannot move there, as there is a brick wall in your way...")
            time.sleep(3)
            second_room()

### COLLECT INPUT ###

    if task_2.lower() == "collect":
        print("You walk up to the table...")
        time.sleep(2)

        if 5 in Coins and "1" in Key:
            print("There is nothing to collect here as you already did it...")
            time.sleep(2)
            second_room()

        elif "1" in Key:
            print("There is a some Coins on the table.")
            collecting = input("What would you like collect? [Coins] \n-> ")
            if collecting.lower() == "coins":
                print("You walk up to the table and collect the coins...")
                Coins.append(5)
                time.sleep(2)
                print("You now have: ",Coins," Coins")
                time.sleep(2)
                second_room()
            else:
                print("Choose a correct option and try again...")
                time.sleep(2)
                second_room()


        elif 5 not in Coins:
            print("There is a Key and some Coins on the table.")
            collecting = input("What would you like collect? [KEY] or [COINS]\n-> ")
            if collecting.lower() == "coins":
                if 5 not in Coins:
                    print("You walk up to the table and collect the coins...")
                    Coins.append(5)
                    time.sleep(2)
                    print("You now have: ",Coins," Coins")
                    time.sleep(2)
                    second_room()
                elif 5 in Coins:
                    print("You already collected the coins")
                    time.sleep(2)
                    second_room()
                else:
                    second_room()

            if collecting.lower() == "key":
                if "1" not in Key:
                    print("You walk up to the table and collect the key...")
                    Key.append("1")
                    time.sleep(2)
                    second_room()

        elif 5 in Coins:
            print("There is a Key on the table.")
            collecting = input("What would you like collect? [KEY] \n-> ")
            if collecting.lower() == "key":
                if "1" not in Key:
                    print("You walk up to the table and collect the key...")
                    Key.append("1")
                    time.sleep(2)
                    print("You now have a key!")
                    time.sleep(2)
                    second_room()
                else:
                    print("Choose a correct option and try again...")
                    time.sleep(2)
                    second_room()

### NO INPUT ###

    else:
        print("Choose a correct option and try again...")
        time.sleep(3)
        second_room()

def secret_room():
    os.system("cls") # Used to clear the terminal (Only works for Windows)
    print("You walk inside a room which has a golden statue in the middle. There is only an exit in South")
    task_3 = input("What would you like to do? [Look], [Move], [Action] or [Collect].\n-> ")

### LOOK INPUT ###

    if task_3.lower() == "look":
        print("You look around the room...")
        time.sleep(2)
        print("You keep looking...")
        time.sleep(2)
        print("There is a golden statue in the middle of the room. You might be able to collect it.")
        time.sleep(4)
        secret_room()

### ACTION INPUT ###

    elif task_3.lower() == "action":
        print("What would you like to do?")
        action_3 = input("[Shout] or [Punch]\n-> ")

        if action_3.lower() == "shout":
            print("You proceed to shout in this room...")
            time.sleep(2)
            print("Nothing happens")
            time.sleep(2)
            secret_room()

        elif action_3.lower() == "punch":
            print("You tried punching the brick wall...")
            time.sleep(2)
            print("Nothing happens")
            time.sleep(2)
            secret_room()

        while action_3.lower() is not ["shout", "punch"]:
            print("Please choose a valid option")
            print("What would you like to do?")
            action_3 = input("[Shout] or [Punch]\n-> ")

            if action_3.lower() == "shout":
                print("You proceed to shout in this room...")
                time.sleep(2)
                print("Nothing happens")
                time.sleep(2)
                secret_room()

            elif action_3.lower() == "punch":
                print("You tried punching the wall...")
                time.sleep(2)
                print("Nothing happens")
                time.sleep(2)
                secret_room()

### MOVE INPUT ###

    if task_3.lower() == "move":
        direction_3 = input("Would you like to exit this room? As there is only exit to the South [YES] or [NO]\n-> ")
        if direction_3.lower() == "yes":
            print("You choose to leave this room...")
            time.sleep(2)
            second_room()

        elif direction_3.lower() == "no":
            print("You choose to stay in this room...")
            time.sleep(2)
            secret_room()

        else:
            print("Choose a correct option and try again...")
            time.sleep(3)
            secret_room()

### COLLECT INPUT ###
    if task_3.lower() == "collect":
        if "Golden Statue" in Inventory:
            print("There is nothing here to collect...")
            time.sleep(2)
            secret_room()

        elif "Golden Statue" not in Inventory:
            print("There is a golden statue in the middle of the room...")
            time.sleep(2)
            print("It seems to be really valuable, would you like to collect it?")
            time.sleep(1)
            collect = input("[Yes] or [No]\n-> ")

            if collect.lower() == "yes":
                print("You walk up to the statue and collect it...")
                time.sleep(2)
                Inventory.append("Golden Statue")
                secret_room()

            elif collect.lower() == "no":
                print("You choose to not collect the Golden Statue for some reason...")
                time.sleep(2)
                secret_room() 

            else:
                print("Choose a correct option and try again...")
                time.sleep(3)
                second_room()

### NO INPUT ###

    else:
        print("Choose a correct option and try again...")
        time.sleep(3)
        secret_room()

def treasure_room():
    os.system("cls") # Used to clear the terminal (Only works for Windows)
    print("You are in a dark room. There is a chest in the centre of the room, lit only by the light of the doorway.\nThere is a door to the South.")
    task_4 = input("What would you like to do? [Look], [Move], [Action] or [Collect].\n-> ")

### LOOK INPUT ###

    if task_4.lower() == "look":
        print("You look around the room...")
        time.sleep(2)
        print("You keep looking...")
        time.sleep(2)
        print("There is a chest in the middle of the room. You might be able to open it.")
        time.sleep(4)
        treasure_room()

### ACTION INPUT ###

    elif task_4.lower() == "action":
        print("What would you like to do?")
        action_4 = input("[Shout] or [Punch]\n-> ")

        if action_4.lower() == "shout":
            print("You proceed to shout in this room...")
            time.sleep(2)
            print("Nothing happens")
            time.sleep(2)
            treasure_room()

        elif action_4.lower() == "punch":
            print("You tried punching the brick wall...")
            time.sleep(2)
            print("Nothing happens")
            time.sleep(2)
            treasure_room()

        while action_4.lower() is not ["shout", "punch"]:
            print("Please choose a valid option")
            print("What would you like to do?")
            action_4 = input("[Shout] or [Punch]\n-> ")

            if action_4.lower() == "shout":
                print("You proceed to shout in this room...")
                time.sleep(2)
                print("Nothing happens")
                time.sleep(2)
                treasure_room()

            elif action_4.lower() == "punch":
                print("You tried punching the wall...")
                time.sleep(2)
                print("Nothing happens")
                time.sleep(2)
                treasure_room()

### MOVE INPUT ###

    if task_4.lower() == "move":
        direction_3 = input("Would you like to exit this room? As there is only exit to the South [YES] or [NO]\n-> ")
        if direction_3.lower() == "yes":
            print("You choose to leave this room...")
            time.sleep(2)
            first_room()

        elif direction_3.lower() == "no":
            print("You choose to stay in this room...")
            time.sleep(2)
            treasure_room()

        else:
            print("Choose a correct option and try again...")
            time.sleep(3)
            treasure_room()

### COLLECT INPUT ###

    if task_4.lower() == "collect":
        if 100 in Coins:
            print("Chest is already open... There is nothing here to collect...")
            time.sleep(2)
            treasure_room()

        elif 100 not in Coins:
            print("There is a a chest in the middle of the room...")
            time.sleep(2)
            print("Would you want to open it?")
            time.sleep(1)
            collect = input("[Yes] or [No]\n-> ")

            if collect.lower() == "yes":
                print("You walk up to the chest and open it...")
                time.sleep(2)
                print("It contains a lot of coins, and you choose to collect them...")
                Coins.append(100)
                time.sleep(2)
                treasure_room()

            elif collect.lower() == "no":
                print("You choose to not open the chest for some reason...")
                time.sleep(2)
                treasure_room() 

            else:
                print("Choose a correct option and try again...")
                time.sleep(3)
                treasure_room()

### TITLE SCREEN ###
def title_screen():
    os.system("cls") # Used to clear the terminal (Only works for Windows)
    print('##########################')
    print('# Welcome To Mad Dungeon #')
    print('##########################')
    print('          -Play-          ')
    print('          -Quit-          ')
    print('##########################')
    title_screen_options()

def title_screen_options():
    option = input("Select one of the options and type them out\n-> ")

    if option.lower() == "play":
        first_room()

    elif option == "quit":
        print("Thank you for playing!")
        print("Your game will close in 5 seconds")
        time.sleep(5)
        SystemExit

    while option.lower() not in ["play", "quit"]:
        print("!!!!! Please enter a valid option from the list !!!!!")
        print("Select one of the options and type them out")
        time.sleep(2)
        os.system("cls") # Used to clear the terminal (Only works for Windows)
        title_screen()


        if option == "play":
            first_room()

        elif option == "quit":
            print("Thank you for playing!")
            print("Your game will close in 5 seconds")
            time.sleep(5)
            sys.exit()

title_screen()




