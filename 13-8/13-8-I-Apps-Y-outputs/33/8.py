
def get_longest_acgt_substring(s):
    # Initialize variables
    longest_acgt_substring = ""
    current_acgt_substring = ""
    
    # Iterate through the characters of the input string
    for char in s:
        # If the current character is A, C, G, or T, add it to the current ACGT substring
        if char in "ACGT":
            current_acgt_substring += char
        # If the current character is not A, C, G, or T, start a new ACGT substring
        else:
            if len(current_acgt_substring) > len(longest_acgt_substring):
                longest_acgt_substring = current_acgt_substring
            current_acgt_substring = ""
    
    # If the last ACGT substring is the longest, add it to the output
    if len(current_acgt_substring) > len(longest_acgt_substring):
        longest_acgt_substring = current_acgt_substring
    
    return len(longest_acgt_substring)

def main():
    s = input()
    print(get_longest_acgt_substring(s))

if __name__ == '__main__':
    main()

