import math
from hashlib import sha256

def calculate_visible_sandwiches(test_cases):
    results = []

    for x, y, sandwiches in test_cases:
        visibility_map = {}

        for sx, sy in sandwiches:
            dx, dy = sx - x, sy - y
            gcd = math.gcd(dx, dy)
            direction = (dx // gcd, dy // gcd)

            if direction not in visibility_map or gcd < visibility_map[direction][0]:
                visibility_map[direction] = (gcd, (sx, sy))

        visible_sandwiches = [coord for _, coord in visibility_map.values()]
        visible_sandwiches.sort()  # Sort by x, then y
        results.append(visible_sandwiches)

    return results

def compute_flag(visible_sandwiches):
    concatenated = "".join(f"{x}{y}" for sandwiches in visible_sandwiches for x, y in sandwiches)
    return sha256(concatenated.encode()).hexdigest()


def main():
    with open("testcases.txt", "r") as file:
        lines = file.readlines()

    T = int(lines[0].strip())
    test_cases = []
    idx = 1

    for _ in range(T):
        x, y, n = map(int, lines[idx].strip().split())
        idx += 1
        sandwiches = [tuple(map(int, lines[idx + i].strip().split())) for i in range(n)]
        idx += n
        test_cases.append((x, y, sandwiches))

    visible_sandwiches = calculate_visible_sandwiches(test_cases)
    # print(visible_sandwiches)
    with open("flag.txt", "w") as file:
        # for sandwiches in visible_sandwiches:
        #     for sx, sy in sandwiches:
        #         file.write(f"{sx} {sy}\n")
        file.write(f"{compute_flag(visible_sandwiches)}\n")

if __name__ == "__main__":
    main()
