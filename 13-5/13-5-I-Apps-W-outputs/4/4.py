
def get_minimal_weight(n, k, stages):
    # Initialize the weight of the rocket as 0
    weight = 0
    # Create a list to store the stages of the rocket
    rocket = []
    # Loop through the stages
    for i in range(n):
        # Check if the stage is already in the rocket
        if stages[i] not in rocket:
            # Add the stage to the rocket
            rocket.append(stages[i])
            # Update the weight of the rocket
            weight += ord(stages[i]) - ord('a') + 1
            # Check if the rocket has the required number of stages
            if len(rocket) == k:
                # Return the weight of the rocket
                return weight
    # If the rocket cannot be built with the given stages, return -1
    return -1
