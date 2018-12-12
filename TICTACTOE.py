#brandon robbins
#12/18
#tictactoe
X="X"
O="O"
EMPTY=" "
TIE = "TIE"
NUM_SQUARES = 9
def display():
    print("Welcome to TicTacToe")
    print()
    print()
    print("""The rules are as follows.
- There are a range of squares 0-8 where you may place your piece
- Player 1 is X and X goes first
- First to put 3 in a row wins
- This is your board""")
    print()
    print()
    print("""
    0  |    1    |   2    
   -----------------
    3   |   4   |   5                
   -----------------
    6   |   7   |   8    
              """)
    print("you think you can beat the MACHINE!")
#ask yes or no 
def ask_yes_no(question):
    response=None
    while response not in ("y","n"):
        response = input(question+"y or n ").lower()
    return response
#ask the number
def ask_num(question,low,high):
    response ="9999"
    while True:
        if response.isdigit():
            if int(response) in range(low, high):
                break
            else:
                response = input(question)
        else:
            print("you must enter a number")
            response = input(question)
    return int(response)
#pieces
def pieces():
    go_first=ask_yes_no("do you want to go first?")
    if go_first== "y":
        human= X
        computer= O
        print("first to lose!")
    else:
        human= O
        computer = X
        print("Ha coward")
    return human, computer
# the blank board list
def new_board():
    board=[]
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board
# display the new board
def display_board(board):
    """Display game board on screen"""
    print("\n\t", board[0], "|" , board[1] ,"|", board[2])
    print("\t","----------")
    print("\t", board[3], "|" , board[4], "|" , board[5])
    print("\t","----------")
    print("\t", board[6], "|" , board[7], "|" , board[8], "\n")
# legal moves lsit
def legal_moves(board):
    moves = []
    for square in range(NUM_SQUARES):
        if board[square]==EMPTY:
            moves.append(square)
        return moves
# winner winner
def winner(board):
    """Determine the game winner."""
    WAYS_TO_WIN=((0,1,2),
                 (3,4,5),
                 (6,7,8),
                 (0,3,6),
                 (1,4,7),
                 (2,5,8),
                 (0,4,8),
                 (2,4,6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
        if EMPTY not in board:
            return TIE
        
        return None


