
def get_min_energy(cliff, start_points):
    # Initialize a dictionary to store the minimum energy needed to reach each cell
    min_energy = {}
    for row in range(len(cliff)):
        for col in range(len(cliff[0])):
            min_energy[(row, col)] = float('inf')

    # Set the starting points with 0 energy
    for start_point in start_points:
        min_energy[start_point] = 0

    # Loop through each cell in the cliff
    for row in range(len(cliff)):
        for col in range(len(cliff[0])):
            # If the current cell is not a starting point, skip it
            if (row, col) not in min_energy:
                continue

            # Get the energy needed to reach the current cell
            energy = cliff[row][col]

            # If the energy is negative, it means the cell is a starting point, so skip it
            if energy < 0:
                continue

            # Get the neighbors of the current cell
            neighbors = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]

            # Loop through each neighbor and update the minimum energy needed to reach it
            for neighbor in neighbors:
                # If the neighbor is out of bounds or has already been visited, skip it
                if neighbor[0] < 0 or neighbor[1] < 0 or neighbor[0] >= len(cliff) or neighbor[1] >= len(cliff[0]) or neighbor in min_energy:
                    continue

                # Update the minimum energy needed to reach the neighbor
                min_energy[neighbor] = min(min_energy[neighbor], min_energy[(row, col)] + energy)

    # Return the minimum energy needed to reach the bottom-right cell
    return min_energy[(len(cliff)-1, len(cliff[0])-1)]

def main():
    # Read the input
    R, C = map(int, input().split())
    cliff = []
    for _ in range(R):
        cliff.append(list(map(int, input().split())))
    start_points = list(input())

    # Solve the problem
    min_energy = get_min_energy(cliff, start_points)

    # Print the output
    print(min_energy)

if __name__ == '__main__':
    main()

