
def solve(N, L, luggage_positions):
    # Sort the luggage positions in ascending order
    sorted_positions = sorted(luggage_positions)

    # Initialize the maximum speed to be the minimum speed
    max_speed = 0.1

    # Iterate through each pair of luggage positions
    for i in range(N - 1):
        # Calculate the distance between the two luggage positions
        distance = sorted_positions[i + 1] - sorted_positions[i]

        # If the distance is less than the length of the circular conveyor belt,
        # then the luggage may collide
        if distance < L:
            # Calculate the minimum speed required to avoid the collision
            min_speed = (L - distance) / L

            # Update the maximum speed if necessary
            if min_speed > max_speed:
                max_speed = min_speed

    # Return the maximum speed or "no fika" if no collision-free speed exists
    if max_speed == 0.1:
        return "no fika"
    else:
        return max_speed

