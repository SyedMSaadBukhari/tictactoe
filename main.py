from game.board import Board
from game.players import Player
from tools.display import display_welcome, display_board, announce_winner, prompt_for_restart
from tools.logger import Logger


def main():
    player1_name = input("Please enter Player 1 name: ")
    player2_name = input("Please enter Player 2 name: ")
    display_welcome(player1_name, player2_name)
    
    logger = Logger()
    
    play_again = True
    while play_again:
        board = Board()
        player1 = Player(player1_name, "X")
        player2 = Player(player2_name, "O")
        current_player = player1
        game_over = False
        move_count = 0
        
        logger.start_new_game(player1_name, player2_name, current_player.name)
        
        while not game_over:
            display_board(board.positions)
            
            position = current_player.get_move(board.get_available_moves())
            
            board.update_position(position, current_player.marker)
            
            move_count += 1
            
            logger.log_move(move_count, current_player.name, position, board.positions)
            
            if board.check_winner(current_player.marker):
                display_board(board.positions)
                announce_winner(current_player.name)
                logger.log_result(f"{current_player.name} wins!")
                game_over = True
            elif board.is_full():
                display_board(board.positions)
                print("It's a draw!")
                logger.log_result("Draw")
                game_over = True
            
            current_player = player2 if current_player == player1 else player1
        
        play_again = prompt_for_restart()
    
    print("Thanks for playing! Goodbye!")


if __name__ == "__main__":
    main()