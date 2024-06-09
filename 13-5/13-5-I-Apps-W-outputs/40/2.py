
def solve(s):
    # Check if the string is already a palindrome
    if s == s[::-1]:
        return "First"
    
    # Check if the string can be reordered to form a palindrome
    for i in range(len(s)):
        if s[i] != s[-i-1]:
            return "Second"
    return "First"

