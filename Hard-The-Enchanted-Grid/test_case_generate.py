import random
import numpy as np


random_indexes = set(np.random.randint(1,499, size=50))
limit = 100
min_limit = 4
cases = []
coord_limit = 15
for i in range (800):
    number_points = random.randint(min_limit,limit)
    
    points = []
    cas = str(number_points)+"\n"
    if (i in random_indexes):
        number_points= number_points-4
        # append two points that will form a square with other two
        point1 = [str(random.randint(0,coord_limit)), str(random.randint(0,coord_limit))]
        
        point2 = [str(random.randint(0,coord_limit)), str(random.randint(0,coord_limit))]
        while (point1 == point2):
            point2 = [str(random.randint(0,coord_limit)), str(random.randint(0,coord_limit))]
        print ("random index: " , point1 , point2)
        x1 = int(point1[0])
        x2 = int(point2[0])
        y1 = int(point1[1])
        y2 = int(point2[1])
        dx = x2 - x1
        dy = y2 - y1

        # Compute the other two points using ±90° rotation
        point3 = [str(x1 - dy), str(y1 + dx)]  # Clockwise
        point4 = [str(x2 - dy), str(y2 + dx)]
        print ("other poinnts: " , point3 , point4)
        
        points.append(point1)
        points.append(point2)
        points.append(point3)
        points.append(point4)
        cas += " ".join(point1) + "\n"
        cas += " ".join(point2) + "\n"
        cas += " ".join(point3) + "\n"
        cas += " ".join(point4) + "\n"
    
        print(number_points)
    for i in range(number_points):
        point = [str(random.randint(0,coord_limit)), str(random.randint(0,coord_limit))]
        while(point in points):
            point = [str(random.randint(0,coord_limit)), str(random.randint(0,coord_limit))]
        if ( point not in points ):
            points.append(point)
            cas += " ".join(point) + "\n"
    cases.append(cas)
        
f = open(__file__.replace(__file__.split('/')[-1], '') + 'input.txt', 'w')
f.write(''.join(cases))
f.close()
