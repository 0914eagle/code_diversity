
def solve(trips):
    trips.insert(0, 0)
    total_cost = 0
    for i in range(len(trips)):
        trip_time = trips[i]
        if i == 0:
            total_cost += 20
        elif trip_time - trips[i-1] == 1:
            total_cost += 20
        elif trip_time - trips[i-1] == 90:
            total_cost += 50
        elif trip_time - trips[i-1] == 1440:
            total_cost += 120
        else:
            total_cost += 20
    return total_cost

