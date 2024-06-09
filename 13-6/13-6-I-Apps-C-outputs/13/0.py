
def longest_repeated_substring(input_string):
    # Initialize variables
    longest_substring = ""
    current_substring = ""
    substring_start_index = 0
    substring_end_index = 0

    # Iterate through the input string
    for i in range(len(input_string)):
        # If the current character is already in the current substring, update the substring end index
        if input_string[i] in current_substring:
            substring_end_index = i
        # If the current substring is longer than the longest substring, update the longest substring
        if len(current_substring) > len(longest_substring):
            longest_substring = current_substring
        # Add the current character to the current substring
        current_substring += input_string[i]

    # If the current substring is longer than the longest substring, update the longest substring
    if len(current_substring) > len(longest_substring):
        longest_substring = current_substring

    # Return the longest substring
    return longest_substring

