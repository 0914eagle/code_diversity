
def get_smoothie_amount(distance, total_smoothie, carrying_capacity):
    # Initialize variables
    smoothie_amount = 0
    containers = []
    current_container = 0

    # Loop until all smoothie is consumed or the carrying capacity is reached
    while smoothie_amount < total_smoothie and current_container < carrying_capacity:
        # Calculate the amount of smoothie that can be carried in the current container
        container_smoothie = min(total_smoothie - smoothie_amount, carrying_capacity - current_container)

        # Add the container to the list of containers
        containers.append(container_smoothie)

        # Update the current container amount
        current_container += container_smoothie

        # Update the smoothie amount
        smoothie_amount += container_smoothie

    # Return the total amount of smoothie that can be brought to the family
    return smoothie_amount

