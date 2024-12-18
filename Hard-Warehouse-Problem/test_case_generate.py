import random 

# generate test cases for fractional knapsack problem

cases = []
limit = 3000
for i in range(limit):
    n = random.randint(1,100)
    w = random.randint(1,10000)
    weights = [random.randint(1,10000) for _ in range(n)]
    values = [random.randint(1,10000) for _ in range(n)]
    cases.append((n,w,weights,values))
with open(__file__.replace(__file__.split('/')[-1], '') +'input.txt', 'w') as f:
    for cas in cases:
            
        f.write(f'{cas[0]} {cas[1]}\n')
        f.write(' '.join(map(str, cas[2])) + '\n')
        f.write(' '.join(map(str, cas[3])) + '\n')
