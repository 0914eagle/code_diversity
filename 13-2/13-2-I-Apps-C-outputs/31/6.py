
def get_smoothie_amount(distance, total_smoothie, carrying_capacity):
    # Initialize variables
    smoothie_amount = 0
    containers = []
    current_container = 0

    # Loop until all smoothie is consumed or the family is reached
    while smoothie_amount < total_smoothie and distance > 0:
        # Calculate the amount of smoothie that can be consumed in the next step
        step_smoothie = min(distance, carrying_capacity)

        # Add the smoothie to the current container
        containers[current_container] += step_smoothie

        # Update the smoothie amount and distance
        smoothie_amount += step_smoothie
        distance -= step_smoothie

        # If the current container is full, move to the next one
        if containers[current_container] == carrying_capacity:
            current_container += 1

    # Return the amount of smoothie that can be brought to the family
    return smoothie_amount

