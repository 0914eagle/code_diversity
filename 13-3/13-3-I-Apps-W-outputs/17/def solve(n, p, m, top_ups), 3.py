
def solve(n, p, m, top_ups):
    balance = 0
    days_with_negative_balance = 0
    for i in range(m):
        balance += p
        if i in top_ups:
            balance += top_ups[i]
        if balance < 0:
            days_with_negative_balance += 1
    return days_with_negative_balance

