
def is_lucky_ticket(ticket):
    sum1 = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
    sum2 = int(ticket[3]) + int(ticket[4]) + int(ticket[5])
    return sum1 == sum2

def min_replacements_to_make_lucky(ticket):
    if is_lucky_ticket(ticket):
        return 0
    replacements = 0
    for i in range(len(ticket)):
        for digit in range(10):
            if ticket[i] != str(digit):
                ticket = ticket[:i] + str(digit) + ticket[i+1:]
                if is_lucky_ticket(ticket):
                    return replacements + 1
        replacements += 1
    return replacements

