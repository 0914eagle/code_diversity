
def get_maximum_account_state(n):
    if n < 0:
        n = -n
    return int(str(n)[:-1]) if n > 10 else n

