
def get_min_cost(n, a, b, k, f, trips):
    # Initialize variables
    cost = 0
    card_cost = f
    card_count = 0
    current_stop = ""
    route_costs = {}

    # Iterate through the trips
    for i in range(n):
        start_stop, end_stop = trips[i]

        # Check if the trip is a transshipment
        if start_stop == current_stop:
            cost += b
        else:
            cost += a

        # Check if a travel card can be bought for the current route
        route = (start_stop, end_stop)
        if card_count < k and route not in route_costs:
            route_costs[route] = card_cost
            card_count += 1

        # Update the current stop and cost
        current_stop = end_stop
        cost += route_costs.get(route, 0)

    return cost

def main():
    n, a, b, k, f = map(int, input().split())
    trips = [input().split() for _ in range(n)]
    print(get_min_cost(n, a, b, k, f, trips))

if __name__ == '__main__':
    main()

