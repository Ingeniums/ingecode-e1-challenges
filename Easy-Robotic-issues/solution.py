


def get_input(file=__file__.replace(__file__.split('/')[-1], '')+'/input.txt'):
    with open(file, 'r') as f:
        commands = f.read().strip().split(',')
        return commands
    
def robot_path(commands):
    x, y = 0, 0
    visited = {(0, 0)}
    
    moves = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
    
    for command in commands:
        dx, dy = moves[command]
        x, y = x + dx, y + dy
        if (x, y) in visited:
            return "TRAPPED"
        visited.add((x, y))
    
    return "({},{})".format(x, y)


def main():
    test_cases = get_input()
    flag = ""
    for case in test_cases:
        flag += robot_path(case) +","
    flag = flag[:-1]
    print(flag)
    #md5 hash the string
    import hashlib
    print(hashlib.md5(flag.encode()).hexdigest())


if __name__ == '__main__':
    main()