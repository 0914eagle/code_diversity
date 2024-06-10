
def find_longest_acgt_substring(s):
    # Initialize variables
    longest_substring = ""
    current_substring = ""
    
    # Iterate through the characters of the input string
    for char in s:
        # If the current character is A, C, G, or T, add it to the current substring
        if char in "ACGT":
            current_substring += char
        # If the current character is not A, C, G, or T, check if the current substring is longer than the longest substring found so far
        else:
            if len(current_substring) > len(longest_substring):
                longest_substring = current_substring
            # Reset the current substring to an empty string
            current_substring = ""
    
    # Check if the last substring is longer than the longest substring found so far
    if len(current_substring) > len(longest_substring):
        longest_substring = current_substring
    
    # Return the length of the longest substring
    return len(longest_substring)

def main():
    s = input()
    print(find_longest_acgt_substring(s))

if __name__ == '__main__':
    main()

