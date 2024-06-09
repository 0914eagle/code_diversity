
def get_energy_needed(cliff, start_points):
    # Initialize a dictionary to store the minimum energy needed to reach each point
    min_energy = {}
    for point in cliff:
        min_energy[point] = float('inf')
    for start_point in start_points:
        min_energy[start_point] = 0
    
    # Loop through the points in the cliff and calculate the minimum energy needed to reach each point
    for _ in range(len(cliff)):
        for point in cliff:
            if point not in min_energy:
                continue
            for neighbor in get_neighbors(point, cliff):
                energy = min_energy[point] + cliff[neighbor]
                if energy < min_energy[neighbor]:
                    min_energy[neighbor] = energy
    
    # Return the minimum energy needed to reach the bottom of the cliff
    return min_energy[cliff[-1]]

def get_neighbors(point, cliff):
    # Get the row and column of the point
    row, col = point
    
    # Get the neighbors of the point
    neighbors = []
    if row > 0:
        neighbors.append((row - 1, col))
    if row < len(cliff) - 1:
        neighbors.append((row + 1, col))
    if col > 0:
        neighbors.append((row, col - 1))
    if col < len(cliff[0]) - 1:
        neighbors.append((row, col + 1))
    
    # Return the neighbors that are in the cliff
    return [neighbor for neighbor in neighbors if neighbor in cliff]

def main():
    # Read the input
    R, C = map(int, input().split())
    cliff = [list(map(int, input().split())) for _ in range(R)]
    start_points = list(input())
    
    # Calculate the minimum energy needed to complete the climb
    min_energy = get_energy_needed(cliff, start_points)
    
    # Print the minimum energy needed
    print(min_energy)

if __name__ == '__main__':
    main()

