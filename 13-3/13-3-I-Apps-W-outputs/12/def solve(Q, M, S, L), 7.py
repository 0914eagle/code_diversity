
def solve(Q, M, S, L):
    # Calculate the total number of time slots
    total_slots = S + L * Q

    # Sort the time slots in ascending order
    sorted_slots = sorted([1] * S + [Q] * L)

    # Initialize the minimum time to complete all slots
    min_time = 0

    # Iterate through the sorted time slots
    for i in range(total_slots):
        # If the current slot is 1 second, add 1 to the minimum time
        if sorted_slots[i] == 1:
            min_time += 1

        # If the current slot is Q seconds, add Q to the minimum time
        elif sorted_slots[i] == Q:
            min_time += Q

    # Return the minimum time to complete all slots
    return min_time

