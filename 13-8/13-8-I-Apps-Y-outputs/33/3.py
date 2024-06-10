
def find_longest_acgt_substring(s):
    # Initialize variables
    longest_acgt_string = ""
    current_acgt_string = ""
    
    # Iterate through the string
    for char in s:
        # If the character is A, C, G, or T, add it to the current ACGT string
        if char in "ACGT":
            current_acgt_string += char
        # If the character is not A, C, G, or T, reset the current ACGT string
        else:
            current_acgt_string = ""
        
        # If the current ACGT string is longer than the longest ACGT string, update the longest ACGT string
        if len(current_acgt_string) > len(longest_acgt_string):
            longest_acgt_string = current_acgt_string
    
    # Return the length of the longest ACGT string
    return len(longest_acgt_string)

def main():
    s = input()
    print(find_longest_acgt_substring(s))

if __name__ == '__main__':
    main()

