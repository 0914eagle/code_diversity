
def get_tolls(tickets):
    # Initialize a set to store the entrances and exits
    entrances_and_exits = set()
    
    # Iterate over the tickets
    for ticket in tickets:
        # Add the entrance and exit to the set
        entrances_and_exits.add(ticket[0])
        entrances_and_exits.add(ticket[1])
    
    # Initialize a dictionary to store the tolls for each entrance
    tolls = {}
    
    # Iterate over the entrances and exits
    for entrance in entrances_and_exits:
        # Initialize the toll for this entrance to 0
        tolls[entrance] = 0
    
    # Iterate over the tickets again
    for ticket in tickets:
        # Get the entrance and exit numbers
        entrance, exit = ticket
        
        # If the entrance and exit are not the same
        if entrance != exit:
            # Add the toll for this entrance
            tolls[entrance] += abs(entrance - exit)
    
    # Return the sum of the tolls
    return sum(tolls.values())

def get_least_tolls(tickets):
    # Initialize the least tolls to infinity
    least_tolls = float("inf")
    
    # Iterate over the tickets
    for i in range(len(tickets)):
        # Get the current ticket
        current_ticket = tickets[i]
        
        # Iterate over the remaining tickets
        for j in range(i+1, len(tickets)):
            # Get the next ticket
            next_ticket = tickets[j]
            
            # If the current ticket and next ticket have the same entrance or exit
            if current_ticket[0] == next_ticket[1] or current_ticket[1] == next_ticket[0]:
                # Continue to the next iteration
                continue
            
            # Exchange the tickets
            current_ticket[0], next_ticket[1] = next_ticket[1], current_ticket[0]
            
            # Get the tolls for the exchanged tickets
            exchanged_tolls = get_tolls(tickets)
            
            # If the exchanged tolls are less than the least tolls
            if exchanged_tolls < least_tolls:
                # Update the least tolls
                least_tolls = exchanged_tolls
    
    # Return the least tolls
    return least_tolls

def main():
    # Read the number of trucks
    num_trucks = int(input())
    
    # Initialize a list to store the tickets
    tickets = []
    
    # Iterate over the number of trucks
    for _ in range(num_trucks):
        # Read the entrance and exit numbers for the current truck
        entrance, exit = map(int, input().split())
        
        # Add the entrance and exit numbers to the list of tickets
        tickets.append([entrance, exit])
    
    # Get the least tolls
    least_tolls = get_least_tolls(tickets)
    
    # Print the least tolls
    print(least_tolls)

if __name__ == '__main__':
    main()

