from collections import deque
import hashlib

def shortest_path(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque([(start[0], start[1], 0)])  
    visited = set()
    visited.add((start[0], start[1]))

    while queue:
        r, c, steps = queue.popleft()
        if (r, c) == end:
            return steps
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc, steps + 1))
    return -1  

def solve_test_cases(file_name="test_cases.txt"):
    with open(file_name, "r") as f:
        test_cases = f.read().strip().split("\n\n")

    results = []
    for test in test_cases:
        lines = test.strip().split("\n")
        rows, cols = map(int, lines[0].split())
        grid = [list(map(int, lines[i + 1].split())) for i in range(rows)]
        start = tuple(map(int, lines[rows + 1].split()))
        end = tuple(map(int, lines[rows + 2].split()))
        result = shortest_path(grid, start, end)
        results.append(str(result))

    concatenated = "".join(results)
    return concatenated
    #return hashlib.sha256(concatenated.encode()).hexdigest()

flag = solve_test_cases()
print("Flag:", flag)
