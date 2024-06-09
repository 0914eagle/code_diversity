
def f1(N, K, directions, plants):
    # Initialize the final coordinates as the coordinates of the first plant
    final_coordinates = plants[0]
    
    # Iterate through the directions and plants
    for i in range(1, N):
        # Get the current plant coordinates
        current_coordinates = plants[i]
        
        # Get the direction of the jump
        direction = directions[i-1]
        
        # Calculate the new coordinates based on the direction
        if direction == "A":
            new_coordinates = (current_coordinates[0] + 1, current_coordinates[1] + 1)
        elif direction == "B":
            new_coordinates = (current_coordinates[0] + 1, current_coordinates[1] - 1)
        elif direction == "C":
            new_coordinates = (current_coordinates[0] - 1, current_coordinates[1] + 1)
        else:
            new_coordinates = (current_coordinates[0] - 1, current_coordinates[1] - 1)
        
        # Check if the new coordinates are within the bounds of the lake
        if new_coordinates[0] >= 0 and new_coordinates[0] <= 1000000000 and new_coordinates[1] >= 0 and new_coordinates[1] <= 1000000000:
            # If they are, update the final coordinates
            final_coordinates = new_coordinates
    
    return final_coordinates

def f2(final_coordinates):
    # Print the final coordinates
    print(final_coordinates)

if __name__ == '__main__':
    # Read the input
    N, K = map(int, input().split())
    directions = input()
    plants = []
    for i in range(N):
        x, y = map(int, input().split())
        plants.append((x, y))
    
    # Call the functions
    final_coordinates = f1(N, K, directions, plants)
    f2(final_coordinates)

