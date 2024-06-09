
def is_lucky_ticket(ticket):
    n = len(ticket)
    if n < 2:
        return "NO"
    
    sum_left = 0
    sum_right = sum(map(int, ticket))
    for i in range(n-1):
        sum_left += int(ticket[i])
        sum_right -= int(ticket[i])
        if sum_left == sum_right:
            return "YES"
    
    return "NO"

