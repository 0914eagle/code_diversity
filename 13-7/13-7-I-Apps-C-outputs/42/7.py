
def get_min_cost(trips, a, b, k, f):
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
        cost += trip_cost

        # Check if the current trip is a transshipment and if we can buy a travel card for it
        if is_transshipment and (current_trip[0], current_trip[1]) not in travel_cards and k > 0:
            # Buy a travel card for the current trip
            travel_cards.append((current_trip[0], current_trip[1]))
            k -= 1

    # Calculate the cost of the travel cards
    travel_cards_cost = f * len(travel_cards)

    # Return the minimum cost
    return cost + travel_cards_cost

def main():
    # Read the input
    n, a, b, k, f = map(int, input().split())
    trips = [input().split() for _ in range(n)]

    # Calculate the minimum cost
    min_cost = get_min_cost(trips, a, b, k, f)

    # Print the minimum cost
    print(min_cost)

if __name__ == '__main__':
    main()

