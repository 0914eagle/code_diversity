
def is_lucky_ticket(ticket):
    n = len(ticket)
    if n < 2:
        return "NO"
    
    sums = [0] * n
    for i in range(n):
        sums[i] = sums[i-1] + int(ticket[i])
    
    for i in range(1, n):
        for j in range(i, n):
            if sums[j] - sums[i-1] == sums[n-1] - sums[j]:
                return "YES"
    
    return "NO"

