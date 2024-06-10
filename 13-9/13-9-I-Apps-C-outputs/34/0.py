
def get_longest_repeated_substring(input_string):
    # Initialize variables
    longest_substring = ""
    current_substring = ""
    substring_map = {}

    # Iterate through the input string
    for char in input_string:
        # If the current character is already in the substring map,
        # it means we have found the start of a repeated substring
        if char in substring_map:
            # Update the current substring with the previous characters
            current_substring = current_substring + char

            # If the current substring is longer than the longest substring,
            # update the longest substring
            if len(current_substring) > len(longest_substring):
                longest_substring = current_substring

            # Remove the character from the substring map
            del substring_map[char]
        else:
            # If the current character is not in the substring map,
            # add it to the map and update the current substring
            substring_map[char] = 1
            current_substring = current_substring + char

    # Return the longest substring
    return longest_substring

def main():
    # Read the input string
    input_string = input()

    # Call the function to get the longest repeated substring
    longest_substring = get_longest_repeated_substring(input_string)

    # Print the longest substring
    print(longest_substring)

if __name__ == '__main__':
    main()

