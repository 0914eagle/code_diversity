


def is_palindrome(string: str) -> bool:
    
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    
    if not string:
        return ''
    # Find the longest postfix of supplied string that is a palindrome
    palindrome = ''
    for i in range(len(string), -1, -1):
        sub_string = string[:i]
        if sub_string == sub_string[::-1]:
            palindrome = sub_string
            break
    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    return string + palindrome[::-1]


if __name__ == '__main__':
