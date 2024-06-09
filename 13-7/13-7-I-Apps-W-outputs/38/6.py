
def is_lucky_ticket(ticket):
    sum1 = int(ticket[:3])
    sum2 = int(ticket[3:])
    return sum1 == sum2

def min_replacements_needed(ticket):
    count = 0
    for i in range(len(ticket)):
        for digit in range(10):
            if ticket[i] != str(digit):
                count += 1
                ticket = ticket[:i] + str(digit) + ticket[i+1:]
                if is_lucky_ticket(ticket):
                    return count
    return count

