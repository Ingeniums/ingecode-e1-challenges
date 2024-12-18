def clock_policy_page_faults(buffer_size, requests):
    buffer_pool = [-1] * buffer_size
    ref_array = [0] * buffer_size
    clock_hand = 0
    page_hits = 0
    page_faults = 0

    for request in requests:
        if request in buffer_pool:
            page_hits += 1
            ind = buffer_pool.index(request)
            ref_array[ind] = 1
        else:
            page_faults += 1
            while ref_array[clock_hand] != 0:
                ref_array[clock_hand] = 0
                clock_hand = (clock_hand + 1) % buffer_size
            buffer_pool[clock_hand] = request
            ref_array[clock_hand] = 1
            clock_hand = (clock_hand + 1) % buffer_size

    return f"{page_hits} {page_faults}\n{' '.join(map(str, buffer_pool))}"

def main():
    import sys
    if len(sys.argv) != 3:
        print("Usage: python solve.py <input_file> <output_file>")
        return
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    with open(input_file, "r") as f:
        data = f.read().splitlines()
    
    test_cases = int(data[0])  # First line specifies the number of test cases
    results = []

    idx = 1
    for _ in range(test_cases):
        buffer_size, num_requests = map(int, data[idx].split())
        requests = list(map(int, data[idx + 1].split()))
        idx += 2
        results.append(clock_policy_page_faults(buffer_size, requests))
    
    with open(output_file, "w") as f:
        for result in results:
            f.write(f"{result}\n")

if __name__ == "__main__":
    main()
