
def solve(N, K, P):
    # Initialize a list to store the possible characters
    chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    # Initialize a list to store the palindromic substrings
    palindromes = []
    
    # Iterate through the possible characters
    for char in chars:
        # Check if the character is already in the palindromes list
        if char not in palindromes:
            # Check if the character is a palindrome
            if is_palindrome(char):
                # Add the character to the palindromes list
                palindromes.append(char)
    
    # Initialize a list to store the possible strings
    strings = []
    
    # Iterate through the palindromes
    for palindrome in palindromes:
        # Check if the palindrome has length P
        if len(palindrome) == P:
            # Add the palindrome to the strings list
            strings.append(palindrome)
    
    # Check if there are any strings that satisfy all the requirements
    for string in strings:
        # Check if the string has length N
        if len(string) == N:
            # Check if the string has exactly K distinct characters
            if len(set(string)) == K:
                # Return the string
                return string
    
    # If no string satisfies all the requirements, return "IMPOSSIBLE"
    return "IMPOSSIBLE"

# Define a function to check if a string is a palindrome
def is_palindrome(string):
    # Check if the string is the same forwards and backwards
    if string == string[::-1]:
        return True
    else:
        return False

# Test the solve function with example inputs
assert solve(6, 5, 3) == "rarity"
assert solve(9, 8, 1) == "canterlot"
assert solve(5, 3, 5) == "madam"

