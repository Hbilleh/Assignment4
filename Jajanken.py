import random

def get_user_choice():
    """Get user's choice and validate it."""
    choices = ['rock', 'paper', 'scissors']
    choice = input("Enter Rock, Paper, or Scissors: ").lower()
    print("User Choice:", choice)
    if choice in choices:
        return choice
    else:
        print("Invalid choice. Please try again.")
        return get_user_choice()

def get_computer_choice():
    """Randomly select computer's choice."""
    print("Jajanken...")
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    print("Computer Choice:", computer_choice)
    return computer_choice

def determine_winner(user_choice, computer_choice):
    """Determine the winner of a round."""
    print(f"Choices: User - {user_choice}, Computer - {computer_choice}")  # Debug print
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") \
         or (user_choice == "scissors" and computer_choice == "paper") \
         or (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def play_round():
    """Play a single round of Rock, Paper, Scissors."""
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"Computer chose {computer_choice}.")
    result = determine_winner(user_choice, computer_choice)
    print("Round Result:", result)
    return result

# Main game function
def play_game():
    """Play a best-of-three game of Rock, Paper, Scissors."""
    user_score, computer_score = 0, 0
    rounds = 3

    for _ in range(rounds):
        result = play_round()
        print(result)
        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        print(f"Current Score: User - {user_score}, Computer - {computer_score}")

        if user_score == 2 or computer_score == 2:
            break

    if user_score > computer_score:
        print(f"You won the game {user_score} to {computer_score}!")
    elif computer_score > user_score:
        print(f"Computer won the game {computer_score} to {user_score}!")
    else:
        print(f"The game is a tie at {user_score} each!")

# Run the game
play_game()
