from shapely.geometry import Polygon, Point
from itertools import combinations
import numpy as np

def point_in_triangle(pt, v1, v2, v3):
    x, y = pt
    x1, y1 = v1
    x2, y2 = v2
    x3, y3 = v3

    detT = (y2 - y3) * (x1 - x3) + (x3 - x2) * (y1 - y3)
    if detT == 0:
        return False 

    alpha = ((y2 - y3) * (x - x3) + (x3 - x2) * (y - y3)) / detT
    beta = ((y3 - y1) * (x - x3) + (x1 - x3) * (y - y3)) / detT
    gamma = 1 - alpha - beta

    return 0 < alpha < 1 and 0 < beta < 1 and 0 < gamma < 1

def generate_interior_points(vertices, num_points=1000):
    polygon = Polygon(vertices)
    minx, miny, maxx, maxy = polygon.bounds

    x_coords = np.linspace(minx, maxx, int(np.sqrt(num_points)))
    y_coords = np.linspace(miny, maxy, int(np.sqrt(num_points)))

    grid_points = [(x, y) for x in x_coords for y in y_coords if polygon.contains(Point(x, y))]
    return grid_points

def minimize_coverage(N, K, vertices):
    """Minimize coverage of interior points by selecting K vertices."""
    interior_points = generate_interior_points(vertices, num_points=500)
    best_indices = []
    min_covered = float('inf')

    # Start with a greedy approach: evenly spaced vertices
    step = max(1, N // K)
    initial_indices = [(i % N) for i in range(0, K * step, step)][:K]

    # Test initial selection
    current_indices = initial_indices
    covered_points = set()

    for tri in combinations(current_indices, 3):
        v1, v2, v3 = vertices[tri[0]], vertices[tri[1]], vertices[tri[2]]
        for pt in interior_points:
            if point_in_triangle(pt, v1, v2, v3):
                covered_points.add(pt)

    min_covered = len(covered_points)
    best_indices = current_indices

    # Attempt refinements by swapping vertices
    for candidate_indices in combinations(range(N), K):
        covered_points = set()
        for tri in combinations(candidate_indices, 3):
            v1, v2, v3 = vertices[tri[0]], vertices[tri[1]], vertices[tri[2]]
            for pt in interior_points:
                if point_in_triangle(pt, v1, v2, v3):
                    covered_points.add(pt)

        if len(covered_points) < min_covered:
            min_covered = len(covered_points)
            best_indices = candidate_indices

    return [i + 1 for i in best_indices]  # Convert to 1-based index

if __name__ == "__main__":
    with open("test_cases.txt", "r") as test_file:
        lines = test_file.readlines()

    results = []
    i = 0
    while i < len(lines):
        # Parse test case
        N, K = map(int, lines[i].split())
        i += 1
        vertices = []
        for _ in range(N):
            x, y = map(int, lines[i].split())
            vertices.append((x, y))
            i += 1

        # Solve the test case
        result = minimize_coverage(N, K, vertices)
        results.append(" ".join(map(str, result)))

    # Write results to a file
    with open("results.txt", "w") as result_file:
        result_file.write(" ".join(results))
