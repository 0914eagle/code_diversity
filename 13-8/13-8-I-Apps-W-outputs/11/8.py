
def get_happy_ticket(ticket):
    n = len(ticket) // 2
    first_sum = sum(int(ticket[i]) for i in range(n))
    second_sum = sum(int(ticket[i]) for i in range(n, len(ticket)))
    return first_sum == second_sum

def get_winner(ticket):
    if "?" not in ticket:
        return "Bicarp"
    
    happy_ticket = get_happy_ticket(ticket)
    if happy_ticket:
        return "Bicarp"
    else:
        return "Monocarp"

def main():
    n = int(input())
    ticket = input()
    print(get_winner(ticket))

if __name__ == '__main__':
    main()

