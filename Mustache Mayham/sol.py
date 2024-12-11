def solve_challenge(filename):
   
    final_binary = ""
    
    with open(filename, "r") as file:
        for line in file:
            if line.startswith("Random String:"):
                
                random_string = line.split("Random String:")[1].strip()
                count = random_string.count(":-|")
                final_binary += str(count % 2)  
    
    print(f"Final Binary Code: {final_binary}")
    return final_binary

if __name__ == "__main__":
    solve_challenge("test_cases.txt")
