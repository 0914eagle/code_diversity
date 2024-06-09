
def is_lucky_ticket(ticket):
    n = len(ticket)
    if n < 2:
        return "NO"
    
    sum1 = 0
    for i in range(n//2):
        sum1 += int(ticket[i])
    
    for i in range(n//2, n):
        if sum1 == int(ticket[i]):
            return "YES"
        sum1 += int(ticket[i])
    
    return "NO"

