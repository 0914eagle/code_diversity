
def get_optimal_tickets(trips):
    # Initialize variables
    total_cost = 0
    tickets = []
    current_trip = 0
    
    # Loop through each trip
    for trip in trips:
        # Check if current trip is within the time range of the previous trip
        if trip > current_trip + 1:
            # Add a one-trip ticket to the list of tickets
            tickets.append(1)
            total_cost += 20
        # Check if current trip is within the time range of the previous ticket
        elif trip > current_trip + 90:
            # Add a 90-minute ticket to the list of tickets
            tickets.append(90)
            total_cost += 50
        # Check if current trip is within the time range of the previous ticket
        elif trip > current_trip + 1440:
            # Add a one-day ticket to the list of tickets
            tickets.append(1440)
            total_cost += 120
        
        # Update the current trip time
        current_trip = trip
    
    # Return the list of tickets and the total cost
    return tickets, total_cost

def get_charged_amount(trips, tickets, total_cost):
    # Initialize variables
    charged_amount = 0
    current_trip = 0
    
    # Loop through each trip
    for trip in trips:
        # Check if current trip is within the time range of the previous trip
        if trip > current_trip + 1:
            # Add the cost of one-trip ticket to the charged amount
            charged_amount += 20
        # Check if current trip is within the time range of the previous ticket
        elif trip > current_trip + 90:
            # Add the cost of 90-minute ticket to the charged amount
            charged_amount += 50
        # Check if current trip is within the time range of the previous ticket
        elif trip > current_trip + 1440:
            # Add the cost of one-day ticket to the charged amount
            charged_amount += 120
        
        # Update the current trip time
        current_trip = trip
    
    # Return the charged amount
    return charged_amount - total_cost

def main():
    # Read the number of trips
    n = int(input())
    
    # Read the trips
    trips = []
    for i in range(n):
        trips.append(int(input()))
    
    # Get the optimal tickets and the total cost
    tickets, total_cost = get_optimal_tickets(trips)
    
    # Get the charged amount
    charged_amount = get_charged_amount(trips, tickets, total_cost)
    
    # Print the charged amount for each trip
    for trip in trips:
        print(charged_amount)

if __name__ == '__main__':
    main()

