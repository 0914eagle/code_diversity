
def get_min_light_radius(lantern_positions, street_length):
    # Sort the lantern positions in ascending order
    sorted_positions = sorted(lantern_positions)

    # Initialize the minimum light radius as the maximum lantern position
    min_light_radius = sorted_positions[-1]

    # Iterate over the lantern positions in reverse order
    for position in sorted_positions[::-1]:
        # Calculate the light radius for the current lantern position
        light_radius = (position + min_light_radius) / 2

        # Check if the light radius is sufficient to light the whole street
        if position - light_radius >= 0 and position + light_radius <= street_length:
            return light_radius

        # Update the minimum light radius for the next iteration
        min_light_radius = light_radius

    # If the loop completes, return the minimum light radius
    return min_light_radius

