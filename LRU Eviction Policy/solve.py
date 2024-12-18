def lru_page_faults(cache_capacity, requests):
    cache = []
    page_hits = 0
    page_faults = 0

    for request in requests:
        if request in cache:
            page_hits += 1
            cache.remove(request)  # Move the accessed page to the most recently used position
            cache.append(request)
        else:
            page_faults += 1
            if len(cache) < cache_capacity:
                cache.append(request)  # Add to cache if space is available
            else:
                cache.pop(0)  # Evict the least recently used page
                cache.append(request)
    return f"{page_hits} {page_faults}\n{' '.join(map(str, cache))}"

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
        cache_capacity, num_requests = map(int, data[idx].split())
        requests = list(map(int, data[idx + 1].split()))
        idx += 2
        results.append(lru_page_faults(cache_capacity, requests))
    
    with open(output_file, "w") as f:
        for result in results:
            f.write(f"{result}\n")

if __name__ == "__main__":
    main()