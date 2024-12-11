import hashlib

def maxProfit(prices):
    if not prices or len(prices) < 2:
        return 0

    n = len(prices)

    profit1 = [0] * n
    min_price = prices[0]
    for i in range(1, n):
        min_price = min(min_price, prices[i])
        profit1[i] = max(profit1[i - 1], prices[i] - min_price)

    profit2 = [0] * n
    max_price = prices[-1]
    for i in range(n - 2, -1, -1):
        max_price = max(max_price, prices[i])
        profit2[i] = max(profit2[i + 1], max_price - prices[i])

    max_profit = 0
    for i in range(n):
        max_profit = max(max_profit, profit1[i] + (profit2[i + 1] if i + 1 < n else 0))

    return max_profit


results = []
with open('test_cases.txt', 'r') as file:
    num_cases = int(file.readline().strip())
    for _ in range(num_cases):
        n = int(file.readline().strip())
        prices = list(map(int, file.readline().strip().split()))
        profit = maxProfit(prices)
        results.append(profit)

result_string = "".join(map(str, results))

hashed_result = hashlib.md5(result_string.encode()).hexdigest()


print(f"MD5 Hash of Results: {hashed_result}")
