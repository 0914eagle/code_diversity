
def get_affected_settlements(n, m, d, p):
    # Initialize a set to store the affected settlements
    affected_settlements = set()
    
    # Iterate over the list of affected settlements
    for i in range(m):
        # Get the current affected settlement
        current_settlement = p[i]
        
        # Add the current affected settlement to the set of affected settlements
        affected_settlements.add(current_settlement)
        
        # Iterate over the range of damage range
        for j in range(1, d + 1):
            # Get the settlements at distance j from the current affected settlement
            settlements_at_distance_j = get_settlements_at_distance(n, current_settlement, j)
            
            # Add the settlements at distance j to the set of affected settlements
            affected_settlements.update(settlements_at_distance_j)
    
    # Return the set of affected settlements
    return affected_settlements

def get_settlements_at_distance(n, settlement, distance):
    # Initialize a set to store the settlements at distance
    settlements_at_distance = set()
    
    # Iterate over the paths
    for i in range(n - 1):
        # Get the ends of the current path
        a, b = input().split()
        
        # Check if the current path connects the settlement and a settlement at distance
        if a == settlement and b in settlements_at_distance:
            # Add the settlement at distance to the set of settlements at distance
            settlements_at_distance.add(b)
    
    # Return the set of settlements at distance
    return settlements_at_distance

if __name__ == '__main__':
    # Read the input
    n, m, d = map(int, input().split())
    p = list(map(int, input().split()))
    
    # Get the affected settlements
    affected_settlements = get_affected_settlements(n, m, d, p)
    
    # Print the number of affected settlements
    print(len(affected_settlements))

