def get_valid_index(prompt):
    while True:
        try:
            index = int(input(prompt))
            if index >= 0 and index <= 2:
                return index
            print "Must be 0 - 2 inclusive!"
        except ValueError:
            print "Must be an integer!"
def game_is_over(board):
    for i in range(3):
        # Check horizontal
        if board[i][0] == board[i][1] == board[i][2] \
            and board[i][0] != " ":
            print board[i][0] + " wins!"
            return True
        
        # Check vertical
        if board[0][i] == board[1][i] == board[2][i] \
            and board[0][i] != " ":
            print board[0][i] + " wins!"
            return True
        
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] \
        and board[0][0] != " ":
        print board[0][0] + " wins!"
        return True
    
    if board[2][0] == board[1][1] == board[0][2] \
        and board[2][0] != " ":
        print board[2][0] + " wins!"
        return True
    
    # Check tie
    if " " not in board[0] and " " not in board[1] \
        and " " not in board[2]:
        print "Tie game!"
        return True
    
    # Not over yet!
    return False
def print_board(board):
    
    for i in range(len(board)):
        [str(x) for x in board[i]]
        print " ".join([str(x) for x in board[i]])

# TODO: Set up the board as a 3x3 grid of spaces here...
board = [ [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' '] ]
    
print_board(board)
    
# x goes first


# Play tic tac toe
turnCounter = 0
while not game_is_over(board):
    
    if(turnCounter % 2 == 0):
        turn = 'X'
    else:
        turn = 'O'
    
    print "It's " + turn + "'s turn."
    row = get_valid_index("Row: ")
    col = get_valid_index("Col: ")
    
    board[row][col] = turn
    print_board(board)
    
    turnCounter = turnCounter + 1