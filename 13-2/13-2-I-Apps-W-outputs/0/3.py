
def solve(s):
    # Initialize the number of complementary substrings to 0
    count = 0
    
    # Loop through each substring of length 2 to length N
    for i in range(1, len(s)):
        # Loop through each starting index for the substring
        for j in range(len(s) - i + 1):
            # Extract the substring
            substring = s[j:j+i]
            
            # Check if the substring is complementary to its reverse complement
            if is_complementary(substring, reverse_complement(substring)):
                # Increment the number of complementary substrings
                count += 1
    
    # Return the number of complementary substrings
    return count

# Check if a string is complementary to its reverse complement
def is_complementary(s, t):
    # Create a dictionary to map each character to its complement
    complement_map = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }
    
    # Loop through each character in the string
    for i in range(len(s)):
        # If the character is not complementary to the corresponding character in the reverse complement, return False
        if s[i] != complement_map[t[len(s) - 1 - i]]:
            return False
    
    # If all characters are complementary, return True
    return True

# Return the reverse complement of a string
def reverse_complement(s):
    # Create a dictionary to map each character to its reverse complement
    complement_map = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }
    
    # Return the reverse of the string, with each character mapped to its reverse complement
    return ''.join([complement_map[c] for c in s[::-1]])

