# Mapping of sequences to characters for a Nokia 3310 keyboard.
SEQUENCE_TO_CHAR = {
    '2': 'a', '22': 'b', '222': 'c',
    '3': 'd', '33': 'e', '333': 'f',
    '4': 'g', '44': 'h', '444': 'i',
    '5': 'j', '55': 'k', '555': 'l',
    '6': 'm', '66': 'n', '666': 'o',
    '7': 'p', '77': 'q', '777': 'r', '7777': 's',
    '8': 't', '88': 'u', '888': 'v',
    '9': 'w', '99': 'x', '999': 'y', '9999': 'z',
    '0': ' '  # Space is mapped to 0
}

def sequence_to_word(sequence):
    """Converts a sequence of numbers into the corresponding word."""
    result = ''
    buffer = ''
    for char in sequence:
        if buffer and buffer[-1] != char:
            result += SEQUENCE_TO_CHAR.get(buffer, '')
            buffer = char
        else:
            buffer += char
    # Process the last buffer.
    result += SEQUENCE_TO_CHAR.get(buffer, '')
    return result

def convert_test_cases(filename):
    """Converts sequences in a file back to words."""
    with open(filename, 'r') as file:
        sequences = file.readlines()
    words = [sequence_to_word(seq.strip()) for seq in sequences]
    return words

# Input file name.
input_file = "test_cases.txt"

# Convert the sequences and print the results.
converted_words = convert_test_cases(input_file)
print("Converted words:")
print(' '.join(converted_words))
