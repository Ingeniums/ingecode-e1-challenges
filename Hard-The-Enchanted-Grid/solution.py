


def get_input(file=__file__.replace(__file__.split('/')[-1], '')+'input.txt'):
    cases = []
    with open(file, 'r') as f:
        #while not eof
        num_cases = int(f.readline())
        while True:
            n = f.readline()
            if n == "":
                break
            n = int(n)
            cas = []
            for i in range(n):
                l = tuple([int(x) for x in  f.readline().strip().split()])
                cas.append(l)
            cases.append(cas)
        return cases
    
def count_all_squares(points):
    point_set = set(points)  # Use a set for quick lookups
    square_count = 0

    # Iterate through all pairs of points
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            x1, y1 = points[i]
            x2, y2 = points[j]

            # sol 1: Treat the two points as a diagonal
            dx = x2 - x1
            dy = y2 - y1

            # Compute the other two points using ±90° rotation
            p3_diag = (x1 - dy, y1 + dx)  # Clockwise
            p4_diag = (x2 - dy, y2 + dx)  # Clockwise
            if p3_diag in point_set and p4_diag in point_set:
                square_count += 1

            # sol 2: Treat the two points as adjacent corners
            # mx, my = (x1 + x2) / 2, (y1 + y2) / 2  # Midpoint of the two points
            # hx, hy = (x2 - x1) / 2, (y2 - y1) / 2  # Half-vector between the points

            
            # p3_side = (mx - hy, my + hx)  # Clockwise rotation
            # p4_side = (mx + hy, my - hx)  # Counter-clockwise rotation
            # if p3_side in point_set and p4_side in point_set:
            #     square_count += 1

    return square_count // 2


def main ():
        
    cases = get_input()
    print(len(cases))
    flag= ""
    for cas in cases:
        flag += str(count_all_squares(cas))+","
    flag = flag[:-1]
    
    print(flag)
    
    import hashlib
    print(hashlib.md5(flag.encode()).hexdigest())    


if __name__ == "__main__":
    main()