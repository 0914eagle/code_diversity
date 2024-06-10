
def is_happy(ticket, n):
    # Function to check if the ticket is happy
    first_half = ticket[:n//2]
    second_half = ticket[n//2:]
    return sum(first_half) == sum(second_half)

def get_erased_digits(ticket, n):
    # Function to get the indices of the erased digits
    indices = []
    for i in range(n):
        if ticket[i] == "?":
            indices.append(i)
    return indices

def get_replacement_digit(ticket, n, indices):
    # Function to get a replacement digit for the erased digits
    replacement_digit = 0
    for i in indices:
        if ticket[i] != "?":
            replacement_digit = ticket[i]
            break
    return replacement_digit

def get_next_ticket(ticket, n, indices, replacement_digit):
    # Function to get the next ticket after replacing the erased digits
    next_ticket = ticket
    for i in indices:
        next_ticket = next_ticket[:i] + str(replacement_digit) + next_ticket[i+1:]
    return next_ticket

def get_winner(ticket, n):
    # Function to get the winner
    indices = get_erased_digits(ticket, n)
    if len(indices) == 0:
        return "Bicarp"
    replacement_digit = get_replacement_digit(ticket, n, indices)
    next_ticket = get_next_ticket(ticket, n, indices, replacement_digit)
    if is_happy(next_ticket, n):
        return "Bicarp"
    else:
        return "Monocarp"

if __name__ == '__main__':
    n = int(input())
    ticket = input()
    print(get_winner(ticket, n))

