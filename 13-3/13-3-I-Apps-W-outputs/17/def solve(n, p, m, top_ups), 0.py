
def solve(n, p, m, top_ups):
    balance = 0
    days_with_negative_balance = 0
    for i in range(m):
        balance += p
        for j in range(n):
            if top_ups[j][0] == i + 1:
                balance += top_ups[j][1]
        if balance < 0:
            days_with_negative_balance += 1
    return days_with_negative_balance

