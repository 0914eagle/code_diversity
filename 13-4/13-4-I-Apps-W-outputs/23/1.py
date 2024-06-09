
def is_palindrome(s):
    return s == s[::-1]

def get_palindrome(s):
    if is_palindrome(s):
        return s
    
    for i in range(len(s)):
        if is_palindrome(s[:i] + s[i:]):
            return s[:i] + s[i-1] + s[i:]
    
    return "NA"

