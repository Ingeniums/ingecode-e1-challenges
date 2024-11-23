import sys

window_length = 6
def unsum(arr):
    result = [0] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        if len(arr) - 1 - i == 0:
            result[i] = arr[-1]
            continue
        result[i] = arr[i] - sum(result[i + 1:min(len(arr), i + window_length)])
    return result

def xor(arr):
    result = 0
    for i in arr:
        result ^= i
    return result

with open(sys.argv[1]) as file:
    arrays = list(map(lambda line: list(map(lambda s: int(s), line[:-1].split(","))), file.readlines()))

print(sum([xor(unsum(arr)) for arr in arrays]))
