
def make_palindrome(string: str) -> str:
    
    # find the longest postfix of the string that is a palindrome
    palindromic_suffix = ''
    for i in range(len(string), 0, -1):
        if string[:i] == string[:i][::-1]:
            palindromic_suffix = string[:i]
            break
    # append the reverse of the prefix to the end of the string
    return string + palindromic_suffix[::-1]

