import hashlib


def longest_palindromic_substring(s: str) -> str:
    n = len(s)
    if n == 0:
        return ""
    
    start, maxLength = 0, 1

    for i in range(n):
        l, r = i, i
        while l >= 0 and r < n and s[l] == s[r]:
            if r - l + 1 > maxLength:
                start = l
                maxLength = r - l + 1
            l -= 1
            r += 1
        l, r = i, i + 1
        while l >= 0 and r < n and s[l] == s[r]:
            if r - l + 1 > maxLength:
                start = l
                maxLength = r - l + 1
            l -= 1
            r += 1
    
    return s[start:start + maxLength]


with open('test_cases.txt', 'r') as file:
    test_cases = file.read().strip().split(',')


results = []


for test_case in test_cases:
    result = longest_palindromic_substring(test_case)
    results.append(result)

concatenated_result = ''.join(results)

hashed_result = hashlib.sha256(concatenated_result.encode('utf-8')).hexdigest()

# Print the flag
flag = "INGECODE{" + hashed_result + "}"
print(flag)
