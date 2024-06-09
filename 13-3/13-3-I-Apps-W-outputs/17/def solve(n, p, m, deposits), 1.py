
def solve(n, p, m, deposits):
    balance = 0
    negative_days = 0
    for i in range(m):
        balance += deposits.get(i + 1, 0) - p
        if balance < 0:
            negative_days += 1
    return negative_days

