import random 

# generate test cases for fractional knapsack problem

cases = []
limit = 700
for i in range(limit):
    n = random.randint(150, 400)
    m = random.randint(150, 400)
    rows = [[random.randint(1,90) for _ in range (m)] for i in range(n)]
    cases.append(rows)
with open(__file__.replace(__file__.split('/')[-1], '') +'input.txt', 'w') as f:
    f.write(str(len(cases))+"\n")
    for cas in cases:
            
        f.write(f'{len(cas)} {len(cas[0])}\n')
        for row in cas:
            f.write(' '.join(map(str, row)) + '\n')
