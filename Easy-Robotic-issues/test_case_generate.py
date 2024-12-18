import random

alphabet = "UDLR"
limit = 100
cases = []
for i in range (2000):
    cas = ""
    print(f"case {i}")
    l = random.randint(3,limit)
    
    for i in range(l):
        cas += random.choice(alphabet)
    cases.append(cas)
        
f = open(__file__.replace(__file__.split('/')[-1], '') + 'input.txt', 'w')
f.write('\n'.join(cases))
f.close()
