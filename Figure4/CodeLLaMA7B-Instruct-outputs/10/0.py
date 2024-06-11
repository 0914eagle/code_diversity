


def is_palindrome(string: str) -> bool:
    
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    
    if not string:
        return ''
    # Find the longest postfix of `string` that is a palindrome
    palindrome = ''
    for i in range(len(string), -1, -1):
        substr = string[:i]
        if substr == substr[::-1]:
            palindrome = substr
            break
    # Append to the end of `string` the reverse of a prefix that comes before the palindromic suffix
    return string + palindrome[::-1]


if __name__ == '__
