
def is_lucky_ticket(ticket):
    n = len(ticket)
    if n < 2:
        return "NO"
    
    sums = []
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += int(ticket[j])
            if sum in sums:
                return "YES"
            sums.append(sum)
    
    return "NO"

