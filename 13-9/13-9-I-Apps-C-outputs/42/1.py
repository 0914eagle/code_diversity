
def get_sequence(oranges, apples):
    # Initialize the sequence with 'A' and 'B'
    sequence = 'AB'
    # Loop until the fruit is gone
    while oranges > 0 or apples > 0:
        # If there are still oranges, add an 'A' to the sequence
        if oranges > 0:
            sequence += 'A'
            oranges -= 1
        # If there are still apples, add a 'B' to the sequence
        if apples > 0:
            sequence += 'B'
            apples -= 1
    return sequence

def get_compressed_sequence(oranges, apples):
    # Get the sequence of cards
    sequence = get_sequence(oranges, apples)
    # Initialize the compressed sequence
    compressed_sequence = ''
    # Loop through the sequence
    for i in range(len(sequence)):
        # If the current character is the same as the previous character
        if i > 0 and sequence[i] == sequence[i-1]:
            # Increment the count of the current character
            count = compressed_sequence[-1] + 1
            # Update the compressed sequence
            compressed_sequence = compressed_sequence[:-1] + str(count) + sequence[i]
        # If the current character is different from the previous character
        else:
            # Add the current character to the compressed sequence
            compressed_sequence += sequence[i]
    return compressed_sequence

def main():
    oranges, apples = map(int, input().split())
    sequence = get_compressed_sequence(oranges, apples)
    print(sequence)

if __name__ == '__main__':
    main()

