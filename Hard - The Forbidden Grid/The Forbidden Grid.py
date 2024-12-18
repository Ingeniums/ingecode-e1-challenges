def isSafeToPut(i, j, option, board, n, forbidden):

    for k in range(n):
        if board[k][j] == option or board[i][k] == option:
            return False

    starti = (i // 3) * 3
    startj = (j // 3) * 3

    for p in range(starti, starti + 3):
        for q in range(startj, startj + 3):
            if board[p][q] == option:
                return False

    if option in forbidden[i][j]:
        return False
    
    return True


def sudokuSolver(i, j, board, n, forbidden):
    if i == n:
        return True
    
    if j == n:
        return sudokuSolver(i + 1, 0, board, n, forbidden)

    if board[i][j] != 0:
        return sudokuSolver(i, j + 1, board, n, forbidden)
    
    for option in range(1, 10):
        if isSafeToPut(i, j, option, board, n, forbidden):
            board[i][j] = option
            canWeMoveFwd = sudokuSolver(i, j + 1, board, n, forbidden)
            if canWeMoveFwd:
                return True
            board[i][j] = 0

    return False

filename = 'inputs.txt'

with open(filename, 'r') as file:
        test_cases = []

        T = int(file.readline().strip())

        for i in range(T):
            
            board = []
            for _ in range(9):
                line = file.readline().strip()
                board.append(list(map(int, line.split())))

            if not board:
                break

            m = 0
            line = file.readline().strip()
            if line:
                m = int(line)

            forbidden = [[set() for _ in range(9)] for _ in range(9)]

            for _ in range(m):
                line = file.readline().strip()
                if line:
                    r, c, num = map(int, line.split())
                    forbidden[r][c].add(num)

            test_cases.append((board, forbidden))
        
flag = ""
        
for index, (board, forbidden) in enumerate(test_cases):
    
    ans = sudokuSolver(0, 0, board, 9, forbidden)

    if ans:
        for row in board:
            print(" ".join(map(str, row)))
        print()
        flag +="1"
    else:
        print("No solution.\n")
        flag += "0"

print(flag)