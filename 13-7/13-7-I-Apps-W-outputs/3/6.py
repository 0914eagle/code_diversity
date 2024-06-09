
def is_lucky_ticket(ticket):
    n = len(ticket)
    if n == 1:
        return "YES"
    sum1 = 0
    sum2 = 0
    for i in range(n//2):
        sum1 += int(ticket[i])
    for i in range(n//2, n):
        sum2 += int(ticket[i])
    if sum1 == sum2:
        return "YES"
    else:
        return "NO"

