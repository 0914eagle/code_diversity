
def solve(s):
    # Check if the string is already a palindrome
    if s == s[::-1]:
        return "First"

    # Check if the string can be made a palindrome by removing a character
    for i in range(len(s)):
        if s[:i] + s[i+1:] == s[i:] + s[:i][::-1]:
            return "Second"

    # If the string cannot be made a palindrome, the first player wins
    return "First"

