
def get_trip_cost(start_stop, finish_stop, transshipment_cost, regular_cost):
    if start_stop == finish_stop:
        return 0
    else:
        return transshipment_cost if start_stop == "University" else regular_cost

def get_total_cost(trips, transshipment_cost, regular_cost, travel_cards):
    total_cost = 0
    for i in range(len(trips) - 1):
        total_cost += get_trip_cost(trips[i], trips[i + 1], transshipment_cost, regular_cost)
    return total_cost

def get_min_cost(trips, transshipment_cost, regular_cost, travel_cards):
    min_cost = get_total_cost(trips, transshipment_cost, regular_cost, travel_cards)
    for i in range(travel_cards):
        total_cost = get_total_cost(trips, transshipment_cost, regular_cost, i)
        if total_cost < min_cost:
            min_cost = total_cost
    return min_cost

def main():
    n, a, b, k, f = map(int, input().split())
    trips = []
    for i in range(n):
        start_stop, finish_stop = input().split()
        trips.append(start_stop)
        trips.append(finish_stop)
    print(get_min_cost(trips, b, a, k))

if __name__ == '__main__':
    main()

