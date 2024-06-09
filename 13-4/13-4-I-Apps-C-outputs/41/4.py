
def solve(n, k, camera_ranges):
    # Initialize a set to store the covered walls
    covered_walls = set()
    # Initialize a variable to store the number of cameras
    num_cameras = 0
    # Loop through each camera range
    for a, b in camera_ranges:
        # If the camera range is valid
        if a <= b:
            # Add the walls covered by the camera to the set
            covered_walls |= set(range(a, b + 1))
        # If the camera range is invalid
        else:
            # Add the walls covered by the camera to the set
            covered_walls |= set(range(a, n + 1)) | set(range(1, b + 1))
        # Increment the number of cameras
        num_cameras += 1
    # If all walls are covered
    if len(covered_walls) == n:
        # Return the number of cameras
        return num_cameras
    # If not all walls are covered
    else:
        # Return the string "impossible"
        return "impossible"

