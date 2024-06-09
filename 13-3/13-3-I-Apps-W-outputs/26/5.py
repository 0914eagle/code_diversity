
def get_max_volume(n, radii, heights):
    # Sort the cakes by height in descending order
    sorted_cakes = sorted(zip(radii, heights), key=lambda x: x[1], reverse=True)

    # Initialize the maximum volume
    max_volume = 0

    # Iterate over the cakes
    for i in range(n):
        # Get the current cake
        current_radius, current_height = sorted_cakes[i]

        # Get the volume of the current cake
        current_volume = 3.14 * current_radius ** 2 * current_height

        # Check if the current cake can be placed on top of the previous cakes
        for j in range(i):
            # Get the previous cake
            previous_radius, previous_height = sorted_cakes[j]

            # Check if the current cake is taller than the previous cake
            if current_height > previous_height:
                # Calculate the volume of the current cake placed on top of the previous cake
                volume_on_top = 3.14 * current_radius ** 2 * current_height + 3.14 * previous_radius ** 2 * previous_height

                # Check if the volume on top is greater than the current maximum volume
                if volume_on_top > max_volume:
                    max_volume = volume_on_top

    return max_volume

if __name__ == '__main__':
    n = int(input())
    radii = list(map(int, input().split()))
    heights = list(map(int, input().split()))
    print(get_max_volume(n, radii, heights))

