
def get_trip_cost(trip, a, b):
    if trip[0] == trip[1]:
        return 0
    return a if trip[0] != trip[1] else b

def get_travel_card_cost(travel_cards, f):
    return f * len(travel_cards)

def get_min_cost(trips, a, b, k, f):
    travel_cards = {}
    cost = 0
    for trip in trips:
        if trip[0] not in travel_cards or trip[1] not in travel_cards:
            cost += get_trip_cost(trip, a, b)
            if len(travel_cards) < k:
                travel_cards[trip[0]] = trip[1]
                travel_cards[trip[1]] = trip[0]
        elif travel_cards[trip[0]] == trip[1] or travel_cards[trip[1]] == trip[0]:
            cost += get_trip_cost(trip, a, b)
        else:
            cost += get_trip_cost(trip, a, b) - get_travel_card_cost(travel_cards, f)
    return cost

if __name__ == '__main__':
    n, a, b, k, f = map(int, input().split())
    trips = [input().split() for _ in range(n)]
    print(get_min_cost(trips, a, b, k, f))

