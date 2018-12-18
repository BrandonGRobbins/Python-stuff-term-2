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
    """Create new game board."""
    board = []
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
    """Create list of legal moves."""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves
# winner winner
def winner(board):
    """Determine the game winner."""
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner

    if EMPTY not in board:
        return TIE

    return None
#human moves
def human_move(board):
    legal=legal_moves(board)
    move=None
    while move not in legal:
        move=ask_num("Where will you move? (0-8):",0,NUM_SQUARES)
        if move not in legal:
            print("You really think that would work?... Pathetic")
    return move
#next turn function
def next_turn(turn):
    """Switch turns"""
    if turn ==X:
        return O
    else:
        return X
# Congrats winner
def congrats_winner(winner,human,computer):
    if winner != TIE:
        print(winner," won")
    else:
        print("its a tie")
    if winner==human:
        print("you have bested me... this time")
    elif winner == computer:
        print("you lose and i win HAHAHAHA")
    elif winner== TIE:
        print("wow you really stink you tied with me.")
# computer move
def computer_move(board,human,computer):
    """make computer move"""
    #make a copy to work with since function will be changing list
    board=board[:]
    #the best postitions to have in order
    BEST_MOVES=(4,0,2,6,8,1,3,5,7)
    print("i shall take square number",end=" ")
    #if computer can win take that move
    for move in legal_moves(board):
        board[move]=computer
        if winner(board)==computer:
            print(move)
            return move
        #done checking this move undo it
        board[move]=EMPTY
        # human can win take that move
    for move in legal_moves(board):
        board[move]=human
        if winner(board)==human:
            print(move)
            return move
        #done checking this move undo it
        board[move]=EMPTY
    #since no one can win on next move pick the best open square
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move
def main():
    display()
    board=new_board()
    human, computer=pieces()
    win=None
    turn=None
    while win==None:
        turn=next_turn(turn)
        display_board(board)
        if turn==human:
           moves=human_move(board)
           board[moves]=human
        
        else:
            moves=computer_move(board,human,computer)
            board[moves]=computer
        display_board(board)
        win=winner(board)
    congrats_winner(win,human,computer)
main()
