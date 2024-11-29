import random

yes_cases = [2,3,5,7,11,13,17,31,37,71,73,79,97,113,131,197,199,311,337,373,719,733,919,971,991,1193,1931,3119,3779,7793,7937,9311,9377,11939,19391,19937,37199,39119,71993,91193,93719,93911,99371,193939,199933,319993,331999,391939,393919,919393,933199,939193,939391,993319,9993310]

no_cases = [str(random.randint(0, 10**5)) for _ in range(1950)]
# merge the results
for yes in yes_cases:
    ind = random.randint(0, len(no_cases))
    no_cases.insert(ind, str(yes))
f = open('input.txt', 'w')
f.write(','.join(no_cases))
f.close()
