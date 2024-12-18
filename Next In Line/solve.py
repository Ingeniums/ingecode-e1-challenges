def next(test):
    p, q = test
    return (q, q - p % q + (p // q) * q)

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

    for case in data[1:]:
        p, q = map(int, case.split())
        results.append(next((p, q)))

    with open(output_file, "w") as f:
        for result in results:
            f.write(f"{result[0]} {result[1]}\n")

if __name__ == "__main__":
    main()