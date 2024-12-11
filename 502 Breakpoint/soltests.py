import hashlib

def calculate_race_time(laps, F, T, D, pit_stop_times):
    n = len(laps)
    
    # To store the best time and pit stop sequence
    best_time = float('inf')
    
    # Recursive helper function to evaluate all combinations
    def dfs(current_lap, current_time, fuel_left, tires_left, stamina_left):
        nonlocal best_time

        # If all laps are completed, check if this is the best time
        if current_lap == n:
            if current_time < best_time:
                best_time = current_time
            return

        # Add the current lap's time
        lap_time = laps[current_lap]

        # Case 1: No pit stop, check constraints
        if fuel_left > 0 and tires_left > 0 and stamina_left > 0:
            dfs(current_lap + 1, current_time + lap_time, 
                fuel_left - 1, tires_left - 1, stamina_left - 1)

        # Case 2: Perform a pit stop (try all valid pit stops)
        # Refuel only
        if fuel_left <= 0:
            dfs(current_lap + 1, current_time + lap_time + pit_stop_times[0], 
                F - 1, tires_left - 1, stamina_left - 1)
        
        # Tire change only
        if tires_left <= 0:
            dfs(current_lap + 1, current_time + lap_time + pit_stop_times[1], 
                fuel_left - 1, T - 1, stamina_left - 1)
        
        # Driver rest only
        if stamina_left <= 0:
            dfs(current_lap + 1, current_time + lap_time + pit_stop_times[2], 
                fuel_left - 1, tires_left - 1, D - 1)
        
        # Refuel + Tire Change
        if fuel_left <= 0 or tires_left <= 0:
            dfs(current_lap + 1, current_time + lap_time + pit_stop_times[3], 
                F - 1, T - 1, stamina_left - 1)
        
        # Refuel + Driver Rest
        if fuel_left <= 0 or stamina_left <= 0:
            dfs(current_lap + 1, current_time + lap_time + pit_stop_times[4], 
                F - 1, tires_left - 1, D - 1)
        
        # Tire Change + Driver Rest
        if tires_left <= 0 or stamina_left <= 0:
            dfs(current_lap + 1, current_time + lap_time + pit_stop_times[5], 
                fuel_left - 1, T - 1, D - 1)
        
        # Refuel + Tire Change + Driver Rest
        if fuel_left <= 0 or tires_left <= 0 or stamina_left <= 0:
            dfs(current_lap + 1, current_time + lap_time + pit_stop_times[6], 
                F - 1, T - 1, D - 1)

    # Start DFS with initial conditions
    dfs(0, 0, F, T, D)
    
    return best_time

def read_test_cases(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    
    num_cases = int(lines[0].strip())
    test_cases = []
    idx = 1
    
    for _ in range(num_cases):
        params = list(map(int, lines[idx].strip().split()))
        laps = list(map(int, lines[idx + 1].strip().split()))
        idx += 2
        test_cases.append((params, laps))
    
    return test_cases

def compute_hash_for_test_cases(test_cases):
    concatenated_results = ""
    
    for params, laps in test_cases:
        num_laps, F, T, D, *pit_stop_times = params
        min_race_time = calculate_race_time(laps, F, T, D, pit_stop_times)
        concatenated_results += str(min_race_time)
    
    # Compute MD5 hash of the concatenated results
    hash_result = hashlib.md5(concatenated_results.encode()).hexdigest()
    return hash_result

# Main execution
test_cases = read_test_cases("test_cases.txt")
hash_result = compute_hash_for_test_cases(test_cases)

print(f"MD5 Hash of the concatenated minimum race times: {hash_result}")
