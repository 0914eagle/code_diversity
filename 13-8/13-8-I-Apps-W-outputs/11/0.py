
def get_happy_ticket(ticket):
    n = len(ticket) // 2
    sum1 = sum(int(ticket[i]) for i in range(n))
    sum2 = sum(int(ticket[i]) for i in range(n, len(ticket)))
    return sum1 == sum2

def get_winner(ticket):
    if get_happy_ticket(ticket):
        return "Bicarp"
    else:
        return "Monocarp"

if __name__ == '__main__':
    n = int(input())
    ticket = input()
    print(get_winner(ticket))

