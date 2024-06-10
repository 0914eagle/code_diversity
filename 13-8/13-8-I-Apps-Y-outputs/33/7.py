
def longest_acgt_substring(s):
    # Initialize variables
    max_length = 0
    current_length = 0
    start_index = 0
    
    # Iterate through the string
    for i in range(len(s)):
        # If the current character is A, C, G, or T, increase the current length
        if s[i] in ["A", "C", "G", "T"]:
            current_length += 1
        # If the current character is not A, C, G, or T, or if we have reached the end of the string, check if the current length is greater than the maximum length
        else:
            if current_length > max_length:
                max_length = current_length
                start_index = i - current_length
            current_length = 0
    
    # If the string ends with an ACGT string, check if the current length is greater than the maximum length
    if current_length > max_length:
        max_length = current_length
        start_index = len(s) - current_length
    
    # Return the length of the longest ACGT string
    return max_length

def main():
    s = input()
    print(longest_acgt_substring(s))

if __name__ == '__main__':
    main()

