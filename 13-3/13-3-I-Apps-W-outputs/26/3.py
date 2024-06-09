
def get_maximum_volume(n, radii, heights):
    # Sort the cakes by height in descending order
    sorted_cakes = sorted(zip(radii, heights), key=lambda x: x[1], reverse=True)

    # Initialize the maximum volume
    max_volume = 0

    # Iterate over the cakes
    for i in range(n):
        # Get the current cake
        current_radius, current_height = sorted_cakes[i]

        # Check if the current cake is the largest one
        if current_height == max(heights):
            # If it is, add its volume to the maximum volume
            max_volume += (current_radius ** 2) * current_height
            break

        # If the current cake is not the largest one, find the next cake that is smaller than it
        for j in range(i + 1, n):
            next_radius, next_height = sorted_cakes[j]
            if next_height < current_height:
                # If a smaller cake is found, add its volume to the maximum volume
                max_volume += (next_radius ** 2) * next_height
                break

    return max_volume

