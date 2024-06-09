
def is_possible_to_win(sequence):
    # Initialize variables
    n = len(sequence)
    i = 0
    j = n - 1
    count = 0
    beautiful_word = ""

    # Iterate through the sequence
    while i < j:
        # Check if the current letter is the rightmost remaining letter
        if sequence[j] == sequence[n - 1]:
            # Add the letter to the beautiful word
            beautiful_word += sequence[j]
            # Remove the letter from the sequence
            sequence = sequence[:j] + sequence[j + 1:]
            # Increment the count
            count += 1

        # Move to the next letter
        i += 1
        j -= 1

    # Check if it is possible for Slavko to win
    if count % 2 == 0:
        return "NE", ""
    else:
        return "DA", beautiful_word

# Main function
if __name__ == "__main__":
    # Read the input
    n = int(input())
    sequence = input()

    # Call the function to check if it is possible for Slavko to win
    result = is_possible_to_win(sequence)

    # Print the output
    print(result[0])
    print(result[1])

