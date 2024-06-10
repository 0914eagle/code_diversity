
def get_travel_cost(trips, a, b, k, f):
    # Initialize variables
    cost = 0
    travel_cards = []

    # Iterate through the trips
    for i in range(len(trips)):
        # Get the current and next trip
        current_trip = trips[i]
        if i < len(trips) - 1:
            next_trip = trips[i + 1]
        else:
            next_trip = trips[0]

        # Check if the current trip is a transshipment
        if current_trip == next_trip:
            cost += b
        else:
            cost += a

        # Check if the current trip is a new route
        if current_trip not in travel_cards:
            travel_cards.append(current_trip)

    # Check if the travel cards are within the limit
    if len(travel_cards) <= k:
        cost += f * len(travel_cards)

    return cost

def main():
    n, a, b, k, f = map(int, input().split())
    trips = [input().split() for _ in range(n)]
    print(get_travel_cost(trips, a, b, k, f))

if __name__ == '__main__':
    main()

