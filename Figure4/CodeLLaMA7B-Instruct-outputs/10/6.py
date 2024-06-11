


def is_palindrome(string: str) -> bool:
    
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    
    if not string:
        return ''
    # find the longest postfix of supplied string that is a palindrome
    palindrome = ''
    for i in range(len(string), -1, -1):
        substr = string[:i]
        if substr == substr[::-1]:
            palindrome = substr
            break
    # append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    return string + palindrome[::-1]


if
