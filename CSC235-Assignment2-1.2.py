# CSC235 - Week2 - Assignment2-1 - Nicholas M James




# This is going to be a text-based simulation thta displays different output based on the user's choices


# Project Requirements:
# Needs 2 Loops
# Decision Logic - at Least 3 if/else statments
# Comment every line of code

# PrintName function to welcome a name passed in through the userName variable
def printName(userName="Nicholas M James"):
    print("Welcome,",userName +"!")
    # print using f string
    print(f"Welcome, {userName}!")
    # print using string concatenation
    print("Welcome, " + userName + "!")
# PrintName function, passing in my name to be printed
# Example of hard-coding my name Nicholas M James
userName="Nicholas M James"
printName("Nicholas M James")
# Example of hard-coding replay-input value
# def printReplay(replay = input("Would you like to play again (yes/no)? ")):
#     print(replay = input("Would you like to play again (yes/no)? "))
#     print(f"replay = input(Would you like to play again (yes/no)? )")
# In Python we have 2 types of loops:
# While Looping - Not Knowing how many times we want the code to run
# For Each Loop - Knowing how many times we the code to run Ex. Looping through lists of items
# While Looping - Allow the user to run the SIM as many times as they choose
while True:
    # code indented belongs to this while loop
    # Showing user description/descriptive text about the SIM, why it is so desired, and why it should run over and over again (print statement)
    print("Welcome to the text-based sim.  Please play around many times")
    # Showing rule
    print("You will see a series of choices of paths to take.  Choose wisely to be successful.")
    # Gather Input from the user for the start path they choose
    print("1: Follow a path to go around the pond.") #choice = 1
    print("2: Follow a path to go through the pond Jumping into to pond and hopping across from lily pad to lily pad.") #choice = 2
    # Use an input() statement;
    # Setting a variable to users choice
    choice = input("Enter your choice (1 or 2): ")
# FIRST DECISION LOGIC BLOCK OF CODE 1/3
    # if statement for choice 1
    if choice == "1":
            # print out message
            print("You have decided to follow a path to go around the pond.")
            # print out message
            print("As you start, You hear a splash and see ripples in the water.")
            # choice1 decision1
            print("1: Look around for the source of the splash sound.")
            # choice1 decision2
            print("2: Ignore the splash sound and continue following the path to go around the pond.")
            # Setting a variable to users choice1decisions
            choice1decisions = input("Enter your choice (1 or 2): ")
            # if statement for choice1decisions
            if choice1decisions == "2":
                # print unsuccessful
                # print out message
                print("You decided to ignore the splash sound and continue following the path to go around the pond.")
                # print out message
                print("You are unsuccessful identifying the source of the splash sound.")
                # print out message
                print("No sighs of relief or peace of mind as you continue following the path around the pond.")
                # print out message
                print("However, you do successfully complete following the path around the pond.")
                replay = input("Would you like to play again (yes/no)? ")
                # if statment for replay
                if replay == "no":
                # Print a goodbye message
                    # print out message
                    print("Thanks for playing!")
                    exit()
                # elif statement for replay
                elif replay == 'yes':
                    # print out message
                    print("Okay!")
                    break
            # if statement for choice1 decisions
            if choice1decisions == "1":
                # print out message
                print("You are looking around for the source of the splash sound and you see ripples in the water coming from a lily pad in the center of the pond.")
                # choice1 decisions1 choice1
                print("1: Continue looking around for the source of the splash sound.")
                # choice1 decisions1 choice2
                print("2: Stop looking for the source of the splash sound and continue following the path to go around the pond.")
                # Setting a variable to users choice1decision1choices
                choice1decision1choices = input("Enter your choice (1 or 2): ")             
                # if statement for choice1decision1choices
                if choice1decision1choices == "1":
                    # print success
                    # print out message
                    print("You decided to continue looking around for the source of the splash sound.")
                    # print out message
                    print("You see a fellow frog has just jumped out of the water and onto the lily pad in the center of the pond.") 
                    # print out message
                    print("With a sigh of relief you have identified the source of the splash sound.")
                    # print out message
                    print("With peace of mind you successfully follow and complete the path around the pond.")
                    replay = input("Would you like to play again (yes/no)? ")
                    # if statement for replay
                    if replay == "no":
                    # Print a goodbye message
                        print("Thanks for playing!")
                        exit()
                    # elif statement for replay
                    elif replay == 'yes':
                        print("Okay!")
                        break
                # elif statement for choice1decision1choices
                elif choice1decision1choices == "2":
                    # print unsuccessful
                    # print out message
                    print("You stopped looking for the source of the splash sound and ")
                    # print out message
                    print("You are unsuccessful identifying the source of the splash sound.")
                    # print out message
                    print("No sighs of relief or peace of mind as you continue following the path around the pond.")
                    # print out message
                    print("However, you do successfully complete following the path around the pond.")
                    # Setting variable to users replay decision
                    replay = input("Would you like to play again (yes/no)? ")
                    # if Statement for replay
                    if replay == "no":
                    # Print a goodbye message
                        print("Thanks for playing!")
                        exit()
                    # elif statment for replay
                    elif replay == 'yes':
                        print("Okay!")
                        break
