import random

rock_paper_scissor = ["ROCK", "PAPER", "SCISSOR"]

scoreGame = 0
scorePlayer = 0

while(True):
    # 13th line checks if the user inputted with upper cases and if it is not, it makes its all letters upper. I did it for "draw" condition to work.
    # Note: It actually affects how all program is running.
    # You can actually do this with randint as well. But in that case, you should also check for spelling in a different way. I did this in this way because I wanted my program to be able to run regardless of user inputs.
    gameChoice = random.choice(rock_paper_scissor)
    playerChoice = str(input("\nRock, Paper, Scissor? "))
    if(playerChoice.isupper() == False):
        # this empty strip function removes any white spaces from end and start of the string.
        # With that, user can input "   paper" or "paper  " and program will still accept it. Otherwise, because of white spaces, it will ask the user to re-enter the value.
        playerChoice = playerChoice.upper().strip()

    # this section checks if user inputs anything that rock, paper, scissor. If user enters something different like "rocka", it will ask the user to re-enter the value.
    if(playerChoice != "ROCK" and playerChoice != "PAPER" and playerChoice != "SCISSOR"):
        print("please enter a valid value.")
        continue

        # This section contains main mechanic.
    if(playerChoice == "ROCK" and gameChoice == "SCISSOR"):
        print("You won! the choice was", gameChoice, "\n")
        scorePlayer = scorePlayer + 1
    elif(playerChoice == "PAPER" and gameChoice == "ROCK"):
        print("You won! the choice was", gameChoice, "\n")
        scorePlayer = scorePlayer + 1
    elif(playerChoice == "SCISSOR" and gameChoice == "PAPER"):
        print("You won! the choice was", gameChoice, "\n")
        scorePlayer = scorePlayer + 1
    elif(playerChoice == gameChoice):
        print("draw!")
    else:
        print("You lose, the choice was", gameChoice, "\n")
        scoreGame = scoreGame + 1
    # This section contains main mechanic.

    print("Player:", scorePlayer, "Program:", scoreGame)

    if(scoreGame == 3 or scorePlayer == 3):
        break

if(scorePlayer > scoreGame):
    print("\nCongratulations! you won with", scorePlayer, "to", scoreGame)
else:
    print("\nSorry, you lose with", scorePlayer, "to", scoreGame)
