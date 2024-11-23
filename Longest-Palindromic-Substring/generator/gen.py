import random
import string


def generate_random_string(n: int) -> str:
    n = max(n, 10)  
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(n))


def generate_palindrome(n: int) -> str:
    n = max(n, 10) 
    half_length = n // 2
    first_half = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(half_length))
    middle = ''
    if n % 2 != 0:
        middle = random.choice(string.ascii_letters + string.digits + string.punctuation)
    second_half = first_half[::-1]

    return first_half + middle + second_half

def generate_test_cases(num_cases: int = 4000, palindromes_needed: int = 1000, max_length: int = 1000) -> str:
    result = []
    
    for _ in range(palindromes_needed):
        length = random.randint(10, max_length)  
        palindrome = generate_palindrome(length)
        result.append(palindrome)
    remaining_cases = num_cases - palindromes_needed
    for _ in range(remaining_cases):
        length = random.randint(10, max_length)  
        random_string = generate_random_string(length)
        result.append(random_string)

    concatenated_result = ','.join(result)
    
    return concatenated_result

test_cases = generate_test_cases(4000, 1000, 1000)

with open("test_cases.txt", "w") as file:
    file.write(test_cases)

print("Test cases have been written to 'test_cases.txt'.")
