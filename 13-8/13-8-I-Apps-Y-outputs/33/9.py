
def longest_acgt_substring(s):
    # Initialize variables
    max_length = 0
    current_length = 0
    acgt_string = ""
    
    # Iterate through the string
    for char in s:
        # If the character is A, C, G, or T, add it to the current substring
        if char in ["A", "C", "G", "T"]:
            current_length += 1
            acgt_string += char
        # If the character is not A, C, G, or T, reset the current substring
        else:
            if current_length > max_length:
                max_length = current_length
            current_length = 0
            acgt_string = ""
    
    # If the last substring is an ACGT string, add it to the maximum length
    if current_length > max_length:
        max_length = current_length
    
    return max_length

def main():
    s = input("Enter a string: ")
    print(longest_acgt_substring(s))

if __name__ == '__main__':
    main()

