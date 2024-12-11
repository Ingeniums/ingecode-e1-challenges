import hashlib

def maxProfit(prices):
    n = len(prices)
    max_profit = 0

    # Brute-force: Try all combinations of two transactions
    for i in range(n):
        for j in range(i + 1, n):  # First transaction: Buy on day i, sell on day j
            first_transaction_profit = prices[j] - prices[i] if prices[j] > prices[i] else 0

            # Second transaction: After the first, buy on day k, sell on day l
            for k in range(j + 1, n):  # Buy again after the first transaction
                for l in range(k + 1, n):  # Sell after the second buy
                    second_transaction_profit = prices[l] - prices[k] if prices[l] > prices[k] else 0

                    # Calculate total profit from both transactions
                    total_profit = first_transaction_profit + second_transaction_profit
                    max_profit = max(max_profit, total_profit)

    return max_profit


# Read the test cases from the file
results = []

# Replace 'test_cases.txt' with your actual file path
with open('test_cases.txt', 'r') as file:
    num_cases = int(file.readline().strip())  # Read number of test cases
    for _ in range(num_cases):
        n = int(file.readline().strip())  # Read number of days for the current test case
        prices = list(map(int, file.readline().strip().split()))  # Read the prices for the test case
        profit = maxProfit(prices)  # Get the max profit for this test case
        results.append(profit)  # Store the result

# Concatenate all the results as a string
result_string = "".join(map(str, results))

# Compute MD5 hash of the concatenated result string
hashed_result = hashlib.md5(result_string.encode()).hexdigest()

# Print the MD5 hash
print(f"MD5 Hash of All Results: {hashed_result}")
