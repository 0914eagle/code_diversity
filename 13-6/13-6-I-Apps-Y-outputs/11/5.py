
def get_min_diff(H, W):
    # Initialize variables
    min_diff = float('inf')
    max_area = 0
    min_area = 0

    # Iterate over all possible ways to divide the bar into three pieces
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            # Calculate the area of each piece
            area1 = i * j
            area2 = (H - i) * j
            area3 = (H - i) * (W - j)

            # Calculate the difference between the largest and smallest pieces
            diff = max(area1, area2, area3) - min(area1, area2, area3)

            # Update the minimum difference if necessary
            if diff < min_diff:
                min_diff = diff
                max_area = max(area1, area2, area3)
                min_area = min(area1, area2, area3)

    # Return the minimum difference and the areas of the largest and smallest pieces
    return min_diff, max_area, min_area

def main():
    # Read the input
    H, W = map(int, input().split())

    # Calculate the minimum difference and the areas of the largest and smallest pieces
    min_diff, max_area, min_area = get_min_diff(H, W)

    # Print the minimum difference
    print(min_diff)

if __name__ == '__main__':
    main()

