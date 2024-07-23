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

def determine_winner(user_choice, computer_choice):
    """
    Determines the winner of a rock-paper-scissors game round.
    Returns 'user' if the user wins, 'computer' if the computer wins, and 'tie' for a tie.
    """
    winning_combinations = {
        'rock': 'scissors',
        'scissors': 'paper',
        'paper': 'rock'
    }
    if user_choice == computer_choice:
        return 'tie'
    elif winning_combinations[user_choice] == computer_choice:
        return 'user'
    else:
        return 'computer'

def get_user_choice(choices):
    """
    Gets the user's choice from the terminal.
    """
    user_choice = input("Enter your move (rock, paper, scissors): ").lower()
    while user_choice not in choices:
        print("Invalid move. Please try again.")
        user_choice = input("Enter your move (rock, paper, scissors): ").lower()
    return user_choice

def get_computer_choice(choices):
    """
    Randomly selects the computer's choice.
    """
    return random.choice(choices)

def display_round_result(winner, user_choice, computer_choice):
    """
    Displays the result of a single round.
    """
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if winner == 'tie':
        print("It's a tie!")
    elif winner == 'user':
        print("You win!")
    else:
        print("Computer wins!")

def display_final_score(score, rounds_played):
    """
    Displays the final score after the game ends.
    """
    print(f"Final score: User - {score['user']}, Computer - {score['computer']}, Rounds Played - {rounds_played}")

def play_game():
    """
    Main function to play the rock-paper-scissors game.
    Refactored for better unit testability.
    """
    score = {'user': 0, 'computer': 0}
    choices = ['rock', 'paper', 'scissors']
    rounds_played = 0

    while True:
        user_choice = get_user_choice(choices)
        computer_choice = get_computer_choice(choices)

        winner = determine_winner(user_choice, computer_choice)
        rounds_played += 1

        display_round_result(winner, user_choice, computer_choice)

        if winner == 'user':
            score['user'] += 1
        elif winner == 'computer':
            score['computer'] += 1

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            display_final_score(score, rounds_played)
            break

if __name__ == '__main__':
    play_game()
