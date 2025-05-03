def clean_input(input_string):
    return input_string.strip()

def validate_move(position, available_moves):
    try:
        position = clean_input(position)
        
        if not position or not position.isdigit():
            return False
        
        return position in available_moves
    except Exception:
        return False

def generate_available_moves(positions):
    for position in positions:
        if position not in ['X', 'O']:
            yield position