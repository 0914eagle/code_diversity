
def make_palindrome(string: str) -> str:
    
    # find the longest postfix of the string that is a palindrome
    postfix = string[::-1]
    for i in range(len(string), 0, -1):
        if string[-i:] == postfix[:i]:
            postfix = string[-i:]
            break
    # append the reverse of the prefix to the end of the string
    return string + postfix[::-1]

