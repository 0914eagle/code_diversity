
def find_longest_repeated_substring(input_string):
    # Initialize a dictionary to store the starting indices of each unique substring
    substring_indices = {}
    # Initialize the longest repeated substring as an empty string
    longest_repeated_substring = ""
    # Iterate over the characters of the input string
    for i in range(len(input_string)):
        # Check if the current substring is already in the dictionary
        if input_string[i] in substring_indices:
            # If it is, update the longest repeated substring if necessary
            if len(longest_repeated_substring) < i - substring_indices[input_string[i]] + 1:
                longest_repeated_substring = input_string[substring_indices[input_string[i]]:i+1]
        # If the current substring is not in the dictionary, add it to the dictionary with its starting index
        else:
            substring_indices[input_string[i]] = i
    # Return the longest repeated substring
    return longest_repeated_substring

def main():
    input_string = input()
    print(find_longest_repeated_substring(input_string))

if __name__ == '__main__':
    main()

