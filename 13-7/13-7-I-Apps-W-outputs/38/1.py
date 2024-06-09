
def is_lucky_ticket(ticket):
    sum1 = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
    sum2 = int(ticket[3]) + int(ticket[4]) + int(ticket[5])
    return sum1 == sum2

def min_replacements_needed(ticket):
    replacements = 0
    for i in range(len(ticket)):
        if ticket[i] != '0':
            continue
        ticket = ticket[:i] + '9' + ticket[i+1:]
        replacements += 1
        if is_lucky_ticket(ticket):
            break
    return replacements

