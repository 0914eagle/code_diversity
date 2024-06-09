
def is_lucky_ticket(ticket):
    sum1 = int(ticket[:3])
    sum2 = int(ticket[3:])
    if sum1 == sum2:
        return 0
    else:
        return 2

