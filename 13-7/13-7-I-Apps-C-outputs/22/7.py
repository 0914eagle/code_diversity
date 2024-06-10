
def get_tolls(tickets):
    # Initialize a dictionary to store the tolls for each entrance and exit
    tolls = {}
    
    # Iterate over the tickets
    for ticket in tickets:
        # Get the entrance and exit numbers from the ticket
        entrance, exit = ticket
        
        # If the entrance and exit are not already in the dictionary, add them with a toll of 0
        if entrance not in tolls:
            tolls[entrance] = 0
        if exit not in tolls:
            tolls[exit] = 0
        
        # Update the toll for the entrance and exit
        tolls[entrance] += abs(entrance - exit)
        tolls[exit] += abs(entrance - exit)
    
    # Return the sum of all tolls
    return sum(tolls.values())

def get_optimal_tolls(tickets):
    # Initialize the optimal tolls as the initial tolls
    optimal_tolls = get_tolls(tickets)
    
    # Iterate over the tickets
    for i in range(len(tickets)):
        # Get the current ticket
        ticket = tickets[i]
        
        # Iterate over the remaining tickets
        for j in range(i+1, len(tickets)):
            # Get the next ticket
            next_ticket = tickets[j]
            
            # If the tickets are not already exchanged, exchange them and calculate the new tolls
            if ticket not in next_ticket and next_ticket not in ticket:
                exchanged_tickets = list(ticket) + list(next_ticket)
                exchanged_tolls = get_tolls(exchanged_tickets)
                
                # If the exchanged tolls are lower than the current optimal tolls, update the optimal tolls
                if exchanged_tolls < optimal_tolls:
                    optimal_tolls = exchanged_tolls
    
    # Return the optimal tolls
    return optimal_tolls

def main():
    # Read the number of trucks and their tickets
    num_trucks = int(input())
    tickets = []
    for _ in range(num_trucks):
        ticket = tuple(map(int, input().split()))
        tickets.append(ticket)
    
    # Calculate the optimal tolls
    optimal_tolls = get_optimal_tolls(tickets)
    
    # Print the optimal tolls
    print(optimal_tolls)

if __name__ == '__main__':
    main()

