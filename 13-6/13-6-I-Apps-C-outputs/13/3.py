
def longest_repeated_substring(input_string):
    # Initialize variables
    start_index = 0
    end_index = 0
    longest_substring = ""

    # Iterate over the input string
    for i in range(len(input_string)):
        # Check if the substring starting at position i is a repeated substring
        if input_string[i] in input_string[start_index:i]:
            # If it is, update the start index and end index of the longest substring
            start_index = input_string.index(input_string[i], start_index)
            end_index = i
        # If it's not, update the start index
        else:
            start_index = i + 1

        # Update the longest substring if necessary
        if len(longest_substring) < end_index - start_index + 1:
            longest_substring = input_string[start_index:end_index + 1]

    return longest_substring

