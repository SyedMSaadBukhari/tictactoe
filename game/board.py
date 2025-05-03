from game.utils import generate_available_moves

class Board:
    
    def __init__(self):
        self.positions = [str(i) for i in range(1, 10)]
    
    def update_position(self, position, marker):
 
        index = int(position) - 1
        self.positions[index] = marker
    
    def is_position_available(self, position):
       
        try:
            index = int(position) - 1
            return self.positions[index] not in ['X', 'O']
        except (ValueError, IndexError):
            return False
    
    def get_available_moves(self):
        return generate_available_moves(self.positions)
    
    def is_full(self):
        return all(pos in ['X', 'O'] for pos in self.positions)
    
    def check_winner(self, marker):

        win_combinations = [
            # Rows
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            # Columns
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            # Diagonals
            [0, 4, 8], [2, 4, 6]
        ]
        
        for combo in win_combinations:
            if all(self.positions[i] == marker for i in combo):
                return True
        
        return False