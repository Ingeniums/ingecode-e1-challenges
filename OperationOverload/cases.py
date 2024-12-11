import random

def generate_test_case():
    rows = random.randint(5, 10)
    cols = random.randint(5, 10)
    grid = [[0 for _ in range(cols)] for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            if random.random() < 0.3:  
                grid[i][j] = 1

    start = (random.randint(0, rows - 1), random.randint(0, cols - 1))
    end = (random.randint(0, rows - 1), random.randint(0, cols - 1))
    grid[start[0]][start[1]] = 0
    grid[end[0]][end[1]] = 0

    return grid, start, end

def save_test_cases(file_name="test_cases.txt", num_cases=100):
    with open(file_name, "w") as f:
        for _ in range(num_cases):
            grid, start, end = generate_test_case()
            rows = len(grid)
            cols = len(grid[0])
            f.write(f"{rows} {cols}\n")
            for row in grid:
                f.write(" ".join(map(str, row)) + "\n")
            f.write(f"{start[0]} {start[1]}\n")
            f.write(f"{end[0]} {end[1]}\n")
            f.write("\n")  

save_test_cases()
