
def solve(m, h1, a1, x1, y1, h2, a2, x2, y2):
    # Initialize the minimum time to -1
    min_time = -1

    # Create a set to store the visited states
    visited = set()

    # Initialize the current state
    current_state = (h1, h2)

    # Initialize the time step
    time_step = 0

    # Loop until the minimum time is found or the queue is empty
    while min_time == -1 and current_state not in visited:
        # Add the current state to the visited set
        visited.add(current_state)

        # Check if the current state is the desired state
        if current_state == (a1, a2):
            # If it is, return the time step
            min_time = time_step
            break

        # Increment the time step
        time_step += 1

        # Calculate the next state
        next_state = (((x1 * current_state[0] + y1) % m), ((x2 * current_state[1] + y2) % m))

        # Add the next state to the queue
        current_state = next_state

    # Return the minimum time
    return min_time

