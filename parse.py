
import yaml
import os

for f in os.walk('.'):
    if (len(f[1]) == 0): 
        y = f[0]
        for c in f[2]:
            if (c.endswith('.yml')):
                y += "/"+c       
                break 
        
        var = yaml.safe_load(open(y, 'r'))
        print(var) 