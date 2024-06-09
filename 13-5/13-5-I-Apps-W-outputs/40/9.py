
def solve(s):
    # Check if the string is already a palindrome
    if s == s[::-1]:
        return "First"

    # Check if the first player can make a palindrome by removing a character
    for i in range(len(s)):
        if s[:i] + s[i+1:] == s[i] + s[i+1:] + s[i]:
            return "First"

    # Check if the second player can make a palindrome by removing a character
    for i in range(len(s)):
        if s[:i] + s[i+1:] == s[i+1:] + s[i]:
            return "Second"

    # If none of the above conditions are met, the first player will not be able to make a palindrome, so the second player will win
    return "Second"

