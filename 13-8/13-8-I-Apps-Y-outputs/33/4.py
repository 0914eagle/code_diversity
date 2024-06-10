
def longest_acgt_substring(s):
    # Initialize variables
    max_length = 0
    current_length = 0
    acgt_substring = ""
    
    # Iterate through the string
    for i in range(len(s)):
        # If the current character is A, C, G, or T, increment the current length
        if s[i] in ["A", "C", "G", "T"]:
            current_length += 1
        # If the current character is not A, C, G, or T, or if we have reached the end of the string, check if the current length is greater than the maximum length
        elif current_length > max_length:
            max_length = current_length
            acgt_substring = s[i-current_length:i]
            current_length = 0
    
    # Check if the last substring is the longest
    if current_length > max_length:
        max_length = current_length
        acgt_substring = s[len(s)-current_length:]
    
    return max_length

def main():
    s = input()
    print(longest_acgt_substring(s))

if __name__ == '__main__':
    main()

