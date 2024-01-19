# CSC235 - Week2 - Assignment2-1 - Nicholas M James
# This is going to be a text-based simulation thta displays different output based on the user's choices

# Project Requirements:
# Needs 2 Loops
# Decision Logic - at Least 3 if/else statments
# Comment every line of code

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
    print("1: Follow the path through the pond.")
    print("2: Swim from lily pad to lily pad")
# Use an input() statement;
    
    # Setting a variable to users choice
    choice1 = input("Enter your choice (1 or 2): ")
    choice2 = print('2')
    choice3 = ''
    
    # FIRST DECISION LOGIC BLOCK OF CODE 1/3
    # if statement for choice 1
    if choice1 == '1':
        # print out message
        print("You have jumped into the pond.  You hear a splash and see ripples in the water")
        print("1: Look around for the source of the splash sound.")
        print("2: Ignore the splash sound and begin the swim towards the next lily pad")

        # Find out path user chooses
        # Use an input() statement;
        # Set variable for the choice user makes
        choice2 = input("Enter your choice (1 or 2): ")
        # SECOND DECISION LOGIC BLOCK OF CODE 2/3
        # if statement for choice 1
        if choice2 == '1':  
            # Find out path user chooses
            print("You have jumped into the pond.  You hear a splash and see ripples in the water")
            print("1: Look around for the source of the splash sound.")
            print("2: Ignore the splash sound and begin the swim towards the next lily pad")
            # Use an input() statement;
            # Set variable for the choice user makes
            choice3 =("Enter your choice (1 or 2): ")
            # THIRD DECISION LOGIC BLOCK OF CODE 3/3
            # if statement for choice 1
            if choice3 == '1':
                # print success
                print('You are successful getting to the next lily pad')
            # elif next alternative
            elif choice3 == '2':
                # print unsuccessful
                print('You are unsuccessful getting to the next lilly pad')
            # else will be the catch-all for wrong input
            else:
                print("Incorrect Choice.  Please enter a 1 or 2.")
        # elif for the next alternative
        elif choice2 == '2':
            # annoying loop - guess heads/tails to get out of the loop
            secretWord = ""
            while secretWord !="lily pad":
                secretWord = input("Guess heads or tails to continue.")
        
            print("Good job guessing")
        # else will be the catch-all for wrong input
        else:
            print("Incorrect choice.  Please enter a 1 or 2.")
        # elif for the next alternative
    elif choice1 == '2':
        # print out message communicating incorrect choice
        print("You have jumped into the pond.  You hear a splash and see ripples in the water")
        print("1: Look around for the source of the splash sound.")
        print("2: Ignore the splash sound and begin the swim towards the next lily pad")
        
        # Set variable for the choice user makes
        choice2 = input("Enter your choice (1 or 2): ")

        # if statement for 1 choice
        if choice2 == '1':
            # if the user looks around
            print("You looked around")
        elif choice2 == '2':
            # this will be an incorrect choice
            print("Incorrect choice.  Take a break and try again later please.")
        # else will be the catch-all for wrong input
        else:
            print("Incorrect choice.  Please enter a 1 or 2.")
    # else will be the catch-all for wrong input
    else:
        print("Incorrect choice. Please enter a 1 or 2.")
        
        # ask the user if they want to continue (run th sim again), if no, then break
        # while loop options:
        # * continue: go back to the beginning of the loop (if there is a counter,)
        # * break: exit out of the loop and continue running the program
        # * exit: end the program
        replay = input("Do you want to play again (yes/no)? ")

        # If the user says no, leave the game
        if replay.lower() == 'no':
            # Print a goodbye message
            print("Thanks for playing!")
            break

        def printName(userName):
            print("Welcome,", userName, "!")
            # print using f string
            print(f"Welcome, {userName}!")
            # print using string concatenation
            print("Welcome, " + userName + "!")