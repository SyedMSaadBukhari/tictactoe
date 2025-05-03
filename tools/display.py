def display_welcome(player1_name, player2_name):
    print(f"\nWelcome, {player1_name} and {player2_name}!")
    print("Get ready to play Tic-Tac-Toe!\n")


def display_board(positions):
    print("\nCurrent Board:")
    print(f" {positions[0]} | {positions[1]} | {positions[2]} ")
    print("-----------")
    print(f" {positions[3]} | {positions[4]} | {positions[5]} ")
    print("-----------")
    print(f" {positions[6]} | {positions[7]} | {positions[8]} ")
    print()


def announce_winner(winner_name):
    print(f"Congratulations, {winner_name}! You win!")


def prompt_for_restart():
    
    while True:
        response = input("Would you like to play again? (yes/no): ").lower().strip()
        if response in ['yes', 'y']:
            return True
        elif response in ['no', 'n']:
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")