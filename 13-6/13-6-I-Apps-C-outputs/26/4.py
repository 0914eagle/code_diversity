
def get_input():
    n, m, w, h = map(int, input().split())
    volumes = list(map(float, input().split()))
    x_coords = list(map(float, input().split()))
    min_sand = [[0] * m for _ in range(n)]
    max_sand = [[0] * m for _ in range(n)]
    for i in range(n):
        min_sand[i] = list(map(float, input().split()))
        max_sand[i] = list(map(float, input().split()))
    return n, m, w, h, volumes, x_coords, min_sand, max_sand

def solve(n, m, w, h, volumes, x_coords, min_sand, max_sand):
    # Initialize the sand heights for each section
    sand_heights = [0] * n

    # Loop through each color of sand
    for color in range(m):
        # Calculate the total volume of sand for this color
        total_volume = sum(volumes[color] for color in range(m))

        # Calculate the minimum and maximum heights for this color
        min_height = min(min_sand[i][color] for i in range(n))
        max_height = max(max_sand[i][color] for i in range(n))

        # Calculate the minimum and maximum heights for this color in each section
        min_heights = [min(min_height, (min_sand[i][color] / total_volume) * h) for i in range(n)]
        max_heights = [max(max_height, (max_sand[i][color] / total_volume) * h) for i in range(n)]

        # Distribute the sand for this color evenly among the sections
        for i in range(n):
            sand_heights[i] += (max_heights[i] - min_heights[i]) * volumes[color] / total_volume

    # Calculate the minimum difference between the maximum and minimum heights of sand in the sections
    min_diff = min(sand_heights[i + 1] - sand_heights[i] for i in range(n - 1))

    return round(min_diff, 3)

def main():
    n, m, w, h, volumes, x_coords, min_sand, max_sand = get_input()
    print(solve(n, m, w, h, volumes, x_coords, min_sand, max_sand))

if __name__ == '__main__':
    main()

