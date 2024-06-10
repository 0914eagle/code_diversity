
def get_happy_ticket_winner(n, ticket):
    # Convert the ticket string to a list of integers
    ticket_list = [int(i) if i.isdigit() else None for i in ticket]
    
    # Find the indices of the erased digits
    erased_indices = [i for i, x in enumerate(ticket_list) if x is None]
    
    # Check if the ticket is already happy
    if len(erased_indices) == 0:
        return "Bicarp"
    
    # Initialize the winner to Monocarp
    winner = "Monocarp"
    
    # Loop through the erased indices
    for i in erased_indices:
        # Check if the ticket is happy with the current digit
        if is_happy_ticket(ticket_list, n, i):
            # If the ticket is happy, switch the winner to Bicarp
            winner = "Bicarp"
            break
    
    return winner

def is_happy_ticket(ticket_list, n, i):
    # Calculate the sum of the first half of the ticket
    first_half_sum = sum(ticket_list[:n//2])
    
    # Calculate the sum of the second half of the ticket
    second_half_sum = sum(ticket_list[n//2:])
    
    # Check if the sums are equal
    return first_half_sum == second_half_sum

def main():
    n = int(input())
    ticket = input()
    print(get_happy_ticket_winner(n, ticket))

if __name__ == '__main__':
    main()

