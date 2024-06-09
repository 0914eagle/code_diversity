
def longest_repeated_substring(input_string):
    # Initialize variables
    start_index = 0
    end_index = 0
    longest_substring = ""
    current_substring = ""

    # Iterate through the input string
    for i in range(len(input_string)):
        # Check if the current character is already in the current substring
        if input_string[i] in current_substring:
            # If it is, update the start index of the current substring
            start_index = current_substring.index(input_string[i]) + 1
            current_substring = current_substring[start_index:]
        # Add the current character to the current substring
        current_substring += input_string[i]
        # Check if the current substring is longer than the longest substring
        if len(current_substring) > len(longest_substring):
            longest_substring = current_substring
        # Check if the current substring is a repeated substring
        if current_substring in input_string[i+1:]:
            # If it is, update the end index of the longest substring
            end_index = i + 1 + input_string[i+1:].index(current_substring)
            longest_substring = input_string[start_index:end_index]
            break

    return longest_substring

