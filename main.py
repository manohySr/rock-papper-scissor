import random

def make_choice():
    player_choice = input("Make your choice (rock, papper or scissor) !? : ")
    option = ["rock", "papper", "scissor"]
    computer_choice = random.choice(option)
    return {"player_choice": player_choice, "computer_choice": computer_choice}

def who_win(player_choice, computer_choice):
    print(f"You choose {player_choice}, and computer choice was {computer_choice}")
    if (player_choice == computer_choice):
        return "It's a tie :-*"
    elif (player_choice == "rock"):
        if (computer_choice == "papper"):
            return "You lose, the papper covers the rock :("
        else:
            return "You win :)"
    elif (player_choice == "papper"):
        if (computer_choice == "scissor"):
            return "You lose, the scissor cuts the papper :("
        else:
            return "You win :)"
    elif (player_choice == "scissor"):
        if (computer_choice == "rock"):
            return "You lose, the rock smatches the scissor :("
        else:
            return "You win :)"

choice = make_choice()
winner = who_win(choice["player_choice"], choice["computer_choice"])
print(winner)