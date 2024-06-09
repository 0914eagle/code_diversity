
def solve(N, K, P):
    # Initialize a list to store the possible characters
    chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    # Initialize a list to store the palindromic substrings
    palindromes = []
    
    # Iterate through the possible characters
    for char in chars:
        # Check if the character is in the string
        if char in palindromes:
            # If the character is already in the string, continue to the next character
            continue
        # Add the character to the string
        palindromes.append(char)
        # Check if the string has the required length
        if len(palindromes) == N:
            # If the string has the required length, check if it has the required number of distinct characters
            if len(set(palindromes)) == K:
                # If the string has the required number of distinct characters, check if it has the required longest palindromic substring
                if len(max(palindromes, key=len)) == P:
                    # If the string has the required longest palindromic substring, return the string
                    return "".join(palindromes)
    
    # If no string satisfies all the requirements, return "IMPOSSIBLE"
    return "IMPOSSIBLE"

