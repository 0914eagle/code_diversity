
def solve(N, K, P):
    # Initialize a list to store the possible characters
    chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    # Initialize a list to store the palindromic substrings
    palindromes = []
    
    # Iterate through the possible characters
    for char in chars:
        # Check if the character is part of the palindrome
        if char in palindromes:
            # If the character is already in the palindrome, skip it
            continue
        # Check if the character is part of the longest palindrome
        if len(palindromes) == P:
            # If the longest palindrome has length P, break the loop
            break
        # Add the character to the palindrome
        palindromes.append(char)
    
    # Initialize a list to store the symmetric strings
    symmetric_strings = []
    
    # Iterate through the possible characters
    for char in chars:
        # Check if the character is part of the symmetric string
        if char in symmetric_strings:
            # If the character is already in the symmetric string, skip it
            continue
        # Check if the character is part of the longest palindrome
        if len(symmetric_strings) == N // 2:
            # If the symmetric string has length N // 2, break the loop
            break
        # Add the character to the symmetric string
        symmetric_strings.append(char)
    
    # Initialize a list to store the final strings
    final_strings = []
    
    # Iterate through the symmetric strings
    for symmetric_string in symmetric_strings:
        # Check if the symmetric string has length N
        if len(symmetric_string) != N:
            # If the symmetric string has length different from N, skip it
            continue
        # Check if the symmetric string has exactly K distinct characters
        if len(set(symmetric_string)) != K:
            # If the symmetric string has less than K distinct characters, skip it
            continue
        # Check if the symmetric string has a palindromic substring with length P
        if any(palindrome in symmetric_string for palindrome in palindromes):
            # If the symmetric string has a palindromic substring with length P, add it to the final strings
            final_strings.append(symmetric_string)
    
    # Check if there are any final strings
    if not final_strings:
        # If there are no final strings, return IMPOSSIBLE
        return "IMPOSSIBLE"
    # Return any of the final strings
    return final_strings[0]

