
def solve(n, k, cameras):
    # Initialize a set to store the covered walls
    covered_walls = set()
    # Initialize a variable to store the minimum number of cameras needed
    min_cameras = 0
    # Iterate through the cameras
    for camera in cameras:
        # If the camera covers a range of walls
        if camera[0] <= camera[1]:
            # Add the walls in the range to the covered walls set
            covered_walls.update(range(camera[0], camera[1] + 1))
        # If the camera covers a range of walls that wraps around the building
        else:
            # Add the walls in the first range to the covered walls set
            covered_walls.update(range(camera[0], n + 1))
            # Add the walls in the second range to the covered walls set
            covered_walls.update(range(1, camera[1] + 1))
    # Return the length of the covered walls set, which is the minimum number of cameras needed
    return len(covered_walls)

