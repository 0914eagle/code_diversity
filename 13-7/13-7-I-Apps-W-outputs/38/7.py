
def is_lucky_ticket(ticket):
    sum1 = sum([int(ticket[i]) for i in range(3)])
    sum2 = sum([int(ticket[i]) for i in range(3, 6)])
    return sum1 == sum2

