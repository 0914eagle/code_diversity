
def solve(s):
    # Check if the string is already a palindrome
    if s == s[::-1]:
        return "First"

    # Check if the string can be made a palindrome by removing one letter
    for i in range(len(s)):
        if s[:i] + s[i+1:] == s[i] + s[:i] + s[i+1:]:
            return "First"

    # Check if the string can be made a palindrome by removing two letters
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[:i] + s[j+1:] == s[i] + s[i+1:j] + s[j+1:]:
                return "First"

    # If none of the above conditions are met, the second player wins
    return "Second"

