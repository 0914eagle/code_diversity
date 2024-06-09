
def get_cost(trips):
    # Initialize variables
    cost = 0
    current_time = 0
    tickets = []

    # Iterate through the trips
    for trip in trips:
        # Check if the current trip is within the time range of the current ticket
        if current_time <= trip <= current_time + 90:
            # If it is, then the passenger does not need to pay for a new ticket
            continue
        # If the current trip is not within the time range of the current ticket, then the passenger needs to pay for a new ticket
        else:
            # Calculate the cost of the new ticket
            cost += 50
            # Add the new ticket to the list of tickets
            tickets.append(trip)
            # Set the current time to the end time of the new ticket
            current_time = trip + 90

    # Return the total cost
    return cost

def main():
    # Read the number of trips
    n = int(input())
    # Read the times of the trips
    trips = [int(input()) for _ in range(n)]
    # Calculate the cost of the tickets
    cost = get_cost(trips)
    # Print the cost
    print(cost)

if __name__ == '__main__':
    main()

