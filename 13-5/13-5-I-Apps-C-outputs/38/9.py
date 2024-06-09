
def solve(N, M, K, grid):
    # Convert the grid into a 2D array for easier access
    grid = [[char for char in row] for row in grid.split("\n")]
    
    # Initialize the starting point as the current location
    current_location = (0, 0)
    
    # Initialize the number of days as 0
    days = 0
    
    # Initialize the stamina as the given value
    stamina = K
    
    # Initialize a set to keep track of the visited cells
    visited = set()
    
    # Loop until the current location is the treasure location
    while current_location != (N-1, M-1):
        # Check if the current location is valid
        if current_location[0] < 0 or current_location[0] >= N or current_location[1] < 0 or current_location[1] >= M:
            return -1
        
        # Check if the current location is a river
        if grid[current_location[0]][current_location[1]] == "#":
            return -1
        
        # Check if the current location is already visited
        if current_location in visited:
            return -1
        
        # Add the current location to the visited set
        visited.add(current_location)
        
        # Calculate the cost of moving to the next location
        cost = 0
        if grid[current_location[0]][current_location[1]] == ".":
            cost = 1
        elif grid[current_location[0]][current_location[1]] == "F":
            cost = 2
        elif grid[current_location[0]][current_location[1]] == "M":
            cost = 3
        
        # Check if the stamina is enough to move to the next location
        if stamina < cost:
            # Replenish the stamina to the full value
            stamina = K
            # Increment the number of days
            days += 1
        
        # Deduct the cost from the stamina
        stamina -= cost
        
        # Find the next location to move to
        next_location = find_next_location(current_location, grid)
        
        # Update the current location
        current_location = next_location
    
    # Return the number of days needed to reach the treasure
    return days

# Find the next location to move to
def find_next_location(current_location, grid):
    # Initialize the next location as the current location
    next_location = current_location
    
    # Loop until a valid next location is found
    while True:
        # Generate a random direction to move in
        direction = random.choice(["up", "down", "left", "right"])
        
        # Check if the direction is valid
        if direction == "up" and current_location[0] > 0:
            next_location = (current_location[0] - 1, current_location[1])
        elif direction == "down" and current_location[0] < len(grid) - 1:
            next_location = (current_location[0] + 1, current_location[1])
        elif direction == "left" and current_location[1] > 0:
            next_location = (current_location[0], current_location[1] - 1)
        elif direction == "right" and current_location[1] < len(grid[0]) - 1:
            next_location = (current_location[0], current_location[1] + 1)
        
        # Check if the next location is valid
        if next_location[0] >= 0 and next_location[0] < len(grid) and next_location[1] >= 0 and next_location[1] < len(grid[0]):
            break
    
    # Return the next location
    return next_location

