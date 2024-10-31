# Board
# Display Board
# Play Game

# Global Variables
board = ["-", "-", "-", 
         "-", "-", "-", 
         "-", "-", "-",]

game_still_going = True

winner = None

curr_player = "X"


def board_display():
    print(board[0] + "|" + board[1] + "|" + board[2] + "|")
    print(board[3] + "|" + board[4] + "|" + board[5] + "|")
    print(board[6] + "|" + board[7] + "|" + board[8] + "|") 

def handle_turn(player):
    pos = input("Choose a position from 1 to 9:  ")m
    board[int(pos) - 1] = "X"
    board_display()
    

def check_if_game_over():
    check_if_win()
    check_if_tie()

def check_if_win():
    #Check Rows
    #Check Cols
    #Check Diags
    return 

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
    