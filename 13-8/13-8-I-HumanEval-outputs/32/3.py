
def make_palindrome(string: str) -> str:
    
    # Find the longest postfix of the string that is a palindrome
    postfix = ""
    for i in range(len(string), 0, -1):
        if string[:i] == string[:i][::-1]:
            postfix = string[:i]
            break
    # Append the reverse of the prefix to the end of the postfix
    return postfix + string[len(postfix):][::-1]

