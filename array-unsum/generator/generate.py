import random
import sys

# constants
max_int = 1_000_000_000_000_000
window_length = 6

def generate_array(length):
    return [random.randint(1, max_int) for _ in range(length)]

def xor(arr):
    result = 0
    for i in arr:
        result ^= i
    return result

def calculate_sub_sums(arr):
    sums = [sum(arr[0:window_length])]
    for i in range(1, len(arr)):
        result = sums[-1]
        if i + window_length - 1 < len(arr):
            result += arr[i + window_length - 1]
        result -= arr[i - 1]
        sums.append(result)
    return sums

def write_flag(i):
    with open(sys.argv[2], "w") as file:
        file.write(str(i))

def generate_sums(num):
    arrays = [generate_array(random.randint(12, 27)) for _ in range(num)]
    flag = sum(list(map(lambda arr: xor(arr), arrays)))
    write_flag(flag)
    return [calculate_sub_sums(arr) for arr in arrays]

def output(arrays):
    lines = [f"{len(arrays)}\n"]
    for arr in arrays:
        lines.append(f"{len(arr)}\n")
        lines.append(" ".join(list(map(lambda e: str(e), arr))) + "\n")
    with open(sys.argv[1], "w") as file:
        file.writelines(lines)


num_lines = 6000
output(generate_sums(num_lines))
