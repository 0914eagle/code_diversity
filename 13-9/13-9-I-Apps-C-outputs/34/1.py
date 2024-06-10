
def get_longest_repeated_substring(input_string):
    # Initialize variables
    longest_substring = ""
    current_substring = ""
    substring_length = 0
    
    # Iterate through the input string
    for i in range(len(input_string)):
        # Check if the current character is already in the current substring
        if input_string[i] in current_substring:
            # If it is, update the longest substring and reset the current substring
            if len(current_substring) > len(longest_substring):
                longest_substring = current_substring
            current_substring = ""
        # If the current character is not in the current substring, add it to the current substring
        else:
            current_substring += input_string[i]
    
    # If the current substring is longer than the longest substring, update the longest substring
    if len(current_substring) > len(longest_substring):
        longest_substring = current_substring
    
    return longest_substring

def main():
    input_string = input()
    longest_repeated_substring = get_longest_repeated_substring(input_string)
    print(longest_repeated_substring)

if __name__ == '__main__':
    main()

