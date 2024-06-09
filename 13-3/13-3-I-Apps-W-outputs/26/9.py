
def get_max_volume(n, radii, heights):
    # Sort the cakes by height in descending order
    sorted_cakes = sorted(zip(radii, heights), key=lambda x: x[1], reverse=True)

    # Initialize the maximum volume and the current volume
    max_volume = 0
    current_volume = 0

    # Iterate through the cakes and calculate the volume of the current stack
    for i in range(n):
        current_volume += 3.14 * sorted_cakes[i][0] ** 2 * sorted_cakes[i][1]
        max_volume = max(max_volume, current_volume)

    return max_volume

if __name__ == '__main__':
    n = int(input())
    radii = list(map(int, input().split()))
    heights = list(map(int, input().split()))
    print(get_max_volume(n, radii, heights))

