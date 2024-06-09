
def get_min_diff(h, w):
    # Initialize variables
    min_diff = float('inf')
    max_area = 0
    min_area = 0

    # Loop through all possible ways to divide the bar
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            # Calculate the area of each piece
            area_1 = i * j
            area_2 = (h - i) * j
            area_3 = (h - i) * (w - j)

            # Calculate the difference between the largest and smallest pieces
            diff = max(area_1, area_2, area_3) - min(area_1, area_2, area_3)

            # Update the minimum difference if necessary
            if diff < min_diff:
                min_diff = diff
                max_area = max(area_1, area_2, area_3)
                min_area = min(area_1, area_2, area_3)

    # Return the minimum difference and the areas of the largest and smallest pieces
    return min_diff, max_area, min_area

def main():
    # Read the input
    h, w = map(int, input().split())

    # Calculate the minimum difference and print the result
    min_diff, max_area, min_area = get_min_diff(h, w)
    print(min_diff)

if __name__ == '__main__':
    main()

