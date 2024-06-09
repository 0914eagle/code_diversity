
def get_max_volume(n, radii, heights):
    # Sort the cakes by height in descending order
    sorted_cakes = sorted(zip(radii, heights), key=lambda x: x[1], reverse=True)

    # Initialize the maximum volume
    max_volume = 0

    # Iterate over the cakes and calculate the volume of the stack
    for i in range(n):
        # Get the radius and height of the current cake
        radius, height = sorted_cakes[i]

        # Calculate the volume of the current cake
        volume = 3.14 * radius ** 2 * height

        # Check if the current cake can be placed on top of the previous cakes
        for j in range(i):
            # Get the radius and height of the previous cake
            prev_radius, prev_height = sorted_cakes[j]

            # Check if the current cake can be placed on top of the previous cake
            if radius > prev_radius and height + prev_height <= 10000:
                # Calculate the volume of the stack
                stack_volume = volume + 3.14 * prev_radius ** 2 * prev_height

                # Update the maximum volume
                max_volume = max(max_volume, stack_volume)

    return max_volume

if __name__ == '__main__':
    n = int(input())
    radii = list(map(int, input().split()))
    heights = list(map(int, input().split()))
    print(get_max_volume(n, radii, heights))

