
def longest_acgt_substring(s):
    # Initialize variables
    max_length = 0
    current_length = 0
    acgt_string = ""
    
    # Iterate through the string
    for i in range(len(s)):
        # If the current character is A, C, G, or T, add it to the current ACGT string
        if s[i] in "ACGT":
            current_length += 1
            acgt_string += s[i]
        # If the current character is not A, C, G, or T, reset the current ACGT string
        else:
            current_length = 0
            acgt_string = ""
        
        # If the current ACGT string is longer than the maximum length, update the maximum length
        if current_length > max_length:
            max_length = current_length
    
    # Return the maximum length
    return max_length

def main():
    s = input("Enter a string: ")
    print(longest_acgt_substring(s))

if __name__ == '__main__':
    main()

