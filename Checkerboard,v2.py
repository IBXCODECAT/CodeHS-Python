# Pass this function a list of lists, and it will
# print it such that it looks like the grids in
# the exercise instructions.
def print_board(board):
    for i in range(len(board)):
        
        if(True):
            # This line uses some Python you haven't
            # learned yet. You'll learn about this
            # part in a future lesson:
            #
            [str(x) for x in board[i]]
            print " ".join([str(x) for x in board[i]])

# Your code here...

row = ['0', '1', '0', '1', '0', '1', '0', '1']
rowInverted = ['1', '0', '1', '0', '1', '0', '1', '0']
board = [ row, rowInverted, row, rowInverted, row, rowInverted, row, rowInverted]

print_board(board)