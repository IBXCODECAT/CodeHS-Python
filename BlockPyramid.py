"""
This code will ask the user how many blocks they want on the bottom of the pyramid
and then draw a pyramid of squares, subtracting one block from each row.
"""
# Set row value to 0
speed(0)
row_value=0

# This function moves to next row with x-value based on how many blocks are to
# be placed and the y-value based on the row number (gets 50 pixels higher each row)    
def move_to_row(num_blocks):
    x_value = -((num_blocks*50)/2)
    y_value = -200+(50*row_value)
    penup()
    setposition(x_value,y_value)
    pendown()

# This function draw a row of blocks based on user value    
def draw_block_row(num_blocks):
    for i in range(num_blocks):
        for i in range(4):
            forward(50)
            left(90)
        forward(50)

# Ask the user how many blocks should be on bottom row        
num_blocks=int(input("How many blocks on the bottom row? (8 or less): "))

# Call function to move Tracy to beginning of row position and then increase row
# variable value. Then Tracy will draw the row of blocks needed and subtract one
# from the num blocks variable.
for i in range(num_blocks):
    move_to_row(num_blocks)
    row_value=row_value+1
    draw_block_row(num_blocks)
    num_blocks=num_blocks-1