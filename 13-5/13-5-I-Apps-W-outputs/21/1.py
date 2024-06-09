
def closest_weight(weights, target):
    # Sort the weights in non-decreasing order
    weights.sort()
    # Initialize the closest distance as the difference between the target and the smallest weight
    closest_distance = abs(target - weights[0])
    # Initialize the closest weight as the smallest weight
    closest_weight = weights[0]
    # Iterate through the weights
    for weight in weights:
        # Calculate the distance between the target and the current weight
        distance = abs(target - weight)
        # If the distance is smaller than the closest distance, update the closest distance and weight
        if distance < closest_distance:
            closest_distance = distance
            closest_weight = weight
    # Return the closest weight
    return closest_weight

