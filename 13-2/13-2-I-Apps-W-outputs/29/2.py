
def is_palindrome(num):
    return str(num) == str(num)[::-1]

def find_nth_palindrome(n):
    count = 0
    num = 1
    while count < n:
        if is_palindrome(num) and len(str(num)) % 2 == 0:
            count += 1
        num += 1
    return num - 1

