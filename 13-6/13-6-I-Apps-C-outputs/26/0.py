
def get_sand_heights(n, m, w, h, volumes, x, mins, maxs):
    # Initialize the sand heights for each section
    sand_heights = [0] * n

    # Loop through each color of sand
    for color in range(m):
        # Get the minimum and maximum amount of sand for this color
        min_amount = mins[color]
        max_amount = maxs[color]

        # Loop through each section
        for section in range(n):
            # Calculate the amount of sand that can be placed in this section
            available_volume = max_amount - min_amount
            available_area = w - x[section]
            available_sand = available_volume * available_area

            # Calculate the amount of sand that needs to be placed in this section
            needed_sand = max_amount - sand_heights[section]

            # If there is enough sand to fill the section
            if available_sand >= needed_sand:
                # Add the needed sand to the section
                sand_heights[section] += needed_sand

                # Subtract the used sand from the total available volume
                available_volume -= needed_sand

                # Update the available area
                available_area = w - x[section]

                # If there is no more sand to fill the section
                if available_sand == 0:
                    break

    # Return the sand heights for each section
    return sand_heights

def get_min_max_difference(sand_heights):
    # Get the minimum and maximum sand heights
    min_height = min(sand_heights)
    max_height = max(sand_heights)

    # Calculate the difference between the minimum and maximum sand heights
    difference = max_height - min_height

    # Return the difference
    return difference

def main():
    # Read the input
    n, m, w, h = map(int, input().split())
    volumes = list(map(float, input().split()))
    x = list(map(float, input().split()))
    mins = [list(map(float, input().split())) for _ in range(n)]
    maxs = [list(map(float, input().split())) for _ in range(n)]

    # Get the sand heights for each section
    sand_heights = get_sand_heights(n, m, w, h, volumes, x, mins, maxs)

    # Get the minimum and maximum difference
    difference = get_min_max_difference(sand_heights)

    # Print the output
    print(f"{difference:.3f}")

if __name__ == '__main__':
    main()

