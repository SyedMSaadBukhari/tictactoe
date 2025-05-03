A structured, modular Python implementation of the classic Tic-Tac-Toe game that runs in the command line interface.

## Project Overview

This project implements a command-line Tic-Tac-Toe game using object-oriented programming principles. The game features a structured modular design, demonstrating concepts such as:

- Classes and object-oriented design
- Generators for dynamic available moves
- Directory management with pathlib
- Modular code organization
- Logging game history to text files

## Project Structure

```
tictactoe/
├── main.py              # Main game loop and entry point
├── README.md            # This file
├── game/
│   ├── __init__.py      # Package marker
│   ├── board.py         # Board class and game state management
│   ├── players.py       # Player class for both human and computer players
│   └── utils.py         # Utility functions and generators
└── tools/
    ├── display.py       # UI display functions
    └── logger.py        # Game logging system
```

## Features

- **Interactive Gameplay**: Enter moves via command line
- **Two-Player Mode**: Play against another person
- **Computer Player**: Option to play against a computer opponent
- **Game History**: Automatic logging of all game moves and results
- **Multiple Sessions**: Play multiple games in sequence
- **Win Detection**: Automatic detection of winning moves and draws
- **Structured Logs**: Each game's log is stored in a separate directory

## Requirements

- Python 3.6 or higher

## Installation

1. Clone or download this repository
2. Ensure you have Python installed

## How to Run

1. Navigate to the directory containing the project
2. Run the game using Python:

```bash
python tictactoe/main.py
```

Or if you're already in the project directory:

```bash
python main.py
```

On macOS/Linux, you can make the file executable and run it directly:

```bash
chmod +x tictactoe/main.py
./tictactoe/main.py
```

## How to Play

1. Start the game by running `main.py`
2. Enter the names of both players
   - If you enter "Computer" for a player name, that player will make random moves
3. The board is numbered 1-9 as follows:
   ```
   1 | 2 | 3
   ---------
   4 | 5 | 6
   ---------
   7 | 8 | 9
   ```
4. Players take turns entering a position number (1-9) to place their marker
5. The game ends when a player gets three in a row or the board is full (draw)
6. Choose whether to play again or exit

## Game Logs

Game logs are automatically created in a `game_log` directory. Each game session gets its own folder (game1, game2, etc.) with a `log.txt` file containing:

- Player information
- Move history with positions
- Board state at key points
- Game result (win or draw)

## Concepts Demonstrated

1. **Classes and Objects**:

   - `Board` class for game state
   - `Player` class for player management
   - `Logger` class for logging functionality

2. **Generators**:

   - Dynamic generation of available moves

3. **Pathlib for Directory Management**:

   - Creation and management of log directories

4. **Modular Code Organization**:

   - Clear separation of concerns
   - Well-defined module responsibilities

5. **Structured Logging**:
   - Human-readable game history

## Future Enhancements

Potential enhancements that could be added:

- Smarter AI using the minimax algorithm
- Game statistics tracking
- Customizable board size
- GUI interface
- Network multiplayer
