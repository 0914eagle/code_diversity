
def solve(N, K, P):
    # Initialize a list to store the possible characters
    chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    # Initialize a list to store the palindromic substrings
    palindromes = []
    
    # Iterate through the possible characters
    for char in chars:
        # Check if the character is present in the string
        if char in palindromes:
            # If the character is present, add it to the list of palindromic substrings
            palindromes.append(char)
    
    # Check if the length of the palindromic substrings is equal to P
    if len(palindromes) == P:
        # If the length is equal to P, return the string
        return ''.join(palindromes)
    else:
        # If the length is not equal to P, return IMPOSSIBLE
        return "IMPOSSIBLE"

