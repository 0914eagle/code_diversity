
def solve(n, k, cameras):
    # Initialize a set to store the covered walls
    covered_walls = set()
    # Initialize a variable to store the minimum number of cameras needed
    min_cameras = 0
    # Iterate through the cameras
    for camera in cameras:
        # Check if the camera covers any new walls
        new_walls = set(range(camera[0], camera[1] + 1)) - covered_walls
        # If the camera covers new walls, add them to the covered walls set
        if new_walls:
            covered_walls |= new_walls
            # Increment the minimum number of cameras needed
            min_cameras += 1
    # Check if all walls are covered
    if len(covered_walls) == n:
        return min_cameras
    else:
        return "impossible"

