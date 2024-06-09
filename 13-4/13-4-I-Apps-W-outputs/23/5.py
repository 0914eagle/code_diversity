
def is_palindrome(s):
    return s == s[::-1]

def insert_letter(s):
    for i in range(len(s)):
        if is_palindrome(s[:i] + s[i+1:]):
            return s[:i] + s[i] + s[i+1:]
    return "NA"

