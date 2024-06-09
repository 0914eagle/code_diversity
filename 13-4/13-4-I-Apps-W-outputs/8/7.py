
def get_cost(trips, current_time):
    cost = 0
    for trip in trips:
        if trip[0] <= current_time <= trip[1]:
            cost += trip[2]
    return cost

def get_optimal_cost(trips):
    cost = 0
    for i in range(len(trips)):
        current_time = trips[i][1]
        cost += get_cost(trips[:i+1], current_time)
    return cost

def get_charged_amount(trips):
    optimal_cost = get_optimal_cost(trips)
    return optimal_cost - get_cost(trips, 0)

def main():
    n = int(input())
    trips = []
    for i in range(n):
        trip = list(map(int, input().split()))
        trips.append(trip)
    print(*[get_charged_amount(trips[:i+1]) for i in range(n)], sep='\n')

if __name__ == '__main__':
    main()

