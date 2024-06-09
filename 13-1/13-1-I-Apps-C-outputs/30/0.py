
import math

def get_final_height(houses, k):
    # Initialize the final height of each house to its initial height
    final_heights = [house for house in houses]

    # Loop until all houses converge to a final height
    while True:
        # Check if all houses have converged to a final height
        if all(math.isclose(final_heights[i], final_heights[i+1], rel_tol=1e-6) for i in range(len(final_heights)-1)):
            break

        # Update the final height of each house
        for i in range(len(final_heights)):
            if i == 0:
                # Leftmost house: use the average height of the two neighboring houses
                final_heights[i] = (final_heights[i+1] + final_heights[i+2]) / 2 + k
            elif i == len(final_heights) - 1:
                # Rightmost house: use the average height of the two neighboring houses
                final_heights[i] = (final_heights[i-1] + final_heights[i-2]) / 2 + k
            else:
                # Middle houses: use the average height of the three neighboring houses
                final_heights[i] = (final_heights[i-1] + final_heights[i+1]) / 2 + k

    # Return the height of the tallest house
    return max(final_heights)

houses = [39, 10, 40]
k = 1
print(get_final_height(houses, k))

