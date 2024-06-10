
def get_travel_cost(trips, a, b, k, f):
    # Initialize variables
    cost = 0
    travel_cards = []

    # Iterate through the trips
    for i in range(len(trips)):
        # Get the current and next trip
        current_trip = trips[i]
        next_trip = trips[i + 1] if i < len(trips) - 1 else None

        # Check if the current trip is a transshipment
        if current_trip == next_trip:
            # If it is a transshipment, add the cost of the trip
            cost += b
        else:
            # If it is not a transshipment, add the cost of the trip
            cost += a

            # Check if the current trip is a new route
            if current_trip not in travel_cards:
                # If it is a new route, add the cost of the travel card
                cost += f
                travel_cards.append(current_trip)

                # Check if the number of travel cards exceeds the limit
                if len(travel_cards) > k:
                    # If it does, remove the oldest travel card
                    travel_cards.pop(0)

    return cost

def main():
    # Read the input
    n, a, b, k, f = map(int, input().split())
    trips = [input().split() for _ in range(n)]

    # Calculate the minimum travel cost
    cost = get_travel_cost(trips, a, b, k, f)

    # Print the result
    print(cost)

if __name__ == '__main__':
    main()

