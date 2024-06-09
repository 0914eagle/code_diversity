
def f1(n, positions):
    # Initialize a dictionary to store the results
    results = {}
    
    # Iterate over each position
    for position in positions:
        # Initialize a set to store the reachable positions
        reachable = set()
        
        # Iterate over each option
        for option in position:
            # Add the option to the reachable positions
            reachable.add(option)
        
        # Add the reachable positions to the results dictionary
        results[position] = reachable
    
    # Return the results dictionary
    return results

def f2(n, positions, start_position):
    # Initialize a dictionary to store the results
    results = {}
    
    # Iterate over each position
    for position in positions:
        # Initialize a set to store the reachable positions
        reachable = set()
        
        # Iterate over each option
        for option in position:
            # Add the option to the reachable positions
            reachable.add(option)
        
        # Add the reachable positions to the results dictionary
        results[position] = reachable
    
    # Return the results dictionary
    return results

if __name__ == '__main__':
    n = int(input())
    positions = [input().split() for _ in range(n)]
    start_position = input()
    results = f1(n, positions)
    print(f2(n, positions, start_position))

