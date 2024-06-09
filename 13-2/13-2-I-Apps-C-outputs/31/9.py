
def get_smoothie_amount(distance, total_smoothie, carrying_capacity):
    # Initialize variables
    smoothie_amount = 0
    containers = []
    current_container = 0

    # Loop until all smoothie is consumed or the carrying capacity is reached
    while smoothie_amount < total_smoothie and carrying_capacity > 0:
        # Calculate the amount of smoothie that can be carried in the current container
        container_smoothie = min(carrying_capacity, total_smoothie - smoothie_amount)

        # Add the smoothie to the container
        containers.append(container_smoothie)

        # Update the smoothie amount and carrying capacity
        smoothie_amount += container_smoothie
        carrying_capacity -= container_smoothie

        # If the carrying capacity is reached, move to the next container
        if carrying_capacity == 0:
            current_container += 1
            carrying_capacity = total_smoothie

    # Calculate the total distance traveled
    total_distance = sum(distance * container for container in containers)

    # Calculate the total amount of smoothie consumed
    total_smoothie_consumed = sum(container for container in containers)

    # Calculate the amount of smoothie left over
    smoothie_left_over = total_smoothie - total_smoothie_consumed

    # Return the amount of smoothie that can be brought to the family
    return smoothie_left_over + (total_distance / distance) * smoothie_left_over

