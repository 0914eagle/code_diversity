
def solve(n, m):
    if n == m:
        return f"Dr. Chaz will have {m} piece[s] of chicken left over!"
    elif n > m:
        return f"Dr. Chaz needs {n-m} more piece[s] of chicken!"
    else:
        return f"Dr. Chaz will have {m-n} piece[s] of chicken left over!"

