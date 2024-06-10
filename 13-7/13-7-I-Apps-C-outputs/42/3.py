
def get_travel_cost(trips, a, b, k, f):
    # Initialize variables
    cost = 0
    cards = 0
    current_stop = ""
    route_costs = {}

    # Iterate through the trips
    for trip in trips:
        # Get the start and end stops of the trip
        start_stop, end_stop = trip

        # Check if the trip is a transshipment
        if start_stop == current_stop:
            cost += b
        else:
            cost += a

        # Check if the trip is a new route
        if start_stop not in route_costs:
            route_costs[start_stop] = {}

        # Check if the trip is a return trip
        if end_stop in route_costs[start_stop]:
            cost -= route_costs[start_stop][end_stop]
        else:
            route_costs[start_stop][end_stop] = cost
            cards += 1
            if cards > k:
                return -1

        # Update the current stop
        current_stop = end_stop

    # Add the cost of the travel cards
    cost += f * cards

    return cost

def main():
    n, a, b, k, f = map(int, input().split())
    trips = [input().split() for _ in range(n)]
    print(get_travel_cost(trips, a, b, k, f))

if __name__ == '__main__':
    main()

