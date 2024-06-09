
def solve(n, l, luggage_positions):
    # Initialize the maximum speed to be the minimum speed
    max_speed = 0.1

    # Loop through each piece of luggage and check if it will collide with any other piece of luggage
    for i in range(n):
        for j in range(i+1, n):
            # Calculate the distance between the two pieces of luggage
            distance = abs(luggage_positions[i] - luggage_positions[j])

            # If the distance is less than or equal to the length of the circular conveyor belt, they will collide
            if distance <= l:
                # Update the maximum speed to be the minimum speed necessary to avoid the collision
                max_speed = max(max_speed, distance / l)

    # Return the maximum speed
    return max_speed

