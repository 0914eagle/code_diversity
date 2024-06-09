
def make_palindrome(string: str) -> str:
    
    # Find the longest postfix of supplied string that is a palindrome
    palindromic_suffix = ""
    for i in range(len(string), 0, -1):
        if string[-i:] == string[-i:][::-1]:
            palindromic_suffix = string[-i:]
            break
    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    return string + palindromic_suffix[::-1]

