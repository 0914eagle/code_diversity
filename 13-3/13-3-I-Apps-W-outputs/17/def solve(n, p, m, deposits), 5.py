
def solve(n, p, m, deposits):
    balance = 0
    days_with_negative_balance = 0
    for i in range(m):
        balance += p
        if i in deposits:
            balance += deposits[i]
        if balance < 0:
            days_with_negative_balance += 1
    return days_with_negative_balance

