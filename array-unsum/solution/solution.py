
window_length = 6
def unsum(arr):
    result = [0] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        if len(arr) - 1 - i == 0:
            result[i] = arr[-1]
            continue
        result[i] = arr[i] - sum(result[i + 1:min(len(arr), i + window_length)])
    return result

arr = 
sums = 
print(arr)
print(unsum(sums))
