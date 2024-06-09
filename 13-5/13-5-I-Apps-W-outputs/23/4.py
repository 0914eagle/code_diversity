
def get_charges(trips):
    charges = []
    total_cost = 0
    for i in range(len(trips)):
        trip_time = trips[i]
        if i == 0:
            charges.append(20)
            total_cost += 20
        elif i == 1:
            charges.append(20)
            total_cost += 20
        elif trip_time - trips[i-1] == 90:
            charges.append(50)
            total_cost += 50
        else:
            charges.append(10)
            total_cost += 10
    return [total_cost - prev_cost for prev_cost, _ in zip(charges, charges[1:])]

