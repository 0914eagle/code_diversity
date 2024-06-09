
def get_n_th_even_length_palindrome(n):
    count = 0
    i = 1
    while count < n:
        num = str(i)
        if len(num) % 2 == 0 and num == num[::-1]:
            count += 1
        i += 1
    return i - 1

