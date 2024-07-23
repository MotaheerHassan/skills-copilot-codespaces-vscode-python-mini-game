import random

# We need to create a basic rock, paper, scissors game. The game has the following rules:
# Rock beats scissors
# Scissors beats paper
# Paper beats rock
# The game should be a console application that takes a user input from the terminal
# and randomly selects a move for the computer. 
# User should be warned if they enter an invalid move 
# After each round, user will have option to play again or quit the game
# After user quits the game, the app should get terminated and should print the score of the user with the round information

def play_game():
    score = {'user': 0, 'computer': 0}
    choices = ['rock', 'paper', 'scissors']
    rounds_played = 0
    while True:
        rounds_played += 1
        user_choice = input("Enter your move (rock, paper, scissors): ")
        user_choice = user_choice.lower()
        computer_choice = random.choice(choices)

        if user_choice not in choices:
            print("Invalid move. Please try again.")
            continue

        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            print("You win!")
            score['user'] += 1
        else:
            print("Computer wins!")
            score['computer'] += 1

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            print(f"Final score: User - {score['user']}, Computer - {score['computer']}, Rounds Played - {rounds_played}")
            break

play_game()
