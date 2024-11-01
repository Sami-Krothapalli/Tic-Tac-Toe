# Initialize the board and other global variables
board = ["-", "-", "-", 
         "-", "-", "-", 
         "-", "-", "-"]
current_player = "X"
winner = None
game_still_going = True

def display_board():
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("\n")

def handle_turn(player):
    print(f"{player}'s turn.")
    position = input("Choose a position from 1-9: ")
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid input. Choose a position from 1-9: ")
        position = int(position) - 1
        if board[position] == "-":
            valid = True
        else:
            print("You can't go there. Go again.")
    board[position] = player
    display_board()

def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():
    global winner
    row_winner = check_rows()
    col_winner = check_cols()
    diag_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif col_winner:
        winner = col_winner
    elif diag_winner:
        winner = diag_winner
    else:
        winner = None

def check_rows():
    global game_still_going
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] != "-":
            game_still_going = False
            return board[i]
    return None

def check_cols():
    global game_still_going
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] != "-":
            game_still_going = False
            return board[i]
    return None

def check_diagonals():
    global game_still_going
    if board[0] == board[4] == board[8] != "-":
        game_still_going = False
        return board[0]
    elif board[2] == board[4] == board[6] != "-":
        game_still_going = False
        return board[2]
    return None

def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False

def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

def play_game():
    display_board()
    while game_still_going:
        handle_turn(current_player)
        check_if_game_over()
        if game_still_going:
            flip_player()
    if winner:
        print(f"{winner} won.")
    else:
        print("Tie.")

# Start the game
play_game()