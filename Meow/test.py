def generate_test_cases(file_name="test_cases.txt", num_cases=20, max_milk=20000, max_cats=200, max_distance=3000):
    import random

    with open(file_name, "w") as f:
        f.write(f"{num_cases}\n")  

        for _ in range(num_cases):
            M = random.randint(1, max_milk)
            C = random.randint(1, max_cats)
            f.write(f"{M} {C}\n") 

            for i in range(C):
                for j in range(i + 1, C):
                    D = random.randint(1, max_distance)
                    f.write(f"{i} {j} {D}\n")  

generate_test_cases()