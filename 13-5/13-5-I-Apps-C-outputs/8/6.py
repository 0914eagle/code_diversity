
def get_longest_alternating_subsequence(string):
    # Initialize variables
    longest_subsequence = 0
    current_subsequence = 0
    previous_character = string[0]

    # Iterate through the string
    for character in string:
        # If the current character is different from the previous character, start a new subsequence
        if character != previous_character:
            current_subsequence += 1
        # If the current character is the same as the previous character, end the current subsequence
        else:
            longest_subsequence = max(longest_subsequence, current_subsequence)
            current_subsequence = 0
        previous_character = character

    # Return the longest subsequence
    return longest_subsequence

def get_flipped_string(string):
    # Initialize variables
    flipped_string = ""
    previous_character = string[0]

    # Iterate through the string
    for character in string:
        # If the current character is different from the previous character, flip it
        if character != previous_character:
            flipped_string += "1" if character == "0" else "0"
        # If the current character is the same as the previous character, keep it as is
        else:
            flipped_string += character
        previous_character = character

    # Return the flipped string
    return flipped_string

def get_flipped_string_length(string):
    # Get the flipped string
    flipped_string = get_flipped_string(string)

    # Get the length of the flipped string
    flipped_string_length = len(flipped_string)

    # Return the length of the flipped string
    return flipped_string_length

def get_longest_alternating_subsequence_after_flipping(string):
    # Get the flipped string
    flipped_string = get_flipped_string(string)

    # Get the length of the flipped string
    flipped_string_length = get_flipped_string_length(string)

    # Get the longest alternating subsequence of the flipped string
    longest_alternating_subsequence = get_longest_alternating_subsequence(flipped_string)

    # Return the length of the longest alternating subsequence of the flipped string
    return longest_alternating_subsequence

if __name__ == '__main__':
    # Get the number of questions
    n = int(input())

    # Get Kevin's results on the USAICO
    results = input()

    # Get the length of the longest alternating subsequence of Kevin's string after flipping a single substring
    longest_alternating_subsequence = get_longest_alternating_subsequence_after_flipping(results)

    # Print the length of the longest alternating subsequence
    print(longest_alternating_subsequence)

