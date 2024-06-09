
def solve(s):
    # Initialize the number of operations to 0
    k = 0
    
    # Loop until the string is a palindrome or the maximum number of operations is reached
    while not is_palindrome(s) and k < 30:
        # Find the first non-palindromic substring in the string
        i = find_non_palindromic_substring(s)
        
        # If the substring is at the beginning of the string, perform the first operation
        if i == 0:
            s = "".join([s[i:], s[:i]])
            k += 1
        # If the substring is at the end of the string, perform the second operation
        elif i == len(s) - 1:
            s = "".join([s[:i], s[i:]])
            k += 1
        # If the substring is in the middle of the string, perform both operations
        else:
            s = "".join([s[:i], s[i:], s[:i]])
            k += 2
    
    # Return the number of operations and the resulting palindrome
    return k, s

# Check if a string is a palindrome
def is_palindrome(s):
    return s == s[::-1]

# Find the first non-palindromic substring in a string
def find_non_palindromic_substring(s):
    for i in range(len(s)):
        if s[i] != s[-i-1]:
            return i
    return -1

