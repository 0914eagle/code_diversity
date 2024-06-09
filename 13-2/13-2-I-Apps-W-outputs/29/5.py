
def is_palindrome(num):
    return str(num) == str(num)[::-1]

def find_n_th_even_length_palindrome(n):
    count = 0
    for i in range(1, 10**100000):
        if len(str(i)) % 2 == 0 and is_palindrome(i):
            count += 1
            if count == n:
                return i
    return -1

