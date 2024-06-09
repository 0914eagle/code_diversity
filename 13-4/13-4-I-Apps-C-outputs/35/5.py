
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

            # If the current substring is longer than the longest substring found so far,
            # update the longest substring
            if len(current_substring) > len(longest_substring):
                longest_substring = current_substring
        else:
            # If the current character is not in the substring map,
            # it means we have found the start of a new substring
            current_substring = char
            substring_map[char] = 1

    # Return the longest substring
    return longest_substring

def main():
    input_string = input("Enter a string of lowercase letters: ")
    longest_substring = longest_repeated_substring(input_string)
    print(f"The longest repeated substring is: {longest_substring}")

if __name__ == '__main__':
    main()

