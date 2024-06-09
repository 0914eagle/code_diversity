
def get_happy_ticket(ticket):
    n = len(ticket) // 2
    first_half = ticket[:n]
    second_half = ticket[n:]
    return first_half == second_half

def get_winner(ticket):
    if get_happy_ticket(ticket):
        return "Bicarp"
    else:
        return "Monocarp"

if __name__ == '__main__':
    n = int(input())
    ticket = input()
    print(get_winner(ticket))

