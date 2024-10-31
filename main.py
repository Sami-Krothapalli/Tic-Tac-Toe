# Board
# Display Board
# Play Game


board = ["-", "-", "-", 
         "-", "-", "-", 
         "-", "-", "-",]


def board_display():
    print(board[0] + "|" + board[1] + "|" + board[2] + "|")
    print(board[3] + "|" + board[4] + "|" + board[5] + "|")
    print(board[6] + "|" + board[7] + "|" + board[8] + "|") 

def handle_turn():
    name_pos = input("Are you X or O (respond w/ X or O): ")
    pos = input("Choose a position from 1 to 9:  ")
    
    if name_pos == "X":
        board[int(pos) - 1] = "X"
        board_display()
    else:
        board[int(pos) - 1] = "O"
        board_display()     
        
    
    

def check_if_game_over():
    check_if_win()
    check_if_tie()

def check_if_win():
    for rows in range(9):
        for cols in range(4):
            if board[rows] == board[rows + 1] and board[rows] == board[rows + 2] and board[rows + 1] == board[rows + 2]:
                print("Game Over")
            elif board[rows][cols] == board[rows][cols + 1] and board[rows][cols] == board[rows][cols + 2] and board[rows][cols + 1] == board[rows][cols + 2]:
                print("Game Over")


def check_if_tie():
    return

def change_turns():
    return


def play_game():
    
    #display the inital board
    board_display()
    
    while game_still_going:
        handle_turn(curr_player)

        check_if_game_over()
        
        change_turns()
    

        




    


play_game()
    