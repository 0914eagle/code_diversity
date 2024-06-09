
def is_palindrome(s):
    return s == s[::-1]

def solve(s):
    if is_palindrome(s):
        return "NA"
    
    for i in range(len(s)):
        if is_palindrome(s[:i] + s[i] + s[i:]) or is_palindrome(s[:i] + s[i+1] + s[i:]) :
            return s[:i] + s[i] + s[i:]
    
    return "NA"

