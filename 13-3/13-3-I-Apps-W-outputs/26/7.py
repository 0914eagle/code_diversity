
def get_max_volume(n, radii, heights):
    # Sort the cakes by height in descending order
    sorted_cakes = sorted(zip(radii, heights), key=lambda x: x[1], reverse=True)

    # Initialize the maximum volume
    max_volume = 0

    # Iterate over the cakes
    for i in range(n):
        # Get the current cake's radius and height
        radius, height = sorted_cakes[i]

        # Calculate the volume of the current cake
        volume = 3.14 * radius ** 2 * height

        # If the current cake's volume is greater than the maximum volume, update the maximum volume
        if volume > max_volume:
            max_volume = volume

    return max_volume

if __name__ == '__main__':
    n = int(input())
    radii = list(map(int, input().split()))
    heights = list(map(int, input().split()))
    print(get_max_volume(n, radii, heights))

