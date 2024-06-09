
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
        else:
            if trip_time - trips[i-1] <= 90:
                charges.append(0)
            else:
                charges.append(50)
                total_cost += 50
    return [total_cost - charge for charge in charges]

