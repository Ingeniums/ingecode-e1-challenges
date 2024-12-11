def solve_challenge(file_name="test_cases.txt"):
    import heapq

    def can_feed_cats(M, C, distances):
        # Use Prim's algorithm to find the minimum walking distance while satisfying distancing
        adjacency_list = {i: [] for i in range(C)}
        for i, j, D in distances:
            adjacency_list[i].append((D, j))
            adjacency_list[j].append((D, i))

        # cat 0 (fridge location)
        visited = set()
        min_heap = [(0, 0)]  # (distance, cat_index)
        total_distance = 0

        while min_heap and len(visited) < C:
            dist, cat = heapq.heappop(min_heap)
            if cat in visited:
                continue
            visited.add(cat)
            total_distance += dist

            for next_dist, next_cat in adjacency_list[cat]:
                if next_cat not in visited:
                    heapq.heappush(min_heap, (next_dist, next_cat))

        # If we can't visit all cats, return False
        if len(visited) < C:
            return False

        # Total milk requirement = C (1 ml per cat) + Spillage (2 * total_distance ml)
        milk_needed = C + 2 * total_distance
        return M >= milk_needed

    results = []

    with open(file_name, "r") as f:
        T = int(f.readline().strip())  

        for _ in range(T):
            M, C = map(int, f.readline().strip().split())  

            distances = []
            for _ in range(C * (C - 1) // 2):
                i, j, D = map(int, f.readline().strip().split())
                distances.append((i, j, D))

            results.append("yes" if can_feed_cats(M, C, distances) else "no")

    flag = "".join(results)
    print(flag)

solve_challenge()
