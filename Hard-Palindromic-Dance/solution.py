def get_input(file=__file__.replace('/solution.py','')+'/input.txt'):
    with open(file, 'r') as f:
        cases = f.read().strip().split('\n')
        cases = cases[1:]
        return cases
   

def count_palindromic_subsequences(s):
    n = len(s)
    dp = [[set() for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        dp[i][i].add(s[i])  
    
    for length in range(2, n + 1):  
        for i in range(n - length + 1):  
            j = i + length - 1  
            
            dp[i][j] = dp[i+1][j] | dp[i][j-1]
            
            if s[i] == s[j]:
                dp[i][j].add(s[i] + s[j])  
                dp[i][j].update({s[i] + mid + s[j] for mid in dp[i+1][j-1]})
    return len(dp[0][n-1])

def main():
    test_cases = get_input()
    flag = ""
    for case in test_cases:
        flag += str(count_palindromic_subsequences(case)) +","
        
    flag = flag[:-1]
    print(flag)
    #md5 hash the string
    import hashlib
    print(hashlib.md5(flag.encode()).hexdigest())



if __name__ == '__main__':
    main()
