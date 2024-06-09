
def solve(n, p, m, deposits):
    balance = 0
    negative_balance_days = 0
    for i in range(m):
        balance += deposits[i][1] if i in deposits else -p
        if balance < 0:
            negative_balance_days += 1
    return negative_balance_days

