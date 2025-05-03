import pathlib
import time

class Logger:
    
    def __init__(self):
        self.base_log_dir = pathlib.Path("game_log")
        self.base_log_dir.mkdir(parents=True, exist_ok=True)
        self.current_game_dir = None
        self.log_file = None
    
    def start_new_game(self, player1_name, player2_name, first_player_name):

        game_number = self._get_next_game_number()
        
        self.current_game_dir = self.base_log_dir / f"game{game_number}"
        self.current_game_dir.mkdir(parents=True, exist_ok=True)
        
        self.log_file = self.current_game_dir / "log.txt"
        
        with open(self.log_file, "w") as f:
            f.write(f"Game {game_number} Log\n")
            f.write("=" * 20 + "\n\n")
            f.write("Players:\n")
            f.write(f"- {player1_name} (X)\n")
            f.write(f"- {player2_name} (O)\n\n")
            f.write(f"First move: {first_player_name}\n\n")
            f.write("Moves:\n")
    
    def log_move(self, move_number, player_name, position, board_positions):
        
        if self.log_file is None:
            return
        
        with open(self.log_file, "a") as f:
            f.write(f"Move {move_number}: {player_name} -> Position {position}\n")
            
            # Log board state after this move
            if move_number % 3 == 0:  # Log board state every 3 moves to keep log readable
                f.write("Board After Move {}:\n".format(move_number))
                f.write(f" {board_positions[0]} | {board_positions[1]} | {board_positions[2]} \n")
                f.write("-----------\n")
                f.write(f" {board_positions[3]} | {board_positions[4]} | {board_positions[5]} \n")
                f.write("-----------\n")
                f.write(f" {board_positions[6]} | {board_positions[7]} | {board_positions[8]} \n\n")
    
    def log_result(self, result):
        
        if self.log_file is None:
            return
        
        with open(self.log_file, "a") as f:
            f.write(f"\nResult: {result}\n")
            f.write(f"Game ended at: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    def _get_next_game_number(self):
        
        existing_games = [d for d in self.base_log_dir.iterdir() if d.is_dir() and d.name.startswith("game")]
        
        if not existing_games:
            return 1
        
        game_numbers = []
        for game_dir in existing_games:
            try:
                game_number = int(game_dir.name[4:])  
                game_numbers.append(game_number)
            except ValueError:
                continue
        
        return max(game_numbers, default=0) + 1