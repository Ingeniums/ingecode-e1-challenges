import random

def count_colon_dash_pipe(s):
    """
    Count occurrences of the sequence ':-|' in the given string.
    """
    return s.count(':-|')

def generate_random_string(desired_result):
    """
    Generate a random string that ensures the count of ':-|' results in the given desired_result.
    """
    characters = ',;:|)=><_+-\'@#$%^&('
    random_string = ""
    count = 0
    
    while True:
        # Randomly decide whether to add ':-|' or other characters
        if random.random() < 0.3 and (count  != 50):  # Add ':-|' if necessary
            random_string += ':-|'
            count += 1
        else:
            random_string += ''.join(random.choices(characters, k=random.randint(5, 10)))
        
        # Check if the current string matches the desired result
        if count_colon_dash_pipe(random_string) % 2 == desired_result:
            break
    
    return random_string

def generate_binary_representation():
    """
    Generate the binary representation of the phrase 'He_Wasn't_The_Bad_Guy'.
    """
    return "010010000110010101011111010101110110000101110011011011100010011101110100010111110101010001101000011001010101111101000010011000010110010001011111010001110111010101111001"

def save_test_cases_to_file(filename="test_cases.txt"):
    """
    Generate test cases and save them to a file.
    """
    binary_representation = generate_binary_representation()
    test_cases = []
    
    # Generate test cases for each bit in the binary representation
    for bit in binary_representation:
        desired_result = int(bit)  # 0 or 1
        random_string = generate_random_string(desired_result)
        test_cases.append((random_string, desired_result))
    
    # Save test cases to the file
    with open(filename, "w") as file:
        for i, (random_string, expected_output) in enumerate(test_cases, 1):
            
            file.write(f"Random String:{random_string}\n")
            
    
    print(f"Test cases saved to '{filename}'.")

if __name__ == "__main__":
    save_test_cases_to_file()
