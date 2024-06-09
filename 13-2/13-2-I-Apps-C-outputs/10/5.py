
def get_maximum_participants(n, k, preferences):
    # Sort the preferences in descending order
    sorted_preferences = sorted(preferences, reverse=True)

    # Initialize the maximum number of participants that can join
    max_participants = 0

    # Iterate through the preferences and check if the current participant can join
    for i in range(n):
        # Check if the current participant has a preference that is not already satisfied
        if sorted_preferences[i] != i + 1:
            # Check if the current participant's preference is within the capacity of the bus
            if sorted_preferences[i] <= k:
                # Increment the maximum number of participants that can join
                max_participants += 1
            else:
                # The current participant's preference is not within the capacity of the bus, so we cannot include them
                break

    return max_participants

