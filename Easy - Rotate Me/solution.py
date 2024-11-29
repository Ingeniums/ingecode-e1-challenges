

def get_input(file='Easy - Rotate Me/input.txt'):
    with open(file, 'r') as f:
        nums = f.read().strip().split(',')
        return [int(num) for num in nums]
    

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_rotatable_prime(n):
    s = str(n)
    rotations = [int(s[i:] + s[:i]) for i in range(len(s))]
    return "YES" if all(is_prime(rot) for rot in rotations) else "NO"

def main():
    test_cases = get_input()
    flag = ""
    for case in test_cases:
        flag += is_rotatable_prime(case) +","
    flag = flag[:-1]
    print(flag)
    #md5 hash the string
    import hashlib
    print(hashlib.md5(flag.encode()).hexdigest())



if __name__ == '__main__':
    main()