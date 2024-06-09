
def get_charges(trips):
    charges = []
    current_time = 0
    total_cost = 0
    for trip in trips:
        if trip > current_time + 90:
            charges.append(50)
            total_cost += 50
        elif trip > current_time + 20:
            charges.append(20)
            total_cost += 20
        else:
            charges.append(0)
        current_time = trip
    return charges

