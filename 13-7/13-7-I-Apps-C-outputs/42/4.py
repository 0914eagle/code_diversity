
def get_travel_cost(n, a, b, k, f, trips):
    # Initialize variables
    cost = 0
    travel_cards = []

    # Iterate through the trips
    for i in range(n):
        # Get the current trip
        trip = trips[i]

        # Check if the trip is a transshipment
        if i > 0 and trip[0] == trips[i - 1][1]:
            # Add the cost of the transshipment to the total cost
            cost += b
        else:
            # Add the cost of the regular trip to the total cost
            cost += a

        # Check if the trip is a new bus route
        if trip[0] not in travel_cards:
            # Add the cost of the travel card to the total cost
            cost += f
            # Add the trip to the list of travel cards
            travel_cards.append(trip[0])

    # Return the total cost
    return cost

def main():
    # Read the input
    n, a, b, k, f = map(int, input().split())
    trips = [input().split() for _ in range(n)]

    # Calculate the travel cost
    cost = get_travel_cost(n, a, b, k, f, trips)

    # Print the result
    print(cost)

if __name__ == '__main__':
    main()

