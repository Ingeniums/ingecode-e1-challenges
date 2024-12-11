import random
import numpy as np

def is_valid(board):
    """
    Checks if a given 9x9 Sudoku grid is valid based on row, column, and subgrid rules.
    """
    n = 9  # We are working with a fixed 9x9 grid
    
    # Check rows and columns for duplicates
    for i in range(n):
        row_set = set()
        col_set = set()
        for j in range(n):
            # Check for duplicates in rows
            if board[i][j] != 0:
                if board[i][j] in row_set:
                    return False
                row_set.add(board[i][j])
            # Check for duplicates in columns
            if board[j][i] != 0:
                if board[j][i] in col_set:
                    return False
                col_set.add(board[j][i])
    
    # Check 3x3 subgrids for duplicates
    for i in range(0, n, 3):
        for j in range(0, n, 3):
            subgrid_set = set()
            for x in range(3):
                for y in range(3):
                    val = board[i + x][j + y]
                    if val != 0:
                        if val in subgrid_set:
                            return False
                        subgrid_set.add(val)
    return True

def generate_valid_sudoku():
    """
    Generates a valid 9x9 Sudoku grid using a backtracking algorithm.
    """
    n = 9
    board = np.zeros((n, n), dtype=int)

    def solve(board):
        for row in range(n):
            for col in range(n):
                if board[row][col] == 0:
                    for num in range(1, n + 1):
                        board[row][col] = num
                        if is_valid(board):
                            if solve(board):
                                return True
                        board[row][col] = 0
                    return False
        return True
    
    solve(board)
    return board.tolist()

def generate_invalid_sudoku():
    """
    Generates an invalid 9x9 Sudoku grid by modifying a valid grid.
    """
    board = generate_valid_sudoku()
    row = random.randint(0, 8)  # Randomly select a row
    col1, col2 = random.sample(range(9), 2)  # Select two distinct column indices
    board[row][col1], board[row][col2] = board[row][col2], board[row][col1]  # Swap two numbers to create an invalid grid
    return board

def sudoku_to_string(board):
    """Converts a 2D Sudoku board into a string representation."""
    return '\n'.join(' '.join(str(cell) for cell in row) for row in board)

def write_sudoku_grids_to_file(filename, sequence):
    """Writes test cases with random validity based on the sequence of 0s and 1s."""
    with open(filename, 'w') as file:
        for char in sequence:
            if char == '1':
                grid = generate_valid_sudoku()
            else:
                grid = generate_invalid_sudoku()
            
            grid_str = sudoku_to_string(grid)
            file.write(f"9\n{grid_str}\n")  # We are always generating 9x9 grids

# The sequence provided by the user
sequence = ("010100000110000101110100011010010110010101101110011000110110010100100000011010010111001100100000011000010010000001101011011001010111100100100000011001010110110001100101011011010110010101101110011101000010000001101111011001100010000001110011011101010110001101100011011001010111001101110011")

# Write the grids to the test_cases.txt file
write_sudoku_grids_to_file("test_cases.txt", sequence)

print("Test cases written to test_cases.txt.")
