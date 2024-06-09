
def get_max_account_state(n):
    if n < 0:
        n = -n
    return max(n, n // 10, n % 10)

