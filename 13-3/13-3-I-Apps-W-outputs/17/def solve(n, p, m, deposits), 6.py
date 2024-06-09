
def solve(n, p, m, deposits):
    balance = 0
    days_with_negative_balance = 0
    for i in range(m):
        balance += deposits[i] if i in deposits else -p
        if balance < 0:
            days_with_negative_balance += 1
    return days_with_negative_balance

