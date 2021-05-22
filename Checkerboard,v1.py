# Pass this function a list of lists, and it will
# print it such that it looks like the grids in
# the exercise instructions.
def print_board(board):
    for i in range(len(board)):
        
        # This line uses some Python you haven't
        # learned yet. You'll learn about this
        # part in a future lesson:
        #
        [str(x) for x in board[i]]
        print " ".join([str(x) for x in board[i]])

# Your code here...
oneRow = ['1', '1', '1', '1', '1', '1', '1', '1']
zeroRow = ['0', '0', '0', '0', '0', '0', '0', '0']
board = [ oneRow, oneRow, oneRow, zeroRow, zeroRow, oneRow, oneRow, oneRow]

print_board(board)