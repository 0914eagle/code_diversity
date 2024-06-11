


def is_palindrome(string: str) -> bool:
    
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    
    if not string:
        return ''
    # Find the longest postfix of supplied string that is a palindrome
    for i in range(len(string), 0, -1):
        if string[:i] == string[:i][::-1]:
            palindromic_suffix = string[:i]
            break
    else:
        palindromic_suffix = ''
    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    return string + palindromic_suffix[::-1]


if
