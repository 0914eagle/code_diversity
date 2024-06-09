
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
            # Get the settlement at a distance j from the current affected settlement
            settlement_at_distance_j = current_settlement + j
            
            # Check if the settlement at distance j is within the range of settlements
            if settlement_at_distance_j <= n:
                # Add the settlement at distance j to the set of affected settlements
                affected_settlements.add(settlement_at_distance_j)
    
    # Return the set of affected settlements
    return affected_settlements

def get_possible_book_locations(n, m, d, p, q):
    # Get the set of affected settlements
    affected_settlements = get_affected_settlements(n, m, d, p)
    
    # Initialize a set to store the possible book locations
    possible_book_locations = set()
    
    # Iterate over the range of settlements
    for i in range(1, n + 1):
        # Check if the current settlement is not in the set of affected settlements
        if i not in affected_settlements:
            # Add the current settlement to the set of possible book locations
            possible_book_locations.add(i)
    
    # Return the set of possible book locations
    return possible_book_locations

def main():
    # Read the input
    n, m, d = map(int, input().split())
    p = list(map(int, input().split()))
    
    # Get the set of possible book locations
    possible_book_locations = get_possible_book_locations(n, m, d, p)
    
    # Print the number of possible book locations
    print(len(possible_book_locations))

if __name__ == '__main__':
    main()

