
def get_flight_costs(flights):
    costs = {}
    for flight in flights:
        cost = costs.get(flight[0], 0) + flight[2]
        costs[flight[0]] = cost
    return costs

def get_min_cost(flights, additional_flights, start, end):
    costs = get_flight_costs(flights)
    for flight in additional_flights:
        if flight[0] == start or flight[1] == end:
            costs[flight[0]] = min(costs.get(flight[0], 0) + flight[2], costs.get(flight[1], 0) + flight[2])
    return costs[start]

def solve(flights, additional_flights, start, end):
    costs = get_flight_costs(flights)
    for flight in additional_flights:
        if flight[0] == start or flight[1] == end:
            costs[flight[0]] = min(costs.get(flight[0], 0) + flight[2], costs.get(flight[1], 0) + flight[2])
    return costs[start]

if __name__ == '__main__':
    num_airports, num_flights = map(int, input().split())
    flights = []
    for _ in range(num_flights):
        flights.append(list(map(int, input().split())))
    num_additional_flights = int(input())
    additional_flights = []
    for _ in range(num_additional_flights):
        additional_flights.append(list(map(int, input().split())))
    print(solve(flights, additional_flights, 1, num_airports))

