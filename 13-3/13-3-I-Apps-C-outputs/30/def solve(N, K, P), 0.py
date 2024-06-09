
def solve(N, K, P):
    # Initialize a list to store the possible characters
    chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    # Initialize a list to store the palindromic substrings
    palindromes = []
    
    # Iterate through the possible characters
    for char in chars:
        # Check if the character is in the palindromic substring
        if char in palindromes:
            # If the character is already in the palindromic substring, skip it
            continue
        # Check if the character is a palindrome
        if is_palindrome(char):
            # If the character is a palindrome, add it to the palindromic substring
            palindromes.append(char)
    
    # Initialize a list to store the symmetric strings
    symmetric_strings = []
    
    # Iterate through the palindromic substrings
    for palindrome in palindromes:
        # Check if the palindromic substring is a substring of the symmetric string
        if palindrome in symmetric_strings:
            # If the palindromic substring is already a substring of the symmetric string, skip it
            continue
        # Check if the symmetric string has the required length and number of distinct characters
        if len(palindrome) == N and len(set(palindrome)) == K:
            # If the symmetric string has the required length and number of distinct characters, add it to the list of symmetric strings
            symmetric_strings.append(palindrome)
    
    # Check if there are any symmetric strings that satisfy all the requirements
    if len(symmetric_strings) > 0:
        # If there are any symmetric strings that satisfy all the requirements, return any of them
        return symmetric_strings[0]
    else:
        # If there are no symmetric strings that satisfy all the requirements, return IMPOSSIBLE
        return "IMPOSSIBLE"

def is_palindrome(string):
    # Check if the string is a palindrome
    if string == string[::-1]:
        # If the string is a palindrome, return True
        return True
    else:
        # If the string is not a palindrome, return False
        return False

N, K, P = map(int, input().split())
print(solve(N, K, P))

