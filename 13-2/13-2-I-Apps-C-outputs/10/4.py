
def get_maximum_participants(n, k, preferences):
    # Sort the preferences in descending order
    sorted_preferences = sorted(preferences, reverse=True)

    # Initialize the maximum number of participants that can join
    max_participants = 0

    # Iterate through the preferences and check if the current participant can join
    for i in range(n):
        # Check if the current participant has a preference that is not already in the group
        if sorted_preferences[i] not in preferences[:i]:
            # Check if the current participant's preference is within the capacity of the bus
            if sorted_preferences[i] <= k:
                # Add the current participant to the group
                max_participants += 1
            else:
                # The current participant cannot join the group, so break the loop
                break

    return max_participants

