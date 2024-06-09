
def get_max_volume(n, radii, heights):
    # Sort the cakes by height in descending order
    sorted_cakes = sorted(zip(radii, heights), key=lambda x: x[1], reverse=True)

    # Initialize the maximum volume and the current volume
    max_volume = 0
    current_volume = 0

    # Iterate through the sorted cakes
    for i in range(n):
        # Get the radius and height of the current cake
        radius, height = sorted_cakes[i]

        # Calculate the volume of the current cake
        current_volume = 3.14 * radius ** 2 * height

        # If the current volume is greater than the maximum volume, update the maximum volume
        if current_volume > max_volume:
            max_volume = current_volume

    # Return the maximum volume
    return max_volume

if __name__ == '__main__':
    n = int(input())
    radii = list(map(int, input().split()))
    heights = list(map(int, input().split()))
    print(get_max_volume(n, radii, heights))

