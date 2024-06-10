
def get_happy_tickets(ticket):
    n = len(ticket) // 2
    first_half = ticket[:n]
    second_half = ticket[n:]
    return [first_half, second_half]

def get_erased_digits(ticket):
    return [i for i, c in enumerate(ticket) if c == "?"]

def get_available_digits(ticket, erased_digits):
    available_digits = set(range(10))
    for i in erased_digits:
        available_digits.remove(int(ticket[i]))
    return available_digits

def get_next_move(ticket, erased_digits, available_digits):
    if not available_digits:
        return None
    for i in erased_digits:
        for d in available_digits:
            new_ticket = list(ticket)
            new_ticket[i] = str(d)
            new_ticket = "".join(new_ticket)
            if is_happy_ticket(new_ticket):
                return new_ticket
    return None

def is_happy_ticket(ticket):
    first_half, second_half = get_happy_tickets(ticket)
    return first_half == second_half

def play_game(ticket):
    erased_digits = get_erased_digits(ticket)
    available_digits = get_available_digits(ticket, erased_digits)
    while available_digits:
        new_ticket = get_next_move(ticket, erased_digits, available_digits)
        if new_ticket is None:
            return "Monocarp"
        ticket = new_ticket
        erased_digits = get_erased_digits(ticket)
        available_digits = get_available_digits(ticket, erased_digits)
    return "Bicarp"

if __name__ == '__main__':
    n = int(input())
    ticket = input()
    print(play_game(ticket))

