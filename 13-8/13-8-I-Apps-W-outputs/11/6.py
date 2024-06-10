
def get_erased_digits(ticket):
    return [i for i, c in enumerate(ticket) if c == "?"]

def get_happy_ticket(ticket):
    n = len(ticket) // 2
    return sum(map(int, ticket[:n])) == sum(map(int, ticket[n:]))

def get_winner(ticket):
    erased_digits = get_erased_digits(ticket)
    if not erased_digits:
        return "Bicarp" if get_happy_ticket(ticket) else "Monocarp"
    return "Monocarp"

def main():
    n = int(input())
    ticket = input()
    print(get_winner(ticket))

if __name__ == '__main__':
    main()

