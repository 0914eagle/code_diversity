
def longest_repeated_substring(input_string):
    # Initialize variables
    start_index = 0
    end_index = 0
    longest_substring = ""

    # Iterate through the input string
    for i in range(len(input_string)):
        # Check if the substring starting at index i is a repetition of a previous substring
        for j in range(i + 1, len(input_string)):
            # If the substring is a repetition, update the longest substring and its indices
            if input_string[i:j] == input_string[i - 1:j - 1]:
                start_index = i
                end_index = j
                longest_substring = input_string[i:j]
                break

    # Return the longest substring
    return longest_substring

