
def sort_tickets(tickets):
    return sorted(tickets)

def get_input():
    return list(map(int, input().split()))

if __name__ == '__main__':
    tickets = get_input()
    sorted_tickets = sort_tickets(tickets)
    print(*sorted_tickets, sep=' ')