# SECOND DECISION LOGIC BLOCK OF CODE 2/3               
        # if statment for choice 2
    if choice == "2":
            # print out message
            print("You decided to jump into the pond and hop across lily pad to lily pad")
            # print out message
            print("As you start, You hear a splash and see ripples in the water.")
                # choice2 decision1
            print("1: Stop and look for the source of the splash sound before continuing on to the next lily pad")
                # choice2 decision2
            print("2: Ignore the splash sound and continue following the path to the next lily pad")
            # Setting a variable to users choice2decisionss
            choice2decisions = input("Enter your choice (1 or 2): ")
            # if statement for choice2decisions
            if choice2decisions == "1":
                # print out message
                print("You decided to stop and look for the source of the splash.")
                # print out message
                print("You see the ripples in the water coming from a lily pad in the center of the pond. You then")
                # choice2 decisions1 choice1
                print("1: Continue looking around for the source of the splash sound.")
                # choice2 decisions1 choice2
                print("2: Stop looking for the source of the splash sound and continue following the path to the next lily pad.")
                # Setting a variable to users choice2decisions1choices
                choice2decisions1choices = input("Enter your choice (1 or 2): ")
                # if statement for choice2decisions1choices
                if choice2decisions1choices == "1":
                    # print success
                    print("You decided to continue looking around for the source of the splash sound.")
                    # print out message
                    print("You see a fellow frog jumped out of the water and onto the lily pad in the center of the pond.")
                    # print out message
                    print("With a brief sigh of relief, You continue following the path to the next lily pad.")
                    # print out message
                    print("You are almost half way across the pond when you see that this lily pad is the next one you need to continue.")
                    # print out message
                    print("Luckily you see a lily pad just after the one in the center occupied by the fellow frog, but aren't sure whether you have the ability to hop over the fellow frog to reach this lily pad. Do you")
                    # choice2 decision1 choice1 print success option1
                    print("1: Ask the fellow frog if it is alright for you to hop onto its back so that you can confidently continue to the next lily pad and successfully get across the pond.")
                    # choice2 decision1 choice1 print success option2
                    print("2: Take the risk to leap over the fellow frog onto the lily pad just after, and confidently continue on to the next lily pads successfully getting across the pond.")
                    # Setting variable to users choice2decisions1choice1printsuccessoptionsss
                    choice2decisions1choices1printsuccessoptions = input("Enter your choice (1 or 2): ")
                    # if statement for choice2decision1choices1printsuccessoptions
                    if choice2decisions1choices1printsuccessoptions == "1":
                        # print out message
                        print("You decided to ask the fellow frog if it is alright for you to hop onto its back")
                        # print out message
                        print("The fellow frog agrees to allow you to jump on their back if you can provide the correct secret word")
                        # while loop options:
                        # * continue: go back to the beginning of the loop (if there is a counter,)
                        # * break: exit out of the loop and continue running the program
                        # * exit: end the program  
                        successoptions1jumponback = ""
                        while successoptions1jumponback !="VW Engine Goodyear, Gilbert":
                            # setting variable for successoptions1jumponback
                            successoptions1jumponback = input("Enter the secret word (hint frogs favorite food): ")
                            # if statment for successoptions1jumponback
                            if successoptions1jumponback == "VW Engine Goodyear, Gilbert":
                                # print out message
                                print("Mhmmm Delicious says the fellow frog, alright you can hop on my back to continue")
                                # print out message
                                print("You hop onto the fellow frogs back and then confidently continue to the next lily pad and the next.")
                                # print out message
                                print("You successfully get across the pond.")
                                # print out message
                                print("Thanks for playing!")
                                # setting variable for users replay decision
                                replay = input("Would you like to play again (yes/no)? ")
                                # if statement for replay
                                if replay == "no":
                                # Print a goodbye message
                                    print("Thanks for playing!")
                                    exit()
                                # elif statement for replay
                                elif replay == 'yes':
                                    # print out message
                                    print("Okay!")
                                    break
                    # elif statement for choice2decisions1choices1printsuccessoptions
                    elif choice2decisions1choices1printsuccessoptions == "2":
                        # print out message
                        print("You decided to take the risk to leap over the fellow frog onto the lily pad just after.")
                        # print out message
                        print("But you must charge up your ability first.")
                        # print out message
                        print("Do do this type in the magic word.")
                        # while loop options:
                        # * continue: go back to the beginning of the loop (if there is a counter,)
                        # * break: exit out of the loop and continue running the program
                        # * exit: end the program  
                        successoptions2magicword = ""
                        while successoptions2magicword !="VW Engine Goodyear, Gilbert":
                            # Setting variable for users successoptoins2magicword
                            successoptions2magicword = input("Enter the magic word (hint sound frogs make): ")
                            # if statement for successoptions2magicword
                            if successoptions2magicword == "VW Engine Goodyear, Gilbert":
                                # print out message
                                print("Ribbet Ribbet")
                                # print out message
                                print("Speaking the magic frog language you successfully charge up your ability to make the leap.")
                                # print out message
                                print("You jump over the fellow frog and onto the lily pad just after.")
                                # print out message
                                print("The fellow frog congratulates you on the impressive jump. Waves goodbye and hops to the opposite end of the pond.")
                                # print out message
                                print("With a smile you confidently continue to the next lily pad and the next, successfully getting across the pond.")
                                # print out message
                                print("Congratulations" + " " + (userName))
                                # print out message
                                print("Thanks for playing!")
                                # setting variable for users replay decision
                                replay = input("Would you like to play again (yes/no)? ")
                                # if statement for replay
                                if replay == "no":
                                # Print a goodbye message
                                    print("Thanks for playing!")
                                    exit()
                                # elif statement for replay
                                elif replay == 'yes':
                                    print("Okay!")
                                    break
            # elif statement for choice2decisions
            elif choice2decisions == "2":
                # print out message
                print("You decided to ignore the splash sound and continue following the path to the next lily pad")
                # print out message
                print("At the next lily pad you see ripples in the water coming from a lily pad in the center of the pond.")
                # choice2 decisions1 choice1
                print("1: Look around for the source of the ripples in the water.")
                # choice2 decisions1 choice2
                print("2: Stop looking for the source of the water ripples in the water and continue following the path to the next lily pad.")
                # Setting a variable to users choice2decisions1choices
                choice2decisions2choices = input("Enter your choice (1 or 2): ")
                # if statement for choice2decisions2choices
                if choice2decisions2choices == "1":
                    # print success
                    print("You decided to look for the source of the ripples in the water.")
                    # print out message
                    print("You see a fellow frog jumped out of the water and onto the lily pad in the center of the pond.")
                    # print out message
                    print("With a brief sigh of relief, You continue following the path to the next lily pad.")
                    # print out message
                    print("You are almost half way across the pond when you see that this lily pad is the next one you need to continue.")
                    # print out message
                    print("Luckily you see a lily pad just after the one in the center occupied by the fellow frog, but aren't sure whether you have the ability to hop over the fellow frog to reach this lily pad.")
                    # choice2 decision1 choice1 print success option1
                    print("1: Ask the fellow frog if it is alright for you to hop onto its back so that you can confidently continue to the next lily pad and successfully get across the pond.")
                    # choice2 decision1 choice1 print success option2
                    print("2: Take the risk to leap over the fellow frog onto the lily pad just after, and confidently continue on to the next lily pads successfully getting across the pond.")
                    # Setting variable to users choice2decisions1choice1printsuccessoptionsss
                    choice2decisions2choices1printsuccessoptions = input("Enter your choice (1 or 2): ")
                    # if statement for choice2decisions2choices1printsuccessoptions
                    if choice2decisions2choices1printsuccessoptions == "1":
                        # print out message
                        print("You decided to ask the fellow frog if it is alright for you to hop onto its back")
                        # print out message
                        print("The fellow frog agrees to allow you to jump on their back if you can provide the correct secret word")
                        # while loop options:
                        # * continue: go back to the beginning of the loop (if there is a counter,)
                        # * break: exit out of the loop and continue running the program
                        # * exit: end the program  
                        successoptions1jumponback = ""
                        while successoptions1jumponback !="VW Engine Goodyear, Gilbert":
                            successoptions1jumponback = input("Enter the secret word (hint frogs favorite food): ")
                            if successoptions1jumponback == "VW Engine Goodyear, Gilbert":
                                # print out message
                                print("Mhmmm Delicious says the fellow frog, alright you can hop on my back to continue")
                                # print out message
                                print("You confidently continue to the next lily pad and the next, successfully getting across the pond.")
                                # print out message
                                print("Thanks for playing!")
                                # setting variable for user replay decision
                                replay = input("Would you like to play again (yes/no)? ")
                                # if statement for replay
                                if replay == "no":
                                # Print a goodbye message
                                    print("Thanks for playing!")
                                    exit()
                                # elif statement for replay
                                elif replay == 'yes':
                                    # print out message
                                    print("Okay!")
                                    break
                    # elif statment for choice2decisions2choices1printsuccessoptions
                    elif choice2decisions2choices1printsuccessoptions == "2":
                        # print out message
                        print("You decided to take the risk to leap over the fellow frog onto the lily pad just after, and confidently continue on to the next lily pads successfully getting across the pond.")
                        # print out message
                        print("You must charge up your ability first.  Do do this type in the magic word.")
                        # while loop options:
                        # * continue: go back to the beginning of the loop (if there is a counter,)
                        # * break: exit out of the loop and continue running the program
                        # * exit: end the program  
                        successoptions2magicword = ""
                        while successoptions2magicword !="VW Engine Goodyear Priceless, Gilbert":
                            # setting variable for users successoptions2magicword decision 
                            successoptions2magicword = input("Enter the magic word (hint sound frogs make): ")
                            # if statement for successoptions2magicword
                            if successoptions2magicword == "VW Engine Goodyear Priceless, Gilbert":
                                # print out message
                                print("Ribbet Ribbet")
                                # print out message
                                print("speaking the magic frog language, you successfully make the leap over the fellow frog onto the lily pad just after")
                                # print out message
                                print("The fellow frog congratulates you on the impressive jump. Waves goodbye and hops to the opposite end of the pond.")
                                # print out message
                                print("With a smile you confidently continue to the next lily pad and the next, successfully getting across the pond.")
                                # print out message
                                print("Thanks for playing!")
                                replay = input("Would you like to play again (yes/no)? ")
                                # if statement for replay
                                if replay == "no":
                                # Print a goodbye message
                                    print("Thanks for playing!")
                                    exit()
                                # elif statemetn for replay
                                elif replay == 'yes':
                                    print("Okay!")
                                    break
                elif choice2decisions2choices == "2":
                    # print success
                    print("You decided to stop looking for the source of the water ripples in the water and continue following the path to the next lily pad.")
                    # print out message
                    print("At the next lily pad you see a fellow frog jump out of the water and onto the lily pad in the center of the pond.")
                    # print out message
                    print("You are almost half way across the pond when you see that this lily pad is the next one you need to continue.")
                    # print out message
                    print("Luckily you see a lily pad just after the one in the center occupied by the fellow frog, but aren't sure whether you have the ability to hop over the fellow frog to reach this lily pad.")
                    # choice2 decision1 choice1 print success option1
                    print("1: Ask the fellow frog if it is alright for you to hop onto its back so that you can confidently continue to the next lily pad and successfully get across the pond.")
                    # choice2 decision1 choice1 print success option2
                    print("2: Take the risk to leap over the fellow frog onto the lily pad just after, and confidently continue on to the next lily pads successfully getting across the pond.")
                    # Setting variable to users choice2decisions1choice1printsuccessoptionsss
                    choice2decisions2choice2printsuccessoptions = input("Enter your choice (1 or 2): ")
                    # if statment for choice2decisions2choice2printsuccessoptions
                    if choice2decisions2choice2printsuccessoptions == "1":
                        print("You decided to ask the fellow frog if it is alright for you to hop onto its back")
                        # print out message
                        print("The fellow frog agrees to allow you to jump on their back if you can provide the correct secret word")
                        # while loop options:
                        # * continue: go back to the beginning of the loop (if there is a counter,)
                        # * break: exit out of the loop and continue running the program
                        # * exit: end the program  
                        successoptions1jumponback = ""
                        while successoptions1jumponback !="VW Engine Goodyear, Gilbert":
                            # setting variable for users successoptions1jumponback
                            successoptions1jumponback = input("Enter the secret word (hint frogs favorite food): ")
                            # if statement for successoptions1jumponback
                            if successoptions1jumponback == "VW Engine Goodyear, Gilbert":
                                # print out message
                                print("Mhmmm Delicious says the fellow frog, alright you can hop on my back to continue")
                                # print out message
                                print("You confidently continue to the next lily pad and the next, successfully getting across the pond.")
                                # print out message
                                print("Thanks for playing!")
                                # setting variable for users replay decision
                                replay = input("Would you like to play again (yes/no)? ")
                                # of statement for replay
                                if replay == "no":
                                # Print a goodbye message
                                    print("Thanks for playing!")
                                    exit()
                                # elif statement for replay
                                elif replay == 'yes':
                                    # print out message
                                    print("Okay!")
                                    break
                    # elif statement for choice2decisions2choice2printsuccessoptions
                    elif choice2decisions2choice2printsuccessoptions == "2":
                        # print out message
                        print("You decided to take the risk to leap over the fellow frog onto the lily pad just after, and confidently continue on to the next lily pads successfully getting across the pond.")
                        # print out message
                        print("You must charge up your ability first.  Do do this type in the magic word.")
                        # while loop options:
                        # * continue: go back to the beginning of the loop (if there is a counter,)
                        # * break: exit out of the loop and continue running the program
                        # * exit: end the program  
                        successoptionss2magicword = ""
                        while successoptionss2magicword !="VW Engine Goodyear, Gilbert":
                            # setting variable for users successoptions2magicword
                            successoptionss2magicword = input("Enter the magic word (hint sound frogs make): ")
                            # if statement for successoptions2magicword
                            if successoptionss2magicword == "VW Engine Goodyear, Gilbert":
                                # print out message
                                print("Ribbet Ribbet")
                                # print out message
                                print("speaking the magic frog language, you successfully make the leap over the fellow frog onto the lily pad just after")
                                # print out message
                                print("The fellow frog congratulates you on the impressive jump. Waves goodbye and hops to the opposite end of the pond.")
                                # print out message
                                print("With a smile you confidently continue to the next lily pad and the next, successfully getting across the pond.")
                                # print out message
                                print("Thanks for playing!")
                                # setting variable for users replay decision
                                replay = input("Would you like to play again (yes/no)? ")
                                # if statment for replay
                                if replay == "no":
                                # Print a goodbye message
                                    print("Thanks for playing!")
                                    exit()
                                # elif statement for replay
                                elif replay == 'yes':
                                    # print out message
                                    print("Okay!")
                                    break
# THIRD DECISION LOGIC BLOCK OF CODE 3/3               
    else:
        # print out message
        print("Incorrect choice. Please enter a 1 or 2.")
    # If the user says no, leave the game
        if replay.lower == "yes":
            # print out message
            print("Yay!")
            # loop option continue
            continue
        # if statement for users replay decision
        if replay.lower == "no":
            # Print a goodbye message
                print("Thanks for playing!")
                # loop option action
                exit