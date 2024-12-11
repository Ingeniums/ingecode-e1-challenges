# Mapping of characters to their respective key sequences on a Nokia 3310 keyboard.
KEYPAD = {
    'a': '2', 'b': '22', 'c': '222',
    'd': '3', 'e': '33', 'f': '333',
    'g': '4', 'h': '44', 'i': '444',
    'j': '5', 'k': '55', 'l': '555',
    'm': '6', 'n': '66', 'o': '666',
    'p': '7', 'q': '77', 'r': '777', 's': '7777',
    't': '8', 'u': '88', 'v': '888',
    'w': '9', 'x': '99', 'y': '999', 'z': '9999',
    ' ': '0'  # Space is mapped to 0
}

def word_to_sequence(word):
    """Converts a word into its corresponding key sequence."""
    sequence = ''
    for char in word:
        if char.lower() in KEYPAD:
            sequence += KEYPAD[char.lower()]
    return sequence

def generate_test_cases(sentence, filename):
    """Generates test cases from a sentence and writes them to a file."""
    words = sentence.split()
    with open(filename, 'w') as file:
        for word in words:
            sequence = word_to_sequence(word)
            file.write(sequence + '\n')

# Sentence to convert.
sentence = "the nokia three three ten is not just a phone you can use it as a tank shell and it ll probably stay intact"

# Output file name.
output_file = "test_cases.txt"

# Generate and write test cases to the file.
generate_test_cases(sentence, output_file)

print(f"Test cases written to {output_file}")
