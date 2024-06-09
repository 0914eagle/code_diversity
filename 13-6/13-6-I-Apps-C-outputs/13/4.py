
def longest_repeated_substring(input_string):
    # Initialize variables
    start_index = 0
    end_index = 0
    longest_substring = ""

    # Iterate through the input string
    for i in range(len(input_string)):
        # Check if the substring starting at position i is a repeated substring
        if input_string[i:].startswith(input_string[:i]):
            # If it is, update the longest substring and its indices
            longest_substring = input_string[:i]
            start_index = i - len(longest_substring) + 1
            end_index = i

    # Return the longest repeated substring
    return longest_substring[start_index:end_index+1]

