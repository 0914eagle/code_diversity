
def get_travel_cost(trips, a, b, k, f):
    # Initialize variables
    total_cost = 0
    travel_cards = []

    # Iterate over the trips
    for i in range(len(trips)):
        # Get the current and next trip
        current_trip = trips[i]
        next_trip = trips[i + 1] if i < len(trips) - 1 else None

        # Check if the trip is a transshipment
        is_transshipment = current_trip == next_trip

        # Calculate the cost of the trip
        cost = a if not is_transshipment else b

        # Check if the trip is within the same route
        is_same_route = current_trip[0] == next_trip[1] if next_trip else False

        # Check if the travel card is already purchased
        has_travel_card = current_trip[0] in travel_cards or current_trip[1] in travel_cards

        # If the trip is within the same route and the travel card is not already purchased, purchase the travel card
        if is_same_route and not has_travel_card:
            travel_cards.append(current_trip[0])
            total_cost += f

        # Add the cost of the trip to the total cost
        total_cost += cost

    # Return the total cost
    return total_cost

def main():
    # Read the input
    n, a, b, k, f = map(int, input().split())
    trips = [input().split() for _ in range(n)]

    # Calculate the total cost
    total_cost = get_travel_cost(trips, a, b, k, f)

    # Print the total cost
    print(total_cost)

if __name__ == '__main__':
    main()

