
def get_smoothie_amount(distance, total_smoothie, carrying_capacity):
    # Initialize variables
    smoothie_amount = 0
    containers = []
    current_container = 0

    # Loop until all smoothie is consumed or the family is reached
    while smoothie_amount < total_smoothie and distance > 0:
        # Calculate the amount of smoothie that can be consumed in the next step
        step_smoothie = min(distance, carrying_capacity)

        # Consume the smoothie
        smoothie_amount += step_smoothie
        distance -= step_smoothie

        # Check if a container needs to be added or removed
        if smoothie_amount > carrying_capacity:
            # Add a container
            containers.append(smoothie_amount - carrying_capacity)
            smoothie_amount = carrying_capacity
        elif smoothie_amount < carrying_capacity and len(containers) > 0:
            # Remove a container
            smoothie_amount += containers.pop()

    return smoothie_amount

