
def get_longest_alternating_subsequence(string):
    # Initialize variables
    longest_sequence = 0
    current_sequence = 0
    previous_character = string[0]

    # Iterate through the string
    for character in string:
        # If the current character is different from the previous character, start a new sequence
        if character != previous_character:
            current_sequence += 1
        # If the current character is the same as the previous character, end the current sequence
        else:
            current_sequence = 0
        # Update the longest sequence if necessary
        longest_sequence = max(longest_sequence, current_sequence)
        # Update the previous character
        previous_character = character

    # Return the longest sequence
    return longest_sequence

def get_flipped_string(string):
    # Initialize variables
    flipped_string = ""
    flipped_character = "0"

    # Iterate through the string
    for character in string:
        # Flip the character
        if character == "0":
            flipped_character = "1"
        else:
            flipped_character = "0"
        # Add the flipped character to the flipped string
        flipped_string += flipped_character

    # Return the flipped string
    return flipped_string

def get_longest_alternating_subsequence_after_flipping(string):
    # Get the flipped string
    flipped_string = get_flipped_string(string)
    # Get the longest alternating subsequence of the flipped string
    longest_sequence = get_longest_alternating_subsequence(flipped_string)
    # Return the length of the longest sequence
    return longest_sequence

if __name__ == '__main__':
    # Get the number of questions
    n = int(input())
    # Get the binary string
    string = input()
    # Get the longest alternating subsequence after flipping a substring
    longest_sequence = get_longest_alternating_subsequence_after_flipping(string)
    # Print the result
    print(longest_sequence)

