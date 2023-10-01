def solve(board):
    """
    Solve the sudoku puzzle using Backtracking.
    Recursively attempts to fill cells until the board is solved or no valid
    number can be found for a cell.
    """
    empty_cell = find_empty_cell(board)
    if not empty_cell:  # Return True if no empty cell is found, i.e., board is solved.
        return True

    row, col = empty_cell

    for num in range(1, 10):  # Try numbers from 1 to 9
        if is_valid(board, num, (row, col)):
            board[row][col] = num  # Assign number to the empty cell
            
            if solve(board):  # Recursively try to fill the next cell
                return True  # Return True if board is solved

            board[row][col] = 0  # Reset cell value to 0 if no valid number can be found

    return False  # Return False if no valid number can be found for this cell


def is_valid(board, num, pos):
    """
    Check whether it is valid to place `num` at position `pos`.
    Returns True if it's valid, False otherwise.
    """
    row, col = pos
    
    # Check row
    if num in board[row]:
        return False
    
    # Check column
    if num in [board[i][col] for i in range(9)]:
        return False

    # Check 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True  # Return True if `num` can be placed in position `pos`


def print_board(board):
    """
    Print the sudoku board in a readable format.
    """
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - + - - - + - - -")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")

            print(board[i][j], end=" ")

            if j == 8:
                print()


def find_empty_cell(board):
    """
    Find and return the row, col index of an empty cell that contains 0.
    Returns None if no empty cell is found.
    """
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i, j
    return None

# Define the Sudoku board as a 2D list.
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Unsolved Sudoku:")
print_board(sudoku_board)

if solve(sudoku_board):
    print("Solved Sudoku:")
    print_board(sudoku_board)
else:
    print("No solution exists")
