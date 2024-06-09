
def get_number_of_ways(n):
    # Initialize a list to store the coordinates of the trenches
    trenches = []
    
    # Iterate over the input and add the coordinates of each trench to the list
    for i in range(n):
        x1, y1, x2, y2 = map(int, input().split())
        trenches.append((x1, y1, x2, y2))
    
    # Initialize a set to store the unique coordinates of the trenches
    unique_coords = set()
    
    # Iterate over the trenches and add the unique coordinates to the set
    for trench in trenches:
        unique_coords.add((trench[0], trench[1]))
        unique_coords.add((trench[2], trench[3]))
    
    # Initialize a dictionary to store the number of ways the guards can be placed on each coordinate
    guard_placements = {}
    
    # Iterate over the unique coordinates and set the number of ways the guards can be placed to 1
    for coord in unique_coords:
        guard_placements[coord] = 1
    
    # Iterate over the trenches and update the number of ways the guards can be placed on each coordinate
    for trench in trenches:
        x1, y1, x2, y2 = trench
        for x in range(min(x1, x2), max(x1, x2) + 1):
            for y in range(min(y1, y2), max(y1, y2) + 1):
                if (x, y) not in unique_coords:
                    continue
                guard_placements[(x, y)] *= 2
    
    # Return the sum of the number of ways the guards can be placed on each coordinate
    return sum(guard_placements.values())

