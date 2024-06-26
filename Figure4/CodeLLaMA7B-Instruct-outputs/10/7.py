


def is_palindrome(string: str) -> bool:
    
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    
    if not string:
        return ''
    # Find the longest postfix of `string` that is a palindrome
    postfix = ''
    for i in range(len(string), -1, -1):
        if string[:i] == string[:i][::-1]:
            postfix = string[:i]
            break
    # Append to the end of `string` the reverse of a prefix that comes before the palindromic suffix
    return string + postfix[::-1]


if __
