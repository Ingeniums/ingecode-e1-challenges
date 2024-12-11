from itertools import combinations

def calculate_race_time(laps, F, T, D, pit_stop_times):
    n = len(laps)
    
    # To store the best time and pit stop sequence
    best_time = float('inf')
    best_stops = []
    
    # Recursive helper function to evaluate all combinations
    def dfs(current_lap, current_time, fuel_left, tires_left, stamina_left, pit_stops):
        nonlocal best_time, best_stops

        # If all laps are completed, check if this is the best time
        if current_lap == n:
            if current_time < best_time:
                best_time = current_time
                best_stops = pit_stops[:]
            return

        # Add the current lap's time
        lap_time = laps[current_lap]

        # Case 1: No pit stop, check constraints
        if fuel_left > 0 and tires_left > 0 and stamina_left > 0:
            dfs(current_lap + 1, current_time + lap_time, 
                fuel_left - 1, tires_left - 1, stamina_left - 1, pit_stops)

        # Case 2: Perform a pit stop (try all valid pit stops)
        # Refuel only
        if fuel_left <= 0:
            dfs(current_lap + 1, current_time + lap_time + pit_stop_times[0], 
                F - 1, tires_left - 1, stamina_left - 1, 
                pit_stops + [(current_lap + 1, "Refuel")])
        
        # Tire change only
        if tires_left <= 0:
            dfs(current_lap + 1, current_time + lap_time + pit_stop_times[1], 
                fuel_left - 1, T - 1, stamina_left - 1, 
                pit_stops + [(current_lap + 1, "Tire Change")])
        
        # Driver rest only
        if stamina_left <= 0:
            dfs(current_lap + 1, current_time + lap_time + pit_stop_times[2], 
                fuel_left - 1, tires_left - 1, D - 1, 
                pit_stops + [(current_lap + 1, "Driver Rest")])
        
        # Refuel + Tire Change
        if fuel_left <= 0 or tires_left <= 0:
            dfs(current_lap + 1, current_time + lap_time + pit_stop_times[3], 
                F - 1, T - 1, stamina_left - 1, 
                pit_stops + [(current_lap + 1, "Refuel + Tire Change")])
        
        # Refuel + Driver Rest
        if fuel_left <= 0 or stamina_left <= 0:
            dfs(current_lap + 1, current_time + lap_time + pit_stop_times[4], 
                F - 1, tires_left - 1, D - 1, 
                pit_stops + [(current_lap + 1, "Refuel + Driver Rest")])
        
        # Tire Change + Driver Rest
        if tires_left <= 0 or stamina_left <= 0:
            dfs(current_lap + 1, current_time + lap_time + pit_stop_times[5], 
                fuel_left - 1, T - 1, D - 1, 
                pit_stops + [(current_lap + 1, "Tire Change + Driver Rest")])
        
        # Refuel + Tire Change + Driver Rest
        if fuel_left <= 0 or tires_left <= 0 or stamina_left <= 0:
            dfs(current_lap + 1, current_time + lap_time + pit_stop_times[6], 
                F - 1, T - 1, D - 1, 
                pit_stops + [(current_lap + 1, "Refuel + Tire Change + Driver Rest")])

    # Start DFS with initial conditions
    dfs(0, 0, F, T, D, [])
    
    return best_time, best_stops

# Test the function
laps = [90, 85, 88, 92, 89, 91, 87, 93, 86, 90]
F = 5  # Maximum laps before fuel runs out
T = 4  # Maximum laps before tires wear out
D = 6  # Maximum laps before driver needs rest
pit_stop_times = [30, 50, 100, 70, 100, 120, 160]  # Pit stop times for different operations

result_time, result_stops = calculate_race_time(laps, F, T, D, pit_stop_times)
print(f"Minimum race time: {result_time}")
print("Pit stops made:")
for stop in result_stops:
    print(f"Lap {stop[0]}: {stop[1]}")
