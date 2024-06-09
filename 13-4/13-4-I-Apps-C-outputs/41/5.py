
def solve(n, k, camera_positions):
    # Initialize a set to store the covered walls
    covered_walls = set()
    # Initialize a list to store the number of cameras needed for each wall
    num_cameras_needed = [0] * (n + 1)
    # Iterate over the camera positions
    for i in range(k):
        # Get the current camera position
        a, b = camera_positions[i]
        # Check if the camera covers the whole building
        if a == 1 and b == n:
            # If it does, return the number of cameras needed (1)
            return 1
        # Add the walls covered by the camera to the set
        covered_walls.update(range(a, b + 1))
        # Increment the number of cameras needed for each wall covered by the camera
        for j in range(a, b + 1):
            num_cameras_needed[j] += 1
    # Initialize a variable to store the number of cameras needed
    num_cameras = 0
    # Iterate over the number of cameras needed for each wall
    for i in range(1, n + 1):
        # If the number of cameras needed for the current wall is greater than 0, increment the total number of cameras needed
        if num_cameras_needed[i] > 0:
            num_cameras += 1
    # Return the total number of cameras needed
    return num_cameras

