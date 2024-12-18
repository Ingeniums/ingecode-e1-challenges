import time

def get_input(file=__file__.replace(__file__.split('/')[-1], '')+'input.txt'):
    cases = []
    # [[random.randint(1,40) for _ in range(random.randint(2, 100))] for _ in range(random.randint(2, 100))]
    with open(file, 'r') as f:
        #while not eof
        num_cases = int(f.readline())
        while True:
            n = f.readline().strip()
            if n == "":
                break
            n = map(int, n.split())
            n, m = n
            grid = []
            for r in range(n):
                row  = map(int, f.readline().split())
                grid.append(list(row))
            cases.append(grid)
            
        return cases


def brute_force(grid):
    n, m = len(grid), len(grid[0])
    min_operations = float('inf')
    target_values = range(min(map(min, grid)), max(map(max, grid)) + 1)
    
    for target in target_values:
        operations = 0
        for i in range(n):
            for j in range(m):
                operations += abs(grid[i][j] - target)
        min_operations = min(min_operations, operations)
    
    return min_operations


def modular_arithmetic(grid):
    n, m = len(grid), len(grid[0])
    flattened = [grid[i][j] for i in range(n) for j in range(m)]
    target = sorted(flattened)[len(flattened) // 2]  # Median value
    
    operations = sum(abs(value - target) for value in flattened)
    return operations





def main():
    start = time.time()
    cases = get_input()
    flag = ""
    for cas in cases:
        flag += str(brute_force(cas)) +","

    print("finished in: " , time.time() - start)
    
    flag = flag[:-1]
    import hashlib
    print(hashlib.md5(flag.encode()).hexdigest())    
    
if __name__ == "__main__":
    main()

