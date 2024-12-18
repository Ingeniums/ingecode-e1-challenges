import hashlib


def find_cheesiest_slice(grid, n, m, i, j):
    # Build prefix sum grid
    prefix_sum = [[0] * (m + 1) for _ in range(n + 1)]
    for r in range(n):
        for c in range(m):
            prefix_sum[r + 1][c + 1] = (
                prefix_sum[r][c + 1] +
                prefix_sum[r + 1][c] -
                prefix_sum[r][c] +
                (1 if grid[r][c] == '#' else 0)
            )

    max_cheese = -1
    top_left_x, top_left_y = 0, 0

    # Iterate over all possible top-left corners of i x j slices
    for start_row in range(n - i + 1):
        for start_col in range(m - j + 1):
            # Calculate the sum of cheese in the current slice using the prefix sum
            cheese_count = (
                prefix_sum[start_row + i][start_col + j]
                - prefix_sum[start_row][start_col + j]
                - prefix_sum[start_row + i][start_col]
                + prefix_sum[start_row][start_col]
            )

            # Update the maximum cheese count and the slice's position
            if cheese_count > max_cheese:
                max_cheese = cheese_count
                top_left_x, top_left_y = start_row, start_col

    # Extract the cheesiest slice safely
    if max_cheese == -1:
        return -1  # No valid slice found
    cheesiest_slice = [
        grid[row][top_left_y:top_left_y + j]
        for row in range(top_left_x, min(top_left_x + i, len(grid)))
    ]

    return cheesiest_slice


def main():
    with open("testcases.txt", "r") as f:
        lines = f.readlines()

    T = int(lines[0].strip())
    line_index = 1

    slices = []

    for _ in range(T):
        n, m = map(int, lines[line_index].strip().split(' '))
        i, j = map(int, lines[line_index + 1].strip().split(' '))
        grid = [line.strip() for line in lines[line_index + 2:line_index + n + 2]]
        line_index += n + 2

        # Validate grid dimensions
        if len(grid) != n or any(len(row) != m for row in grid):
            raise ValueError(f"Invalid grid dimensions for test case {_}")

        cheesiest_slice = find_cheesiest_slice(grid, n, m, i, j)
        # print(cheesiest_slice)
        if cheesiest_slice != -1:
            slices.extend(cheesiest_slice)

    concatenated_slices = "".join(slices)
    hash_object = hashlib.sha256(concatenated_slices.encode('utf-8'))
    hash_digest = hash_object.hexdigest()
    
    with open("flag_opt.txt", "w") as f:
        f.write(hash_digest)

if __name__ == "__main__":
    main()



