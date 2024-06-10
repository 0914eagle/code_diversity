
def get_happy_ticket(ticket):
    n = len(ticket) // 2
    first_sum = sum(map(int, ticket[:n]))
    second_sum = sum(map(int, ticket[n:]))
    return first_sum == second_sum

def play_game(ticket):
    while "?" in ticket:
        i = ticket.index("?")
        ticket = ticket[:i] + str(int(ticket[i])) + ticket[i+1:]
    return get_happy_ticket(ticket)

def main():
    n = int(input())
    ticket = input()
    if play_game(ticket):
        print("Bicarp")
    else:
        print("Monocarp")

if __name__ == '__main__':
    main()

