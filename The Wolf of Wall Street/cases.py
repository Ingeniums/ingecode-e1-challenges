import random

def generate_test_cases(filename, num_cases, max_days, max_price):
    with open(filename, 'w') as file:
        file.write(f"{num_cases}\n")  
        for _ in range(num_cases):
            days = random.randint(max_days // 2, max_days)  
            prices = [random.randint(0, max_price) for _ in range(days)]
            file.write(f"{days}\n")
            file.write(" ".join(map(str, prices)) + "\n")

generate_test_cases('test_cases.txt', num_cases=1000, max_days=10000, max_price=100000)
