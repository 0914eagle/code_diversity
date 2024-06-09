
def get_min_dollars(heights):
    # Initialize variables
    n = len(heights)
    dollars = 0
    current_height = 0

    # Iterate through the heights and calculate the minimum number of dollars needed to reach each pylon
    for i in range(n):
        # Calculate the difference in height between the current pylon and the next pylon
        diff = heights[i] - current_height

        # If the difference is positive, the player can safely pass to the next pylon without losing energy
        if diff > 0:
            current_height = heights[i]

        # If the difference is negative, the player needs to pay the absolute value of the difference to increase the height of the current pylon
        else:
            dollars += abs(diff)
            current_height = heights[i]

    # Return the total number of dollars needed to reach the last pylon
    return dollars

if __name__ == '__main__':
    n = int(input())
    heights = list(map(int, input().split()))
    print(get_min_dollars(heights))

