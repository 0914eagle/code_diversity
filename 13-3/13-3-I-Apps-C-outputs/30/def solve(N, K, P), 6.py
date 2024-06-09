
def solve(N, K, P):
    # Initialize a list to store the possible characters
    chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    # Initialize a list to store the palindromic substrings
    palindromes = []
    
    # Iterate through the possible characters
    for char in chars:
        # Check if the character is already in the palindromes list
        if char not in palindromes:
            # Check if the character can be added to the palindromes list
            if len(palindromes) < K:
                palindromes.append(char)
            # Check if the character can be removed from the palindromes list
            elif len(palindromes) > K:
                palindromes.pop()
    
    # Initialize a list to store the symmetric strings
    symmetric_strings = []
    
    # Iterate through the palindromic substrings
    for palindrome in palindromes:
        # Check if the palindromic substring is already in the symmetric strings list
        if palindrome not in symmetric_strings:
            # Check if the palindromic substring can be added to the symmetric strings list
            if len(symmetric_strings) < P:
                symmetric_strings.append(palindrome)
            # Check if the palindromic substring can be removed from the symmetric strings list
            elif len(symmetric_strings) > P:
                symmetric_strings.pop()
    
    # Check if there is at least one symmetric string that satisfies all the requirements
    if len(symmetric_strings) == P:
        # Initialize a list to store the final string
        final_string = []
        
        # Iterate through the symmetric strings
        for symmetric_string in symmetric_strings:
            # Add the symmetric string to the final string
            final_string.append(symmetric_string)
        
        # Return the final string
        return ''.join(final_string)
    
    # Otherwise, return "IMPOSSIBLE"
    return "IMPOSSIBLE"

