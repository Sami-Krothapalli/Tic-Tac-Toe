# Tic Tac Toe Game

This is a simple command-line Tic Tac Toe game implemented in Python. The game allows two players to take turns and play the classic Tic Tac Toe game.

## How to Play

1. The game board is a 3x3 grid.
2. Players take turns to place their marker (X or O) on the board.
3. The first player to get three of their markers in a row (horizontally, vertically, or diagonally) wins the game.
4. If all nine squares are filled and no player has three in a row, the game is a tie.

## Getting Started

### Prerequisites

- Python 3.x

### Running the Game

1. Clone the repository or download the `main.py` file.
2. Open a terminal and navigate to the directory containing `main.py`.
3. Run the game using the following command:

```sh
python [main.py](http://_vscodecontentref_/2)
```
Sure, here is the complete README.md file with the game instructions, code overview, and example output in Markdown format:


### Game Instructions
- The game will display the board and prompt the current player to choose a position from 1 to 9.
- Enter the number corresponding to the position where you want to place your marker.
- The game will update the board and switch to the other player.
- The game will continue until there is a winner or a tie.

### Code Overview
- display_board(): Displays the current state of the board.
- handle_turn(player): Handles the player's move and updates the board.
- check_if_game_over(): Checks if the game is over by checking for a winner or a tie.
- check_for_winner(): Checks rows, columns, and diagonals for a winner.
- check_rows(), check_cols(), check_diagonals(): Return the winner ("X" or "O") if a - - row, column, or diagonal is complete.
- check_if_tie(): Ends the game if there are no empty spaces left.
- flip_player(): Alternates the current player between "X" and "O".
- play_game(): Manages the game loop, displaying the board and current player after
each move, and announces the winner or a tie at the end.


### Example

- | - | -
- | - | -
- | - | -

X's turn.
Choose a position from 1-9: 5

- | - | -
- | X | -
- | - | -