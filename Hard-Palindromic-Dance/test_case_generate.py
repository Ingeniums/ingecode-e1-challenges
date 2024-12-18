import random

from string import ascii_lowercase, digits


limit = 4000
alphabet = list(ascii_lowercase + digits)
limit_len = len( alphabet ) 
cases = []
for i in range(limit):
    random.shuffle(alphabet)
    s = random.sample(alphabet,random.randint(2,limit_len), counts=[random.randint(1,15) for _ in range(limit_len)])
    cases.append("".join(s))
f = open(__file__.replace(__file__.split('/')[-1], '') + 'input.txt', 'w')
f.write('\n'.join(cases))
f.close()
