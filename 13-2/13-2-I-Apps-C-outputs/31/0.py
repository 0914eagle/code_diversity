
def get_smoothie_amount(distance, total_smoothie, carrying_capacity):
    # Initialize variables
    smoothie_amount = 0
    containers = []
    current_container = 0

    # Loop until all smoothie is consumed or the family is reached
    while smoothie_amount < total_smoothie and distance > 0:
        # Calculate the amount of smoothie that can be consumed in the next step
        step_smoothie = min(distance, carrying_capacity)
        smoothie_amount += step_smoothie
        distance -= step_smoothie

        # If the current container is full, add it to the list of containers and get a new one
        if current_container == carrying_capacity:
            containers.append(current_container)
            current_container = 0

        # Add the smoothie to the current container
        current_container += step_smoothie

    # Calculate the total amount of smoothie that can be brought to the family
    total_family_smoothie = 0
    for container in containers:
        total_family_smoothie += container

    return total_family_smoothie

