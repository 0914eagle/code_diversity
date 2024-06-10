
def get_longest_repeated_substring(input_string):
    # Initialize a dictionary to store the length of each substring and its count
    substring_lengths = {}
    
    # Iterate through the input string
    for i in range(len(input_string)):
        # Get the substring starting from the current index and iterate through the remaining substring
        for j in range(i, len(input_string)):
            # Check if the substring is already in the dictionary
            if input_string[i:j+1] in substring_lengths:
                # If it is, increment its count
                substring_lengths[input_string[i:j+1]] += 1
            else:
                # If it's not, add it to the dictionary with a count of 1
                substring_lengths[input_string[i:j+1]] = 1
    
    # Find the longest repeated substring
    longest_substring = ""
    for substring, count in substring_lengths.items():
        if count > 1 and len(substring) > len(longest_substring):
            longest_substring = substring
    
    return longest_substring

def main():
    input_string = input()
    longest_repeated_substring = get_longest_repeated_substring(input_string)
    print(longest_repeated_substring)

if __name__ == '__main__':
    main()

