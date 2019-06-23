# DiceRollingSim.py
""" Simulate the rolling of dice and play small simple games with them."""
import random

endState = 1

def dice_roll():
    """Roll a dice and receive a number between 1 and 6"""
    roll1 = random.randrange(1, 7)
    return(roll1)

def roll_for_me():
    playerResults = dice_roll()
    opponentResults = dice_roll()
    print(f"Your roll is: {playerResults}")
    print(f"Your Opponents roll is: {opponentResults}")
    return(playerResults, opponentResults)    

# So long as the endstate doesnt reach -1 the games will continue
while endState != -1:

    if endState == 1:
        print("")
        # have player choose an option from the list
        print("Please choose an option...")
        print("Option 1: Greater than")
        print("Option 2: Less than")
        print("Option 3: equal too")
        print("Option 4: get above 10")
        print("Option 5: quit game")
        optionChoice = input('--->')
        print("")

    # Greater Than Option
    if int(optionChoice) == 1:
        endState = 2
        print("you've selected option 1")
        (diceResultsPlayer, diceResultsOpponent) = roll_for_me()
        if diceResultsPlayer > diceResultsOpponent:
            print("Congratulations! your opponent rolled a lower number than you.")
        elif diceResultsPlayer == diceResultsOpponent:
            print("Sorry, you both rolled the same number. You lost.")
        else:
            print("Sorry, your opponent rolled a higher number. You lost.")
        endState = 1

    # Less than Option
    elif int(optionChoice) == 2:
        endState = 2
        print("you've selected option 2")
        (diceResultsPlayer, diceResultsOpponent) = roll_for_me()
        if diceResultsPlayer < diceResultsOpponent:
            print("Congratulations! your opponent rolled a higher number than you.")
        elif diceResultsPlayer == diceResultsOpponent:
            print("Sorry, you both rolled the same number. You lost.")
        else:
            print("Sorry, your opponent rolled a lower number. You lost.")
        endState = 1

    # Equal Too Option
    elif int(optionChoice) == 3:
        endState = 2
        print("You've selected option 3")
        (diceResultsPlayer, diceResultsOpponent) = roll_for_me()
        if diceResultsPlayer == diceResultsOpponent:
            print("Congratulations! your opponent rolled the same number as you.")
        elif diceResultsPlayer < diceResultsOpponent:
            print("Sorry, your opponent rolled a higher number. You lost.")
        else:
            print("Sorry, your opponent rolled a lower number. You lost.")
        endState = 1

    # Above 10 Option
    elif int(optionChoice) == 4:
        endState = 2
        print("You've selected option 4")
        (diceResultsPlayer, diceResultsOpponent) = roll_for_me()
        print(f"The sum of your rolls is: {diceResultsPlayer + diceResultsOpponent}")
        diceSum = diceResultsPlayer + diceResultsOpponent
        if diceSum > 10:
            print("Congratulations! the sum of both your roll and your opponent's roll is above 10.")
        else:
            print("Sorry, your roll and your opponent's roll are too low.")
        endState = 1

    # Quit Game Option
    elif int(optionChoice) == 5:
        print("Quitting game, Thanks for Playing!")
        break

    # Unexpected Input
    else:
        endState = 2
        print("Input not recognized as possible option. Please choose a different option...")
        endState = 1


