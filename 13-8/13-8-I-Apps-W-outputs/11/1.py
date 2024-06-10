
def get_winner(n, ticket):
    # Initialize the winner as None
    winner = None
    
    # Loop until there are no more erased digits in the ticket
    while "?" in ticket:
        # Find the index of the first erased digit
        index = ticket.index("?")
        
        # Replace the erased digit with a random digit from 0 to 9
        ticket = ticket[:index] + str(random.randint(0, 9)) + ticket[index+1:]
    
    # Check if the ticket is happy
    if is_happy(n, ticket):
        # If the ticket is happy, the winner is Bicarp
        winner = "Bicarp"
    else:
        # If the ticket is not happy, the winner is Monocarp
        winner = "Monocarp"
    
    return winner

def is_happy(n, ticket):
    # Find the sum of the first n/2 digits
    first_sum = sum(map(int, ticket[:n//2]))
    
    # Find the sum of the last n/2 digits
    last_sum = sum(map(int, ticket[n//2:]))
    
    # Return True if the sums are equal, False otherwise
    return first_sum == last_sum

if __name__ == '__main__':
    n = int(input())
    ticket = input()
    print(get_winner(n, ticket))

