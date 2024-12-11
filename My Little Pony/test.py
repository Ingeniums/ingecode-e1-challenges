import random
import math

def generate_test_cases(file_name, num_cases):
    def generate_polygon(N):
        """Generate a strictly convex polygon with N vertices."""
        angles = sorted(random.uniform(0, 2 * math.pi) for _ in range(N))
        radius = random.randint(1, 1000)
        vertices = [(int(radius * math.cos(angle)), int(radius * math.sin(angle))) for angle in angles]
        return vertices

    with open(file_name, 'w') as f:
        for _ in range(num_cases):
            N = random.randint(3, 15) 
            K = random.randint(max(1, N - 10), N)  
            vertices = generate_polygon(N)
            f.write(f"{N} {K}\n")
            for x, y in vertices:
                f.write(f"{x} {y}\n")

if __name__ == "__main__":
    generate_test_cases("test_cases.txt", 10)
