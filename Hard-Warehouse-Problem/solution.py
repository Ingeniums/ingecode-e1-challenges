import math


def get_input(file=__file__.replace(__file__.split('/')[-1], '')+'input.txt'):
    cases = []
    with open(file, 'r') as f:
        #while not eof
        num_cases = int(f.readline())
        while True:
            n = f.readline().strip()
            if n == "":
                break
            n = map(int, n.split())
            n, w = n
            weights = map(int, f.readline().split())
            values =  map(int, f.readline().split())
            cas = (n, w, list(weights), list(values))
            cases.append(cas)
            
        return cases


# this is the solution for the traditional challenge 0/a knapsack problem
def solution_dp_01_knapsack(n, w, weights, values):
    # Initialize a DP table
    dp = [[0] * (w + 1) for _ in range(n + 1)]
    
    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(w + 1):
            if weights[i - 1] <= j:  # If the current item's weight fits
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + values[i - 1])
            else:  # Otherwise, skip the item
                dp[i][j] = dp[i - 1][j]
    
    return dp[n][w]


# the below two solutions are the same just programmed in diffrent manners
def solution_greedy_fractional_me (n, w, weights, values):
    #sort the values  based on value/weight propotion
    sorted_values = [y[1] for y in sorted(enumerate(values), key=lambda x: x[1] / weights[x[0]])]
    sorted_weights = [y[1] for y in sorted(enumerate(weights), key=lambda x:  values[x[0]] / x[1] )]

    current_weight = 0
    current_value = 0
    i = 0
    
    while (current_weight <= w) and  (len(sorted_values) > 0):
        crrnt_elem = [sorted_values.pop(), sorted_weights.pop()]

        if (current_weight+crrnt_elem[1] > w):
            remaining_weight = w - current_weight
            current_value += crrnt_elem[0] * (remaining_weight / crrnt_elem[1])
            break
        current_value += crrnt_elem[0]
        current_weight += crrnt_elem[1]
    
    return current_value

def solution_greedy_gpt(n, w, weights, values):
    # Create a list of items with (value, weight, value-to-weight ratio)
    items = [(values[i], weights[i], values[i] / weights[i]) for i in range(n)]
    # Sort the items by value-to-weight ratio in descending order
    items.sort(key=lambda x: x[2], reverse=True)
    # sorted_values = [y[1] for y in sorted(enumerate(values), key=lambda x: x[1] / weights[x[0]])]
    # sorted_weights = [y[1] for y in sorted(enumerate(weights), key=lambda x:  values[x[0]] / x[1] )]
    # print(items)
    # print(sorted_values)
    # print(sorted_weights)
    
    current_weight = 0
    current_value = 0

    for value, weight, _ in items:
        if current_weight + weight <= w:
            current_value += value
            current_weight += weight
        else:
            remaining_weight = w - current_weight
            current_value += value * (remaining_weight / weight)
            break  # Knapsack is now full
    return current_value

    
# # Example Input
# n = 5
# w = 90
# weights = [10, 5, 20, 30, 20]
# values = [60, 60, 20, 120, 50 ]

def main():
    cases = get_input()
    flag = ""
    flag2 = ""
    for n, w, weights, values in cases:
        sol1 = str(math.floor(solution_greedy_gpt(n, w, weights, values)))
        sol2 = str(math.floor(solution_greedy_fractional_me(n, w, weights, values)))
        
        if (sol1 != sol2):
            print(f"mismatch: sol1:{sol1} sol2:{sol2}" )

            return
        flag += str(sol1) + ","
        flag2 += str(sol2) + ","
    print(flag)
    flag = flag[:-1]
    flag2 = flag2[:-1]
    import hashlib
    print(hashlib.md5(flag.encode()).hexdigest())    
    print(hashlib.md5(flag2.encode()).hexdigest())  
    
if __name__ == "__main__":
    main()

