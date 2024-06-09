
def get_energy_required(cliff):
    # Initialize a dictionary to store the minimum energy required to reach each square
    min_energy = {}
    for row in cliff:
        for col in row:
            min_energy[(row, col)] = float('inf')
    
    # Set the starting position to have zero energy required
    min_energy[(0, 0)] = 0
    
    # Loop through each square and calculate the minimum energy required to reach it
    for row in range(len(cliff)):
        for col in range(len(cliff[0])):
            # If the current square is not the starting position, check if the square above, below, left, and right has a lower energy required
            if (row, col) != (0, 0):
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    # If the square above, below, left, or right is not out of bounds and has a lower energy required, set the current square's energy required to that value plus the energy required to move to that square
                    if 0 <= row + dr < len(cliff) and 0 <= col + dc < len(cliff[0]) and min_energy[(row, col)] > min_energy[(row + dr, col + dc)] + cliff[row + dr][col + dc]:
                        min_energy[(row, col)] = min_energy[(row + dr, col + dc)] + cliff[row + dr][col + dc]
    
    # Return the minimum energy required to reach the bottom right square
    return min_energy[(len(cliff) - 1, len(cliff[0]) - 1)]

def main():
    # Read the input file
    with open('cliff.txt', 'r') as f:
        lines = f.readlines()
    
    # Get the number of rows and columns
    rows, cols = map(int, lines[0].split())
    
    # Create a 2D list to store the cliff
    cliff = []
    for i in range(rows):
        cliff.append(list(map(int, lines[i + 1].split())))
    
    # Get the starting positions
    starts = lines[-1].strip().split()
    
    # Initialize the minimum energy required to reach the bottom right square
    min_energy = float('inf')
    
    # Loop through each starting position and calculate the minimum energy required to reach the bottom right square
    for start in starts:
        row, col = map(int, start.split(','))
        min_energy = min(min_energy, get_energy_required(cliff[:row] + [[0] * cols] + cliff[row:]))
    
    # Print the minimum energy required to reach the bottom right square
    print(min_energy)

if __name__ == '__main__':
    main()

