import numpy as np

def is_valid(board):
    
    n = 9  
    
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

def read_sudoku_grids_from_file(filename):
    
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    grids = []
    i = 0
    while i < len(lines):
        n = int(lines[i].strip()) 
        grid = []
        i += 1
        for j in range(n):
            row = list(map(int, lines[i + j].strip().split()))
            grid.append(row)
        grids.append(grid)
        i += n
    
    return grids

def generate_binary_sequence_from_grids(grids):
    
    binary_sequence = []
    for grid in grids:
        if is_valid(grid):
            binary_sequence.append('1')
        else:
            binary_sequence.append('0')
    return ''.join(binary_sequence)

grids = read_sudoku_grids_from_file('test_cases.txt')

binary_sequence = generate_binary_sequence_from_grids(grids)

print(binary_sequence)
