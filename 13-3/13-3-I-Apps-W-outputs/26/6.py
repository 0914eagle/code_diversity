
def get_max_volume(n, radii, heights):
    # Sort the cakes by height in descending order
    sorted_cakes = sorted(zip(radii, heights), key=lambda x: x[1], reverse=True)

    # Initialize the maximum volume
    max_volume = 0

    # Loop through the cakes and calculate the volume of each combination
    for i in range(n):
        for j in range(i):
            volume = (sorted_cakes[i][0] ** 2) * sorted_cakes[i][1] + (sorted_cakes[j][0] ** 2) * sorted_cakes[j][1]
            max_volume = max(max_volume, volume)

    return max_volume

if __name__ == '__main__':
    n = int(input())
    radii = []
    heights = []
    for i in range(n):
        r, h = map(int, input().split())
        radii.append(r)
        heights.append(h)
    print(get_max_volume(n, radii, heights))

