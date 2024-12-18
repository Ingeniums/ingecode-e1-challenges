import hashlib
import time

def count_triangle_sandwiches_faster_corect(n):
    if n % 2 == 0:
        return round((n * n) / 48)
    else:
        return round(((n + 3) * (n + 3)) / 48)

def calculate_perimeter_for_customers(k_values):
    results = []
    for k in k_values:
        n = 1
        while count_triangle_sandwiches_faster_corect(n) < k:
            n += 1
        results.append(n)
    return results

def calculate_perimeter_for_customers_binary_search(k_values):
    results = []

    def binary_search(k):
        low, high = 1, 10**6
        while low < high:
            mid = (low + high) // 2
            if count_triangle_sandwiches_faster_corect(mid) < k:
                low = mid + 1  
            else:
                high = mid
        
        low = low - 8 # do this because it is not a monotonic function, and it have a pattern
        if(low < 0): low = 0
        
        while(count_triangle_sandwiches_faster_corect(low) < k): 
            low = low + 1
        
        return low

    for k in k_values:
        results.append(binary_search(k))
    return results

if __name__ == "__main__":
    with open("testcases.txt", "r") as file:
        lines = file.readlines()

    t = int(lines[0])
    final_output = []

    line_index = 1

    # Start timing
    start_time = time.perf_counter()

    for _ in range(t):
        m = int(lines[line_index])
        line_index += 1
        k_values = list(map(int, lines[line_index].split()))
        line_index += 1

        results = calculate_perimeter_for_customers_binary_search(k_values)
        final_output.extend(results)
        # print(" ".join(map(str, results))) # use this to see the output before hashing

    end_time = time.perf_counter()

    concatenated_result = "".join(map(str, final_output))
    hashed_result = hashlib.sha256(concatenated_result.encode("utf-8")).hexdigest()

    print(hashed_result)
    print(f"Execution Time: {(end_time - start_time) * 1000:.2f} ms")