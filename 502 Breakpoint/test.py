import random

def generate_random_pit_stop_times():
    refuel_time = random.randint(20, 50)
    tire_change_time = random.randint(40, 70)
    driver_rest_time = random.randint(90, 120)
    
    refuel_tire_time = refuel_time + tire_change_time - random.randint(5,10)
    refuel_rest_time = refuel_time + driver_rest_time - random.randint(10,20)
    tire_rest_time = tire_change_time + driver_rest_time -  random.randint(10,20)
    refuel_tire_rest_time = refuel_time + tire_change_time + driver_rest_time - random.randint(20,50)
    
    return {
        'refuel': refuel_time,
        'tire_change': tire_change_time,
        'driver_rest': driver_rest_time,
        'refuel_tire': refuel_tire_time,
        'refuel_rest': refuel_rest_time,
        'tire_rest': tire_rest_time,
        'refuel_tire_rest': refuel_tire_rest_time
    }

def generate_test_case():
    num_laps = random.randint(5, 20)
    
    max_fuel_laps = random.randint(4, 7)
    max_tire_laps = random.randint(3, 6)
    max_driver_laps = random.randint(5, 8)
    
    pit_stop_times = generate_random_pit_stop_times()
    
    lap_times = [random.randint(80, 100) for _ in range(num_laps)]
    
    test_case = f"{num_laps} {max_fuel_laps} {max_tire_laps} {max_driver_laps} " \
                f"{pit_stop_times['refuel']} {pit_stop_times['tire_change']} {pit_stop_times['driver_rest']} " \
                f"{pit_stop_times['refuel_tire']} {pit_stop_times['refuel_rest']} {pit_stop_times['tire_rest']} {pit_stop_times['refuel_tire_rest']}\n" \
                + " ".join(map(str, lap_times)) + "\n"
    
    return test_case

def generate_multiple_test_cases(num_cases=5):
    test_cases = []
    for _ in range(num_cases):
        test_cases.append(generate_test_case())
    
    return test_cases

def save_test_cases(filename="test_cases.txt", num_cases=5):
    test_cases = generate_multiple_test_cases(num_cases)
    with open(filename, "w") as f:
        f.write(str(num_cases) + "\n")
        f.writelines(test_cases)

save_test_cases("test_cases.txt", 10000)
