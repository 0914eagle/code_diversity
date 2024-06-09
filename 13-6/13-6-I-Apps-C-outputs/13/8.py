
def longest_repeated_substring(input_string):
    # Initialize variables
    longest_substring = ""
    current_substring = ""
    substring_map = {}

    # Iterate through the input string
    for char in input_string:
        # If the current character is already in the substring map,
        # update the longest substring and reset the current substring
        if char in substring_map:
            longest_substring = max(longest_substring, current_substring, key=len)
            current_substring = ""

        # Add the current character to the current substring
        current_substring += char
        substring_map[char] = 1

    # After iterating through the entire input string,
    # update the longest substring and return it
    longest_substring = max(longest_substring, current_substring, key=len)
    return longest_substring

