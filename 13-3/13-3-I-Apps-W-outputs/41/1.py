
def max_bank_account(n):
    if n < 0:
        n = -n
    return max(n - int(str(n)[-1]), n - int(str(n)[:-1]))

