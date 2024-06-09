
def get_min_energy(cliff):
    # Initialize the minimum energy required to complete the climb
    min_energy = 0
    
    # Loop through each row of the cliff
    for row in cliff:
        # Loop through each column of the current row
        for col in row:
            # If the current cell is not a start point, add its energy to the minimum energy required
            if col != "S":
                min_energy += int(col)
    
    return min_energy

def solve(cliff):
    # Get the minimum energy required to complete the climb
    min_energy = get_min_energy(cliff)
    
    # Initialize the optimal route with the starting position
    optimal_route = ["S"]
    
    # Loop through each row of the cliff
    for row in cliff:
        # Loop through each column of the current row
        for col in row:
            # If the current cell is not a start point, add it to the optimal route
            if col != "S":
                optimal_route.append(col)
    
    # Return the minimum energy required to complete the climb and the optimal route
    return min_energy, optimal_route

if __name__ == '__main__':
    # Read the input from stdin
    R, C = map(int, input().split())
    cliff = []
    for _ in range(R):
        cliff.append(list(map(int, input().split())))
    
    # Solve the problem
    min_energy, optimal_route = solve(cliff)
    
    # Print the minimum energy required to complete the climb
    print(min_energy)
    
    # Print the optimal route
    print(" ".join(optimal_route))

