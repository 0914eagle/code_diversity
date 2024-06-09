
def get_optimal_tickets(trips):
    tickets = []
    current_trip = 0
    while current_trip < len(trips):
        # Find the cheapest ticket for the current trip
        cheapest_ticket = find_cheapest_ticket(trips, current_trip)
        tickets.append(cheapest_ticket)
        current_trip += cheapest_ticket[1]
    return tickets

def find_cheapest_ticket(trips, current_trip):
    # Find the cheapest ticket for the current trip
    cheapest_ticket = (0, 0)
    for ticket in [(1, 20), (90, 50), (1440, 120)]:
        if current_trip + ticket[1] <= len(trips):
            total_cost = get_total_cost(trips, current_trip, ticket[1])
            if total_cost < cheapest_ticket[0]:
                cheapest_ticket = (total_cost, ticket[1])
    return cheapest_ticket

def get_total_cost(trips, current_trip, trip_length):
    # Calculate the total cost of the current trip
    total_cost = 0
    for i in range(current_trip, current_trip + trip_length):
        total_cost += trips[i]
    return total_cost

def get_charged_amount(trips, tickets):
    # Calculate the charged amount for each trip
    charged_amount = []
    current_trip = 0
    for ticket in tickets:
        charged_amount.append(ticket[0] - trips[current_trip])
        current_trip += ticket[1]
    return charged_amount

def main():
    trips = [20, 20, 10, 0, 20, 0, 0, 20, 20, 10]
    tickets = get_optimal_tickets(trips)
    charged_amount = get_charged_amount(trips, tickets)
    print(charged_amount)

if __name__ == '__main__':
    main()

