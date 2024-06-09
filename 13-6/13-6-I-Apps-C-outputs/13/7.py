
def longest_repeated_substring(input_string):
    # Initialize variables
    longest_substring = ""
    current_substring = ""
    substring_start_index = 0
    substring_end_index = 0

    # Iterate through the input string
    for i in range(len(input_string)):
        # Check if the current character is already in the current substring
        if input_string[i] in current_substring:
            # If it is, update the substring end index
            substring_end_index = i
        else:
            # If it's not, add the current character to the current substring
            current_substring += input_string[i]
            # Check if the current substring is longer than the longest substring
            if len(current_substring) > len(longest_substring):
                # If it is, update the longest substring
                longest_substring = current_substring
            # Update the substring start index
            substring_start_index = i - len(current_substring) + 1
            # Reset the current substring
            current_substring = ""

    # Check if the last substring is longer than the longest substring
    if len(current_substring) > len(longest_substring):
        longest_substring = current_substring

    return longest_substring

