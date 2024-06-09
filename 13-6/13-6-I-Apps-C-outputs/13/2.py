
def longest_repeated_substring(input_string):
    # Initialize variables
    longest_substring = ""
    current_substring = ""
    substring_map = {}

    # Iterate through the input string
    for char in input_string:
        # If the current character is already in the substring map,
        # it means we have found the start of a repeated substring
        if char in substring_map:
            # Update the current substring and substring map
            current_substring += char
            substring_map[char] += 1

            # If the current substring is longer than the longest substring,
            # update the longest substring
            if len(current_substring) > len(longest_substring):
                longest_substring = current_substring
        # If the current character is not in the substring map,
        # it means we have found the end of a repeated substring
        else:
            # Update the substring map and current substring
            substring_map[char] = 1
            current_substring = char

    # Return the longest substring
    return longest_substring

