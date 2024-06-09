
def is_palindrome(s):
    return s == s[::-1]

def solve(n, strings):
    palindromes = 0
    for string in strings:
        if is_palindrome(string):
            palindromes += 1
    return palindromes

