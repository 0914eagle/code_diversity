
def get_min_dollars(heights):
    # Initialize variables
    n = len(heights)
    dollars = 0
    current_height = 0

    # Iterate through the heights and calculate the minimum number of dollars needed to reach each pylon
    for i in range(n):
        # Calculate the difference between the current height and the height of the next pylon
        diff = heights[i] - current_height

        # If the difference is positive, the player can safely pass to the next pylon
        if diff > 0:
            current_height = heights[i]
        # If the difference is negative, the player needs to pay money to increase the height of the current pylon
        else:
            dollars += -diff
            current_height = heights[i] + 1

    # Return the total number of dollars needed
    return dollars

if __name__ == '__main__':
    n = int(input())
    heights = list(map(int, input().split()))
    print(get_min_dollars(heights))

