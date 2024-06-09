
def solve(n, k, p):
    # Initialize a list to store the characters of the string
    chars = []
    
    # Loop through the characters of the alphabet
    for c in range(97, 97 + 26):
        # If the character is not already in the string, add it to the list
        if c not in chars:
            chars.append(chr(c))
    
    # If the length of the string is not equal to N, return "IMPOSSIBLE"
    if len(chars) != n:
        return "IMPOSSIBLE"
    
    # If the number of distinct characters is not equal to K, return "IMPOSSIBLE"
    if len(set(chars)) != k:
        return "IMPOSSIBLE"
    
    # Initialize a variable to store the longest palindromic substring
    longest_palindrome = ""
    
    # Loop through the characters of the string
    for i in range(n):
        # Find the longest palindromic substring starting from the current character
        palindrome = find_palindrome(chars[i:], p)
        
        # If the palindrome is longer than the current longest palindrome, update the longest palindrome
        if len(palindrome) > len(longest_palindrome):
            longest_palindrome = palindrome
    
    # If the longest palindrome has length equal to P, return the string
    if len(longest_palindrome) == p:
        return "".join(chars)
    
    # Otherwise, return "IMPOSSIBLE"
    return "IMPOSSIBLE"

# Find the longest palindromic substring starting from a given character
def find_palindrome(string, p):
    # Initialize a variable to store the longest palindromic substring
    longest_palindrome = ""
    
    # Loop through the characters of the string
    for i in range(len(string)):
        # Find the longest palindromic substring starting from the current character
        palindrome = find_palindrome_helper(string, i, p)
        
        # If the palindrome is longer than the current longest palindrome, update the longest palindrome
        if len(palindrome) > len(longest_palindrome):
            longest_palindrome = palindrome
    
    # Return the longest palindromic substring
    return longest_palindrome

# Find the longest palindromic substring starting from a given character and having a maximum length
def find_palindrome_helper(string, start, max_length):
    # Initialize variables to store the start and end indices of the palindrome
    start_index = start
    end_index = start
    
    # Loop until the end of the string or the maximum length is reached
    while end_index < len(string) and end_index - start_index < max_length:
        # If the character at the end index is the same as the character at the start index, update the end index
        if string[end_index] == string[start_index]:
            end_index += 1
        # Otherwise, break the loop
        else:
            break
    
    # If the palindrome has length greater than 1, return the substring
    if end_index - start_index > 1:
        return string[start_index:end_index]
    # Otherwise, return an empty string
    else:
        return ""

