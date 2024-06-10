
def get_travel_cost(trips, a, b, k, f):
    # Initialize variables
    cost = 0
    travel_cards = []

    # Iterate through the trips
    for i in range(len(trips)):
        # Get the current and next trip
        current_trip = trips[i]
        next_trip = trips[i + 1] if i + 1 < len(trips) else None

        # Check if the current trip is a transshipment
        is_transshipment = current_trip[0] == next_trip[1] if next_trip else False

        # Calculate the cost of the current trip
        trip_cost = a if not is_transshipment else b

        # Check if the current trip is a new route
        if current_trip not in travel_cards:
            # Add the current trip to the list of travel cards
            travel_cards.append(current_trip)

            # Check if the number of travel cards is less than or equal to k
            if len(travel_cards) <= k:
                # Add the cost of the travel card to the total cost
                cost += f

        # Add the cost of the current trip to the total cost
        cost += trip_cost

    return cost

def main():
    # Read the input
    n, a, b, k, f = map(int, input().split())
    trips = [input().split() for _ in range(n)]

    # Calculate the travel cost
    cost = get_travel_cost(trips, a, b, k, f)

    # Print the result
    print(cost)

if __name__ == '__main__':
    main()

