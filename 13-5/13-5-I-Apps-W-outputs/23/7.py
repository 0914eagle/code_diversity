
def solve(trips):
    trips.insert(0, 0)
    total_cost = 0
    cost = 0
    for i in range(len(trips)):
        if trips[i] - trips[i-1] == 1:
            cost += 20
        elif trips[i] - trips[i-1] == 90:
            cost += 50
        elif trips[i] - trips[i-1] == 1440:
            cost += 120
        total_cost += cost
        cost = 0
    return total_cost

