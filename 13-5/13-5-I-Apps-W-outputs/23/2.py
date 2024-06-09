
def get_charges(trips):
    charges = []
    total_cost = 0
    for trip in trips:
        if trip == 0:
            charges.append(0)
            continue
        if trip == 1:
            charges.append(20)
            total_cost += 20
            continue
        if trip == 90:
            charges.append(50)
            total_cost += 50
            continue
        if trip == 1440:
            charges.append(120)
            total_cost += 120
            continue
    
    return [total_cost - charge for charge in charges]

