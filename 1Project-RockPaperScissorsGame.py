# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 17:41:42 2023

@author: johnk
"""
"""
You now have 2/3 of the program Rock, Paper, Scissors completed. It is now time to apply what you have learned over the last two modules. 

As a recap, your program should already:

1.  Use a dictionary to display the characteristics of the rock paper and scissors.
2.  Contains a tuple to verify the user has entered a correct choice. This tuple will also be used to generate the computer's choice
3.  Uses a loop to request  input of rock paper scissors if the person enters in something other than the three available choices. 

For example we ask a user for input of rock, paper or scissor and a person types in "pebble" , our program should let the user know an incorrect choice was made, present the three possible choices and asks the user to enter one of the three choices.



Now let's apply what we learned to the complete the program

1.  Create a function to pick the computer's choice of rock , paper or scissor. Use the Tuple defined in the program as the valid selection of choices
2.  Create a function to declare a winner, either the computer wins, the player wins or it is a tie. The function should use the random module to choose rock , paper or scissor for the computer

Print out to the screen:

1.  who the winner is
2.  The computer and the player's choices
3.  The characteristic of the winner's choice as to explain why the winner won

"""
""" Expected Output - a player chooses rock and the computer randomly chooses paper

Please choose: Rock, Paper or Scissors: rock
The winner is the computer
The player chose rock and the computer chose paper
The paper is able to wrap the rock up, but is easily cut by the scissor

"""

import random

print("--------------------------")
print("Welcome to Rock Paper and Scissors Game")
print()


def comp_choice():
    tpl = ("rock", "paper", "scissor")
    choice = random. choice(tpl)
    return choice


def win(c_player, c_computer):
    if c_player == "rock" and c_computer == "paper":
        return dict[c_computer], "computer"
    elif c_player == "rock" and c_computer == "scissor":
        return dict[c_player], "player"

    elif c_player == "paper" and c_computer == "scissor":
        return dict[c_computer], "computer"
    elif c_player == "paper" and c_computer == "rock":
        return dict[c_player], "player"

    elif c_player == "scissor" and c_computer == "rock":
        return dict[c_computer], "computer"
    elif c_player == "scissor" and c_computer == "paper":
        return dict[c_player], "player"
    else:
        return "tie"


dict = {"rock": "The rock is able to break the scissors, but can be defeated by the paper",
        "paper": "The paper is able to wrap the rock up, bit is easilt cut by the scissor",
        "scissor": "The scissor can cut the paper, but is smashed by the rock"}

tpl = ("rock", "paper", "scissor")
answer = "Bad"

while answer != "Good":

    c_player = input("Please choose: Rock, Paper or Scissors: ")
    c_computer = comp_choice()

    if c_player.lower() in tpl:
        answer = "Good"
        if win(c_player, c_computer) == "tie":
            print("There is no winner")
            print(f"The player chose {c_player} and the computer chose {c_computer}")
            print("The result is a tie")
            print("--------------------------")
        else:
            print(f"The winner is the {win(c_player, c_computer)[1]}")
            print(f"The player chose {c_player} and the computer chose {c_computer}")
            print(win(c_player, c_computer)[0])
            print("--------------------------")

    else:
        answer = "Bad"
        print("Your input was incorrect. It must be between the choices of rock, paper, or scissors.")
        print()
