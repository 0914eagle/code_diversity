
def longest_repeated_substring(input_string):
    # Initialize variables
    start_index = 0
    end_index = 0
    longest_substring = ""

    # Iterate over the input string
    for i in range(len(input_string)):
        # Check if the substring starting from the current index is repeated
        if input_string[i:].startswith(input_string[:i]):
            # If it is repeated, update the longest substring and its indices
            longest_substring = input_string[:i]
            start_index = i
            end_index = start_index + len(longest_substring) - 1

    # Return the longest repeated substring
    return longest_substring

