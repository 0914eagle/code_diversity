
def get_happy_ticket(ticket):
    n = len(ticket)
    first_half = ticket[:n//2]
    second_half = ticket[n//2:]
    return "".join(first_half) == "".join(second_half)

def get_winner(ticket):
    if get_happy_ticket(ticket):
        return "Bicarp"
    else:
        return "Monocarp"

if __name__ == '__main__':
    n = int(input())
    ticket = input()
    print(get_winner(ticket))

