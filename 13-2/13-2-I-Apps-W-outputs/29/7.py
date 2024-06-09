
def is_palindrome(n):
    return str(n) == str(n)[::-1]

def find_nth_palindrome(n):
    count = 0
    i = 1
    while count < n:
        if is_palindrome(i) and len(str(i)) % 2 == 0:
            count += 1
        i += 1
    return i - 1

