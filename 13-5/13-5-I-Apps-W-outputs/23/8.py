
def solve(trips):
    tickets = []
    total_cost = 0
    for trip in trips:
        if len(tickets) == 0:
            tickets.append(trip)
            total_cost += 20
        elif trip == tickets[-1] + 1:
            tickets.append(trip)
            total_cost += 20
        elif trip == tickets[-1] + 90:
            tickets.append(trip)
            total_cost += 50
        else:
            tickets = [trip]
            total_cost += 20
    
    return total_cost

