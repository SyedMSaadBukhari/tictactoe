import random
from game.utils import validate_move

class Player:
    
    def __init__(self, name, marker):
        
        self.name = name
        self.marker = marker
        self.is_computer = name.lower() == "computer"
    
    def get_move(self, available_moves):
        
        moves_list = list(available_moves)
        
        if self.is_computer:
            return self._get_computer_move(moves_list)
        else:
            return self._get_human_move(moves_list)
    
    def _get_human_move(self, available_moves):
        
        while True:
            position = input(f"{self.name}'s Turn ({self.marker}):\nEnter a position (1-9): ")
            
            if validate_move(position, available_moves):
                return position
            
            print("Invalid move! Please choose from available positions.")
    
    def _get_computer_move(self, available_moves):
        
        position = random.choice(available_moves)
        print(f"{self.name}'s Turn ({self.marker}):\nSelected position: {position}")
        return position