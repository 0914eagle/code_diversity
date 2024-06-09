
def maximize_bank_account(n):
    if n < 0:
        n = -n
    return max(n, n // 10, n % 10)

